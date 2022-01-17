# TODO: komentarze przepisać na angielski potencjalnie

# cena, przebieg, pojemność, rok produkcji

import numpy as np
from typing import Union, Tuple, List, Iterable
from copy import deepcopy


# funkcja do porównywania punktów: wariant z minimalizacją wszystkich parametrów
# używana przy sortowaniu owd
def compare(y, x):
    # realizuje porównanie y <= x
    truth_tab = []
    n = len(y)
    for i in range(n):
        truth_tab.append(y[i] <= x[i])
    summary = sum(truth_tab)
    if summary == n:
        return True
    else:
        return False


# wersja sortowania naiwna z filtracją, zgodnie z konspektem z pierwszych labów:
# używane w sprawdzaniu poprawności klas w RMS
def naiwne_owd_v2(x: List):
    n = len(x)
    X = x[:]
    P = []

    for i in range(n):
        if len(X) == 0:
            break
        X_alter = X[:]
        m = len(X_alter)
        Y = X[0]
        for j in range(1, m):
            if compare(Y, X[j]):
                X_alter.remove(X[j])
            elif compare(X[j], Y):
                X_alter.remove(Y)
                Y = X[j]

        if Y not in P:
            P.append(Y)

        # poniżej bez kopii [:] listy iteracja po liście nam przeskoczy elementy po usunięciu,
        # dlatego musimy tej kopii użyć
        for elem in X_alter[:]:
            if compare(Y, elem):
                X_alter.remove(elem)

        if Y in X_alter:
            X_alter.remove(Y)
        X = X_alter[:]

    return P


# używane w RMS
def naiwne_owd_v3(x: Iterable,
                  weights: np.ndarray = None):
    """
    Does ideal point sorting of set x

    :param x: list of points to be sorted (must be either list of tuples or list of lists)
    :param weights: np.ndarray, rather then weights we pass eihter +1 or -1 here to choose what to min/max
    :return:
    """

    if not isinstance(x, list):
        raise TypeError("Wrong x input type!")
    elif weights is not None:
        # jeżeli nic nie podamy jako wagi, zakładam minimalizacje wszystkich kryteriów
        weights = np.array([1 for i in range(len(x[0]))])
    elif not isinstance(weights, np.ndarray):
        raise TypeError("Wrong weights input type!")

    X = np.array(x)
    X_list = deepcopy(x)
    X_altered = X_list[:]
    n = len(x)
    if n <= 1:
        return x
    P = []
    # ZMIANA: nie zliczam ani czasu ani ilości porównań
    # # do zliczania porównań:
    # L = 0
    # # do sprawdzania czasu obliczeń:
    # start = time.time()

    # znajdujemy współrzędne naszego punktu idealnego:
    # numpy to znacząco ułatwia, zakładamy tylko że podane dane na wejście
    # są w odpowiedniej formie (lista krotek/ lista list)
    xmin = np.min(X, axis=0)

    # dummy d:
    d = np.array([np.nan, np.nan])

    for i in range(n):
        distance_sq = (np.linalg.norm(xmin-X[i, :]))**2
        if i == 0:
            d = np.array([i, distance_sq])
        else:
            d = np.vstack([d, [i, distance_sq]])
    d_sorted = d[np.argsort(d[:, 1])]

    M = n
    m = 0
    while m <= M:
        X_temporary_list = X_altered[:]
        X_jm = X_list[int(d_sorted[m, 0])]

        # poniżej skipujemy jeden punkt, jak już go usunęliśmy, bez zmniejszania M
        if X_jm not in X_altered:
            m += 1
            continue

        # usuń z X wszystkie X(i) takie, że X(J(m))≤X(i);
        for elem in X_altered:
            if compare(X_jm, elem):
                X_temporary_list.remove(elem)
            # L += 1

        # usuń X(J(m)) z X;
        if X_jm in X_temporary_list:
            X_temporary_list.remove(X_jm)

        # dodaj X(J(m)) do listy punktów niezdominowanych P;
        P.append(X_jm)

        # aktualizacja zmiennych
        X_altered = X_temporary_list[:]
        M -= 1
        m += 1

    # total_time = time.time() - start
    return P  # L, total_time


# algorytm do rekomendacji topsis
def topsis_min(points: Iterable,
               weights: np.ndarray,
               norm='E') -> np.ndarray:
    """
    Function does topsis algorithm on a given set of points, where the ideal point is the minimal value
    from all vector coordinates from the given points

    :param points: List[tuple[Union(int, float)]
    :param weights: np.ndarray- must be same length as the number of criterion of points - if negative, algorithm will
                    maximalise given criterion
    :param norm: str - either 'E' for Euclidean or 'C' for Chebyshev norms

    :return: np.ndarray - last column - calculated rating, second to last - distance (in the given norm)
             to the non-ideal point, third to last - distance to the ideal point
    """

    # each row will be a different point, each column - different criterion
    if not isinstance(points, np.ndarray):
        np_points_orig = np.array([points])
    else:
        np_points_orig = points.copy()

    # criterion rescaling:
    np_points = np_points_orig.copy()
    for i in range(np_points_orig.shape[1]):
        np_points[:, i] = np_points[:, i] / np.sqrt(np.sum(np_points[:, i])**2)

    # adding weights:
    np_points = np_points * weights

    # ideal point:
    p_ideal = np.min(np_points, axis=0)

    # non-ideal:
    p_non_ideal = np.max(np_points)

    # adding necessary columns for further calculations:
    ideal_dist = np.array([])
    non_ideal_dist = np.array([])

    # calculating distace with given norm:
    if norm == 'E':
        for i in range(np_points.shape[0]):
            ideal_dist = np.append(ideal_dist, np.linalg.norm(np_points[i, :] - p_ideal))
            non_ideal_dist = np.append(non_ideal_dist, np.linalg.norm(np_points[i, :] - p_non_ideal))
    elif norm == 'C':
        for i in range(np_points.shape[0]):
            ideal_dist = np.append(ideal_dist, np.linalg.norm(np_points[i, :] - p_ideal, ord=np.inf))
            non_ideal_dist = np.append(non_ideal_dist, np.linalg.norm(np_points[i, :] - p_non_ideal, ord=np.inf))
    else:
        raise ValueError('WRONG NORM INPUT')

    # necessary calculations:
    ranking = non_ideal_dist/(non_ideal_dist + ideal_dist)
    ranking = np.reshape(ranking, (len(ranking), 1))

    # reordering
    np_points_orig = np.concatenate((np_points_orig, ranking), axis=1)
    p_ordered = np_points_orig[np.argsort(np_points_orig[:, -1])][::-1, :]

    return p_ordered


# sprawdzanie klas do RMS:
def checking_class(i1_class: Iterable,
                   i2_class: Iterable):
    """
    sprawdza zgodność klas w RMS
    klasy powinny być podane już z odpowienio przemnożonymi wartościami (typu co min/max plus/minus)

    :param i1_class: klasa aspiracji (w sensie ta teoretycznie lepsza)
    :param i2_class: klasa teoretycznie gorsza
    :return: poprawione klasy jako krotka
    """

    # klasa i
    i1_edit = i1_class[:]

    # klasa i
    i2_edit = i2_class[:]

    while True:
        # sprawdzamy punkty niezdominowane z klasy i
        non_dom_i1 = naiwne_owd_v2(i1_edit)
        non_dom_i2 = naiwne_owd_v2(i2_edit)

        # łączymy te punkty
        connected_i = i1_edit + i2_edit

        # sprawdzamy niezdominowane w połączeniu
        non_dom_connected = naiwne_owd_v2(connected_i)

        # helper zmienne
        missing_point = None

        # patrzymy czy jakiegoś punktu niezdominowanego brakuje:
        for elem in non_dom_i1:
            if elem in non_dom_connected:
                continue
            # jak znaleźliśmy punkt którego brakuje, wychodzimy z pętli for
            # i naprawiamy tylko ten jeden przypadek
            missing_point = elem
            break

        # jeżeli w połączonym-niezdominowanym są wszystkie niezdominowane z i-1
        # --> klasy nie są sprzeczne
        if missing_point is None:
            # tutaj jak dojdziemy to znaczy że klasy nie są sprzeczne, wychodzim z pętli while
            break

        # jeżeli jakiegoś brakuje --> sprawdzamy który punkt należy usunąć z i
        np_non_dom_con = np.array(non_dom_connected)
        ideal = np.min(np_non_dom_con, axis=0)
        np_non_dom_i2 = np.array(non_dom_i2)

        # patrze które są najlbiżej pseudo punktu idealnego, i najbliższy w i2 usuwam
        d = np.array([np.nan, np.nan])
        for i in range(len(non_dom_i2)):
            distance_sq = (np.linalg.norm(ideal-np_non_dom_i2[i, :]))**2
            if i == 0:
                d = np.array([i, distance_sq])
            else:
                d = np.vstack([d, [i, distance_sq]])
        d_sorted = d[np.argsort(d[:, 1])]
        idx = int(d_sorted[0, 0])
        closest = np.array(non_dom_i2[idx])

        closest = tuple(closest.tolist())
        i2_edit.remove(closest)
        # powtarzamy procedurę aż bedzie break

    # zwracamy poprawione klasy
    return i1_edit, i2_edit


# algorytm RMS do rekomendacji na podstawie wprowadzonych klas
def referance_rms(f_u: Union[np.ndarray, List[Union[Tuple, List]]],
                  status_quo: List[Union[Tuple, List]],
                  aspiration: List[Union[Tuple, List]],
                  anti_ideal: Union[np.ndarray, List[Union[Tuple, List]]] = None,
                  ll_optimality: Union[np.ndarray, List[Union[Tuple, List]]] = None) -> np.ndarray:
    """
    Does RMS algorithm on given sets of points.
    Passed classes already need to be correctly set (either negative, if given criterion needs to be maximised,
    or positive, if minimised)

    :param f_u: decision set (points to sort)
    :param status_quo: status-quo solutions
    :param aspiration: target points
    :param anti_ideal: anti-ideal points
    :param ll_optimality: lower limits of optimality
    :return: sorted f_u points with respective calculated value
    """

    # checking if the data is correct
    if not isinstance(f_u, list):
        raise TypeError("To musi być lista!")
    if not (isinstance(f_u[0], list) or isinstance(f_u[0], tuple)):
        raise TypeError("To musi być lista LIST lub KROTEK")

    # IMPORTANT : jeżeli nic nie będzie wychodzić, zakomentować poniższe do linijki 326 i sprawdzić znowu
    # class checking:
    # aspiration and status_quo:
    checked_aspiration, checked_quo = checking_class(aspiration, status_quo)
    if not checked_aspiration == aspiration:
        aspiration = deepcopy(checked_aspiration)
    if not checked_quo == status_quo:
        status_quo = deepcopy(checked_quo)

    # aspiration and f_u:
    checked_aspiration, checked_f_u = checking_class(aspiration, f_u)
    if not checked_aspiration == aspiration:
        aspiration = deepcopy(checked_aspiration)
    if not checked_f_u == f_u:
        f_u = deepcopy(checked_f_u)

    # f_u and status quo:
    checked_f_u, checked_quo = checking_class(f_u, status_quo)
    if not checked_f_u == f_u:
        f_u = deepcopy(checked_f_u)
    if not checked_quo == status_quo:
        status_quo = deepcopy(checked_quo)
    # zakomentować DO TEJ LINIJKI <326> TUTAJ


    # checking which points are not dominated
    # saving as np arrays to ease further calculations
    nd_f_u = np.array(naiwne_owd_v3(f_u))
    nd_status_quo = np.array(naiwne_owd_v3(status_quo))
    nd_aspiration = np.array(naiwne_owd_v3(aspiration))

    # normalization of points (all dimenstions 0-1)
    helper_rescaling = np.concatenate((nd_f_u, nd_status_quo, nd_aspiration))
    max_rescaling = helper_rescaling.max(axis=0)

    nd_f_u = nd_f_u/max_rescaling
    nd_status_quo = nd_status_quo/max_rescaling
    nd_aspiration = nd_aspiration/max_rescaling

    # centres of our sets of points, may be useful later:
    centre_status_quo = np.sum(nd_status_quo, axis=0)/nd_status_quo.shape[0]
    centre_aspiration = np.sum(nd_aspiration, axis=0)/nd_aspiration.shape[0]

    # extra classes of points:
    if anti_ideal is not None:
        nd_anti_ideal = naiwne_owd_v3(anti_ideal)
    if ll_optimality is not None:
        nd_ll_optimality = naiwne_owd_v3(ll_optimality)

    # creating necessary arrays to fillout
    depth, height, width = len(nd_f_u), len(nd_status_quo), len(nd_aspiration)
    scoring_array = np.zeros((depth, height, width))
    weight_array = np.zeros((height, width))

    # before loops calculate the weight_array:
    # each weight is the 'volume' of a n-dimensional cuboid with vertices on
    # respective points from status_quo - aspiration
    for i in range(height):
        for j in range(width):
            v1 = nd_status_quo[i]
            v2 = nd_aspiration[j]
            volume = np.product(v1 - v2)
            weight_array[i, j] = volume
    # normalizing the array:
    min_ = np.min(weight_array)
    max_ = np.max(weight_array)
    # case if min=max:
    if min_ == max_:
        weight_array = np.ones((height, width))
    else:
        weight_array = (weight_array - min_) / (max_ - min_)


    # 3 for-loops
    # d for depth
    for d in range(nd_f_u.shape[0]):
        u = nd_f_u[d, :]

        # h for height
        for h in range(nd_status_quo.shape[0]):
            a = nd_status_quo[h, :]

            # w for width
            for w in range(nd_aspiration.shape[0]):
                b = nd_aspiration[w, :]

                # logical expressions to check what to do: we check b <= u <= a in two steps
                # we use a special kind of comparison defined earlier

                # b <= u:
                bu = compare(b, u)
                # u <= a:
                ua = compare(u, a)

                # normal variant, inequality satisfied fully:
                if (bu + ua) == 2:
                    dist_quo = np.linalg.norm(u - a)
                    dist_aspiration = np.linalg.norm(b - u)
                    # the closer val is to 1 the better
                    val = dist_quo/(dist_quo + dist_aspiration)

                # unnormal variant, inequality not fully satisfied (both half-satisfied and
                # not satisfied at all)
                elif (bu + ua) < 2:
                    # TODO: implement after the rest is working
                    dist_quo = np.linalg.norm(u - centre_status_quo)
                    dist_aspiration = np.linalg.norm(centre_aspiration - u)
                    # the closer val is to 1 the better
                    val = dist_quo/(dist_quo + dist_aspiration)

                # for debugging:
                else:
                    raise ValueError('Coś nie tak z porównaniem')

                # TODO: implement if the rest is working if needed
                # # the worst variant: inequality not satisfied:
                # else:
                #     val = 0.5

                scoring_array[d, h, w] = val

    # final calculation of 'value'
    scoring_array = scoring_array * weight_array
    individual_scores = np.sum(scoring_array, axis=(1, 2))
    individual_scores = np.reshape(individual_scores, (len(individual_scores), 1))

    # sorting points
    sorted_u = np.concatenate((nd_f_u, individual_scores), axis=1)
    sorted_u = sorted_u[np.argsort(sorted_u[:, -1])][::-1, :]
    sorted_u[:, :-1] = sorted_u[:, :-1] * max_rescaling

    # wynik trzeba wyświetlić, ale nie nadpisywać!!!
    return sorted_u
