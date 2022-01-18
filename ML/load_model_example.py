import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from copy import deepcopy

def ML_predict(data: pd.DataFrame) -> pd.DataFrame:
    """
    OPIS

    :param data: dane, modele samochodów, dla których będziemy przewidywać ceny

    :return predictions: zwraca ndarray z wynikami przewidywań cen dla wprowadzonych modeli samochodów
    """
    filename = 'ML_model.sav'
    loaded_model = pickle.load(open("ML/" + filename, 'rb'))

    #PLIK cars.csv -> konstrukcja kolumny "Kategoria"
    df = pd.read_csv("Data/cars.csv")
    df.dropna(inplace=True)
    if df.isna().sum().sum() > 0: # tu po prostu rzucam error, można to jakoś rozbudować
        raise ValueError("W danych występują brakujące wartości")
    print(df)
    df["Age"] = 2022 - df["Rok produkcji"]
    temp = df.copy()
    table = temp.groupby(['Marka'])['Cena'].mean()
    temp = temp.merge(table.reset_index(), how='left', on='Marka')
    bins = [0, 0.2, 0.5, 0.7, 0.9, 1]
    # bins = [0,5000,8000,11000,15000,100000]
    kat_bins = ['Budget', 'Budget_plus', 'Medium', 'Medium_plus', 'Highend']
    df['Kategoria'] = pd.qcut(temp['Cena_y'], bins, labels=kat_bins)
    # df['Kategoria'] = pd.cut(temp['Cena_y'], bins,  right=False, labels=kat_bins)

    # utworzenie słownika category_dict marka : kategoria cenowa
    grouped_test = df[['Marka', 'Kategoria']]
    unique_val = grouped_test.drop_duplicates(subset='Marka', ignore_index=True)
    category_dict = {}
    for i in range(unique_val.shape[0]):
        category_dict[unique_val.iloc[i]['Marka']] = unique_val.iloc[i]['Kategoria']



    #DATA
    old_df = df
    df = deepcopy(data)
    if df.isna().sum().sum() > 0: # tu po prostu rzucam error, można to jakoś rozbudować
        raise ValueError("W danych występują brakujące wartości")
    df["Age"] = 2022 - df['Rok produkcji']
    # temp = df.copy()
    # table = temp.groupby(['Marka'])['Cena'].mean()
    # temp = temp.merge(table.reset_index(), how='left', on='Marka')
    #bins = [0, 0.2, 0.5, 0.7, 0.9, 1]
    # bins = [0,5000,8000,11000,15000,100000]
    #kat_bins = ['Budget', 'Budget_plus', 'Medium', 'Medium_plus', 'Highend']
    df['Kategoria'] = [category_dict[df.iloc[row]['Marka']] for row in range(df.shape[0])]
    # df['Kategoria'] = pd.cut(temp['Cena_y'], bins,  right=False, labels=kat_bins)
    if df.isna().sum().sum() > 0: # tu wcześniej działy się dziwne rzeczy, więc na wszelki wypadek wrzucam tu error
        raise ValueError("Ogolnie to nie powinno się wydarzyć, ale no w razie czego z nikąd się nagle NaN-y pewnie pojawiły")
    df.drop(['Marka', 'Model', 'Rok produkcji','Cena'], axis=1, inplace=True)
    df_dummies = dummies('Skrzynia biegów', df)
    df_dummies = dummies('Kolor', df_dummies)
    df_dummies = dummies('Nadwozie', df_dummies)
    df_dummies = dummies('Rodzaj paliwa', df_dummies)
    df_dummies = dummies('Gwarancja', df_dummies)
    df_dummies = dummies('Kategoria', df_dummies)
    df = df_dummies
    scaler = MinMaxScaler()
    num_vars = ['Przebieg', 'Pojemność', 'Age']
    scaler.fit(old_df[num_vars])
    df[num_vars] = scaler.transform(df[num_vars])
    # dane są gotowe, przechodzimy do MODEL PRZEWIDYWANIE
    x = df
    #uzupełnienie kolumn eh
    all_cols_to_model = ['ID',
                         'Przebieg',
                         'Pojemność',
                         'Age',
                         'Skrzynia biegów_mechanical',
                         'Kolor_blue',
                         'Kolor_brown',
                         'Kolor_green',
                         'Kolor_grey',
                         'Kolor_orange',
                         'Kolor_other',
                         'Kolor_red',
                         'Kolor_silver',
                         'Kolor_violet',
                         'Kolor_white',
                         'Kolor_yellow',
                         'Nadwozie_coupe',
                         'Nadwozie_hatchback',
                         'Nadwozie_liftback',
                         'Nadwozie_limousine',
                         'Nadwozie_minibus',
                         'Nadwozie_minivan',
                         'Nadwozie_pickup',
                         'Nadwozie_sedan',
                         'Nadwozie_suv',
                         'Nadwozie_universal',
                         'Nadwozie_van',
                         'Rodzaj paliwa_gasoline',
                         'Kategoria_Budget_plus',
                         'Kategoria_Medium',
                         'Kategoria_Medium_plus',
                         'Kategoria_Highend']
    current_cols = list(x.columns)
    for col in all_cols_to_model:
        if col not in current_cols:
            x[col] = [0 for i in range(x.shape[0])]
    x = x[all_cols_to_model]
    predictions = loaded_model.predict(x)
    data['Sugerowana cena'] = predictions
    #opłacalność (różnica cen + labels)
    data['Opłacalność'] = data['Sugerowana cena'] - data['Cena']
    bins = [-50000,-1500,-500,500,1500,50000]
    kat_bins = ['Zdecyowanie za wysoka cena', 'Lekko za wysoka cena', 'Optymalna cena', 'Opłacalne', 'Prawdziwa okazja!']
    data['Opłacalność'] = pd.cut(data['Opłacalność'], bins,  right=False, labels=kat_bins)
    return data


def dummies(col_name,df): #pomocnicza funkcja do ML_predict()
    temp = pd.get_dummies(df[[col_name]], drop_first=True)
    df = pd.concat([df,temp], axis=1)
    df.drop([col_name], axis=1, inplace=True)
    return df

'''
if __name__ == "__main__":
    # przykładowe wykorzystanie gotowego modelu z pliku
    # tylko że to nie zadziała, bo dane trzeba trochę przerobić, żeby można je było wrzucić do modelu
    # więc zrobiłem funkcję ML_predict(), która to ogarnia
    """
    df = pd.read_csv("../../DatCar_swd/Data/cars.csv")
    filename = 'ML_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    # przykład
    y = df.pop("Cena").iloc[[1, 120, 21, 7654, 343, 31142, 2137]]
    x = df.iloc[[1, 120, 21, 7654, 343, 31142, 2137]]
    print(x)
    print(y)
    predicted = loaded_model.predict(x)
    print(predicted)
    """

    # przykładowe użycie funkcji do przewidywania cen
    df = pd.read_csv("../../DatCar_swd/Data/cars.csv")
    #data = df.dropna()
    data = df.iloc[[1,69,420,2137,32121,1233,7544,10000]] #przykładowe kilka modeli samochodów
    #data = df.iloc[:1000]  # przykładowe kilka modeli samochodów
    #data = df.iloc[[4]]
    data.dropna(inplace=True)
    #data_x = data.drop(["Cena"],axis=1)
    #data_y = data["Cena"]
    predictions = ML_predict(data)
    print(predictions)
    #print("Cena przewidziana przez algorytm:\n",predictions)
    print("Cena faktyczna (z ogłoszenia):\n",data["Cena"])
    #print("Różnica w cenie (oszacowana przez algorytm - cena z ogłoszenia):\n",predictions - data_y)

    from sklearn.metrics import mean_squared_error
    #print("Root Mean Squared Error (RMSE): ", np.sqrt(mean_squared_error(predictions, data_y)))'''
