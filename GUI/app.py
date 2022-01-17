import pandas as pd
import numpy as np
from kryteria import Ui_Criteria
from data_choose import Ui_Choose
from data_choose import pandasModel as pandasChooseModel
from data import pandasModel, Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from ..ML.load_model_example import ML_predict


class Ui_DatCar(object):
    def setupUi(self, DatCar):
        self.database = pd.DataFrame()
        self.selected_dream_id = []
        self.selected_owned_id = []
        self.selected_id = []
        self.selected_dream_cars = pd.DataFrame()
        self.selected_owned_cars = pd.DataFrame()
        self.selected_cars = pd.DataFrame()
        self.criterias = {}
        DatCar.setObjectName("DatCar")
        DatCar.resize(1130, 806)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DatCar.sizePolicy().hasHeightForWidth())
        DatCar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        DatCar.setFont(font)
        DatCar.setStyleSheet("background-color:rgb(111, 111, 111)")
        self.centralwidget = QtWidgets.QWidget(DatCar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DatCar_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(48)
        self.DatCar_label.setFont(font)
        self.DatCar_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DatCar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DatCar_label.setObjectName("DatCar_label")
        self.gridLayout.addWidget(self.DatCar_label, 0, 0, 1, 1)
        self.database_btn = QtWidgets.QPushButton(self.centralwidget)
        self.database_btn.setMaximumSize(QtCore.QSize(1077, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.database_btn.setFont(font)
        self.database_btn.setAccessibleDescription("")
        self.database_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.database_btn.setStyleSheet("background:rgb(204, 88, 90)")
        self.database_btn.setAutoDefault(False)
        self.database_btn.setDefault(False)
        self.database_btn.setFlat(False)
        self.database_btn.setObjectName("database_btn")
        self.gridLayout.addWidget(self.database_btn, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.YourDreamCar = QtWidgets.QWidget()
        self.YourDreamCar.setEnabled(True)
        self.YourDreamCar.setObjectName("YourDreamCar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.YourDreamCar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.YourDreamCar)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_marka = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_marka.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_marka.setObjectName("comboBox_marka")
        self.verticalLayout.addWidget(self.comboBox_marka)
        self.comboBox_paliwo = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_paliwo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_paliwo.setObjectName("comboBox_paliwo")
        self.verticalLayout.addWidget(self.comboBox_paliwo)
        self.comboBox_skrzynia = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_skrzynia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_skrzynia.setObjectName("comboBox_skrzynia")
        self.verticalLayout.addWidget(self.comboBox_skrzynia)
        self.comboBox_nadwozie = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_nadwozie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_nadwozie.setObjectName("comboBox_nadwozie")
        self.verticalLayout.addWidget(self.comboBox_nadwozie)
        self.comboBox_gwarancja = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_gwarancja.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_gwarancja.setObjectName("comboBox_stan")
        self.verticalLayout.addWidget(self.comboBox_gwarancja)
        self.comboBox_kolor = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_kolor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_kolor.setObjectName("comboBox_kolor")
        self.verticalLayout.addWidget(self.comboBox_kolor)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.Cena_OD = QtWidgets.QPlainTextEdit(self.frame_3)
        self.Cena_OD.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.Cena_OD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cena_OD.setObjectName("Cena_OD")
        self.Cena_DO = QtWidgets.QPlainTextEdit(self.frame_3)
        self.Cena_DO.setGeometry(QtCore.QRect(210, 30, 101, 31))
        self.Cena_DO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Cena_DO.setObjectName("Cena_DO")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(180, 40, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(20, 6, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.przebiegOD = QtWidgets.QPlainTextEdit(self.frame_4)
        self.przebiegOD.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.przebiegOD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.przebiegOD.setObjectName("przebiegOD")
        self.Przebieg_Do = QtWidgets.QPlainTextEdit(self.frame_4)
        self.Przebieg_Do.setGeometry(QtCore.QRect(210, 30, 101, 31))
        self.Przebieg_Do.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Przebieg_Do.setObjectName("Przebieg_Do")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(180, 40, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5.raise_()
        self.label.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.YourDreamCar)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.kryteria_btn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.kryteria_btn.setFont(font)
        self.kryteria_btn.setAccessibleDescription("")
        self.kryteria_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kryteria_btn.setStyleSheet("background:rgb(204, 88, 90)")
        self.kryteria_btn.setAutoDefault(False)
        self.kryteria_btn.setDefault(False)
        self.kryteria_btn.setFlat(False)
        self.kryteria_btn.setObjectName("kryteria_btn")
        self.verticalLayout_5.addWidget(self.kryteria_btn)
        self.najlepsza_rekomendacja_btn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.najlepsza_rekomendacja_btn.setFont(font)
        self.najlepsza_rekomendacja_btn.setAccessibleDescription("")
        self.najlepsza_rekomendacja_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.najlepsza_rekomendacja_btn.setStyleSheet("background:rgb(204, 88, 90)")
        self.najlepsza_rekomendacja_btn.setAutoDefault(False)
        self.najlepsza_rekomendacja_btn.setDefault(False)
        self.najlepsza_rekomendacja_btn.setFlat(False)
        self.najlepsza_rekomendacja_btn.setObjectName("najlepsza_rekomendacja_btn")
        self.verticalLayout_5.addWidget(self.najlepsza_rekomendacja_btn)
        self.horizontalLayout.addWidget(self.frame_2)
        self.tabWidget.addTab(self.YourDreamCar, "")
        self.rekomendacja_zbior = QtWidgets.QWidget()
        self.rekomendacja_zbior.setObjectName("rekomendacja_zbior")
        self.frame_6 = QtWidgets.QFrame(self.rekomendacja_zbior)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 1081, 578))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_11.addWidget(self.label_27)
        self.wybierz_samochody_btn = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn.setFont(font)
        self.wybierz_samochody_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn.setAutoFillBackground(False)
        self.wybierz_samochody_btn.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn.setDefault(False)
        self.wybierz_samochody_btn.setFlat(False)
        self.wybierz_samochody_btn.setObjectName("wybierz_samochody_btn")
        self.verticalLayout_11.addWidget(self.wybierz_samochody_btn)
        self.wybierz_samochody_btn_5 = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn_5.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn_5.setFont(font)
        self.wybierz_samochody_btn_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn_5.setAutoFillBackground(False)
        self.wybierz_samochody_btn_5.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn_5.setDefault(False)
        self.wybierz_samochody_btn_5.setFlat(False)
        self.wybierz_samochody_btn_5.setObjectName("wybierz_samochody_btn_5")
        self.verticalLayout_11.addWidget(self.wybierz_samochody_btn_5)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(204, 88, 90)")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.rekomendacja_zbior, "")
        self.dreamCar = QtWidgets.QWidget()
        self.dreamCar.setObjectName("dreamCar")
        self.frame_10 = QtWidgets.QFrame(self.dreamCar)
        self.frame_10.setGeometry(QtCore.QRect(10, 7, 1081, 571))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setLineWidth(2)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_28 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_13.addWidget(self.label_28)
        self.wybierz_samochody_btn_2 = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn_2.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn_2.setFont(font)
        self.wybierz_samochody_btn_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn_2.setAutoFillBackground(False)
        self.wybierz_samochody_btn_2.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn_2.setDefault(False)
        self.wybierz_samochody_btn_2.setFlat(False)
        self.wybierz_samochody_btn_2.setObjectName("wybierz_samochody_btn_2")
        self.verticalLayout_13.addWidget(self.wybierz_samochody_btn_2)
        self.wybierz_samochody_btn_3 = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn_3.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn_3.setFont(font)
        self.wybierz_samochody_btn_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn_3.setAutoFillBackground(False)
        self.wybierz_samochody_btn_3.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn_3.setDefault(False)
        self.wybierz_samochody_btn_3.setFlat(False)
        self.wybierz_samochody_btn_3.setObjectName("wybierz_samochody_btn_3")
        self.verticalLayout_13.addWidget(self.wybierz_samochody_btn_3)
        self.wybierz_samochody_btn_6 = QtWidgets.QPushButton(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn_6.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn_6.setFont(font)
        self.wybierz_samochody_btn_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn_6.setAutoFillBackground(False)
        self.wybierz_samochody_btn_6.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn_6.setDefault(False)
        self.wybierz_samochody_btn_6.setFlat(False)
        self.wybierz_samochody_btn_6.setObjectName("wybierz_samochody_btn_6")
        self.verticalLayout_13.addWidget(self.wybierz_samochody_btn_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background:rgb(204, 88, 90)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_13.addWidget(self.pushButton_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.tabWidget.addTab(self.dreamCar, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frame_11 = QtWidgets.QFrame(self.tab_4)
        self.frame_11.setGeometry(QtCore.QRect(10, 10, 1081, 571))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setLineWidth(2)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_29 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_15.addWidget(self.label_29)
        self.wybierz_samochody_btn_4 = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wybierz_samochody_btn_4.sizePolicy().hasHeightForWidth())
        self.wybierz_samochody_btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wybierz_samochody_btn_4.setFont(font)
        self.wybierz_samochody_btn_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wybierz_samochody_btn_4.setAutoFillBackground(False)
        self.wybierz_samochody_btn_4.setStyleSheet("background:rgb(204, 88, 90)")
        self.wybierz_samochody_btn_4.setDefault(False)
        self.wybierz_samochody_btn_4.setFlat(False)
        self.wybierz_samochody_btn_4.setObjectName("wybierz_samochody_btn_4")
        self.verticalLayout_15.addWidget(self.wybierz_samochody_btn_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background:rgb(204, 88, 90)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_15.addWidget(self.pushButton_3)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        DatCar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DatCar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        DatCar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DatCar)
        self.statusbar.setObjectName("statusbar")
        DatCar.setStatusBar(self.statusbar)

        self.retranslateUi(DatCar)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(DatCar)

        self.database_btn.clicked.connect(self.view_all_cars)
        self.kryteria_btn.clicked.connect(self.show_cars_fulfilling_criteria)
        self.najlepsza_rekomendacja_btn.clicked.connect(self.recommendation_with_criterias)
        self.wybierz_samochody_btn.clicked.connect(self.choose_cars)
        self.wybierz_samochody_btn_2.clicked.connect(self.choose_dream_cars)
        self.wybierz_samochody_btn_3.clicked.connect(self.choose_owned_cars)
        self.wybierz_samochody_btn_4.clicked.connect(self.choose_cars)
        self.wybierz_samochody_btn_5.clicked.connect(self.choose_criterias)
        self.wybierz_samochody_btn_6.clicked.connect(self.choose_criterias)
        self.pushButton.clicked.connect(self.recommend_topsis)
        self.pushButton_2.clicked.connect(self.recommend_rsm)
        self.pushButton_3.clicked.connect(self.rate_car)
        self.comboBox_paliwo.addItem("--")
        self.comboBox_marka.addItem("--")
        self.comboBox_skrzynia.addItem("--")
        self.comboBox_nadwozie.addItem("--")
        self.comboBox_kolor.addItem("--")
        self.comboBox_gwarancja.addItem("--")
 

    def retranslateUi(self, DatCar):
        _translate = QtCore.QCoreApplication.translate
        DatCar.setWindowTitle(_translate("DatCar", "DatCar"))
        self.DatCar_label.setText(_translate("DatCar", "DatCar"))
        self.database_btn.setText(_translate("DatCar", "Przeglądaj bazę samochodów"))
        self.label.setText(_translate("DatCar", "Kryteria"))
        self.label_2.setText(_translate("DatCar", "Marka"))
        self.label_4.setText(_translate("DatCar", "Rodzaj paliwa"))
        self.label_5.setText(_translate("DatCar", "Rodzaj skrzyni biegów"))
        self.label_7.setText(_translate("DatCar", "Rodzaj nadwozia"))
        self.label_6.setText(_translate("DatCar", "Gwarancja"))
        self.label_3.setText(_translate("DatCar", "Kolor"))
        self.label_8.setText(_translate("DatCar", "Cena"))
        self.label_9.setText(_translate("DatCar", "Od:"))
        self.label_10.setText(_translate("DatCar", "Do:"))
        self.label_11.setText(_translate("DatCar", "Przebieg"))
        self.label_12.setText(_translate("DatCar", "Od:"))
        self.label_13.setText(_translate("DatCar", "Do:"))
        self.kryteria_btn.setText(_translate("DatCar", "Przeglądaj samochody spełniające kryteria"))
        self.najlepsza_rekomendacja_btn.setText(_translate("DatCar", "Znajdź najlepszą ofertę"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YourDreamCar), _translate("DatCar", "Rekomendacja z uwzględnieniem kryteriów"))
        self.label_27.setText(_translate("DatCar", "Spośród wszystkich samochodów, wybierz te spośród których chcesz uzyskać rekomendację"))
        self.wybierz_samochody_btn.setText(_translate("DatCar", "Wybierz samochody"))
        self.wybierz_samochody_btn_5.setText(_translate("DatCar", "Wybierz odpowiednie kryteria"))
        self.pushButton.setText(_translate("DatCar", "Przeprowadź rekomendację"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rekomendacja_zbior), _translate("DatCar", "Rekomendacja sprośród zbioru"))
        self.label_28.setText(_translate("DatCar", "Wybierz wymarzony/e samochód/y, a następnie swój aktualny pojazd, aby aplikacja mogła znaleźć najlepsze rozwiązanie dla Ciebie!"))
        self.wybierz_samochody_btn_2.setText(_translate("DatCar", "Wybierz wymarzone samochody"))
        self.wybierz_samochody_btn_3.setText(_translate("DatCar", "Wybierz aktualny samochód"))
        self.wybierz_samochody_btn_6.setText(_translate("DatCar", "Wybierz odpowiednie kryteria"))
        self.pushButton_2.setText(_translate("DatCar", "Przeprowadź rekomendację"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dreamCar), _translate("DatCar", "Wymarzony samochód"))
        self.label_29.setText(_translate("DatCar", "Wybierz samochód a my sprawdzimy, czy jest on warty zakupu! "))
        self.wybierz_samochody_btn_4.setText(_translate("DatCar", "Wybierz samochód"))
        self.pushButton_3.setText(_translate("DatCar", "Oceń samochód"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("DatCar", "Ocena jakości samochodu"))

    def show_cars_fulfilling_criteria(self, sorted=False, topsis=False):
        # dodatek do funkcji wyświetlania po sortowaniach
        if sorted:
            self.cars = self.sorted_database
        elif topsis:
            self.cars = self.topsis_sorted
        else:
            self.cars = self.database

        if self.comboBox_marka.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Marka'] == self.comboBox_marka.currentText()]
        if self.comboBox_kolor.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Kolor'] == self.comboBox_kolor.currentText()]
        if self.comboBox_skrzynia.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Skrzynia biegów'] == self.comboBox_skrzynia.currentText()]
        if self.comboBox_nadwozie.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Nadwozie'] == self.comboBox_nadwozie.currentText()]
        if self.comboBox_paliwo.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Rodzaj paliwa'] == self.comboBox_paliwo.currentText()]
        if self.comboBox_gwarancja.currentText() != "--":
            self.cars = self.cars.loc[self.cars['Gwarancja'] == self.comboBox_gwarancja.currentText()]
        if self.Cena_OD.toPlainText():
            self.cars = self.cars.loc[self.cars['Cena'] > int(self.Cena_OD.toPlainText())]
        if self.Cena_DO.toPlainText():
            self.cars = self.cars.loc[self.cars['Cena'] < int(self.Cena_DO.toPlainText())]
        if self.przebiegOD.toPlainText():
            self.cars = self.cars.loc[self.cars['Przebieg'] > int(self.przebiegOD.toPlainText())]
        if self.Przebieg_Do.toPlainText():
            self.cars = self.cars.loc[self.cars['Przebieg'] < int(self.Przebieg_Do.toPlainText())]
        self.view_table_cars(self.cars)

    def read_data(self):
        # TODO zmiana tylko lokalnie -- usunąć przed MERGEM
        self.database = pd.read_csv("Data/cars.csv")
        #self.database = pd.read_csv("GUI/cars.csv")

    def initialize_criteria(self):
        self.paliwa = self.database["Rodzaj paliwa"].unique()
        self.marki = self.database["Marka"].unique()
        self.skrzynie = self.database["Skrzynia biegów"].unique()
        self.kolory = self.database["Kolor"].unique()
        self.nadwozia = self.database["Nadwozie"].unique()
        self.gwarancja = self.database["Gwarancja"].unique()
    
        self.comboBox_paliwo.addItems(self.paliwa)
        self.comboBox_marka.addItems(self.marki)
        self.comboBox_skrzynia.addItems(self.skrzynie)
        self.comboBox_nadwozie.addItems(self.nadwozia)
        self.comboBox_kolor.addItems(self.kolory)
        self.comboBox_gwarancja.addItems(([str(x) for x in self.gwarancja]))

    def view_all_cars(self):
        self.widget = QtWidgets.QWidget()
        self.table_window = Ui_Form()
        self.table_window.setupUi(self.widget)
        model = pandasModel(self.database)
        self.table_window.tableView.setModel(model)
        self.widget.show()

    def view_table_cars(self, data):
        self.widget = QtWidgets.QWidget()
        self.table_window = Ui_Form()
        self.table_window.setupUi(self.widget)
        model = pandasModel(data)
        self.table_window.tableView.setModel(model)
        self.widget.show()
    
    def recommendation_with_criterias(self):
        #DONE: wywołanie funkcji Michała i wyświetlenie wyniku -  niezdominowane wzgledem punktu idealnego

        # zrobimy to tak, że posortujemy WSZYSKTO, a potem wyświetlimy tylko te, które spełniają kryteria za pomocą
        # lekko zmodyfikowanego "show_cars_fulfilling_cryteria"

        # patrzymy na punkt idealny (znajdujemy go względem ceny, przebiegu, roku produkcji oraz pojemności)
        # dodajemy kolumne do dataframe
        # sortujemy resztę względem tej kolumny rosnąco
        # mamy posortowany dataframe
        self.sorted_database = self.database.copy()
        index_list = ["Przebieg", "Cena", "Rok produkcji", "Pojemność"]
        helper_df = self.sorted_database[index_list]
        helper_df.fillna(0)
        helper_np = helper_df.to_numpy()
        helper_np = np.nan_to_num(helper_np)

        # tutaj przy założeniu że wszystkie kryteria są równoważne
        to_norm = np.max(helper_np, axis=0)
        helper_np = helper_np/to_norm

        # minimalizujemy przebieg i cene, maksymalizujemy rok produkcji i pojemność
        helper_weights = np.array([1, 1, -1, -1])
        helper_np = helper_np * helper_weights
        ideal_point = np.min(helper_np, axis=0)
        distances = []
        for i in range(helper_np.shape[0]):
            distance = np.linalg.norm(helper_np[i, :] - ideal_point) / 1000
            distances.append(distance)
        self.sorted_database["sorting_distance"] = distances
        self.sorted_database = self.sorted_database.sort_values("sorting_distance")
        self.show_cars_fulfilling_criteria(sorted=True)

    def choose_cars(self):
        self.widget = QtWidgets.QWidget()
        self.table_window = Ui_Choose(self.selected_id, self.selected_cars, self.database)
        self.table_window.setupUi(self.widget)
        model = pandasChooseModel(self.database, self.selected_id)
        self.table_window.tableView.setModel(model)
        self.widget.show()
        print(self.selected_id)

    def choose_dream_cars(self):
        self.widget = QtWidgets.QWidget()
        self.table_window = Ui_Choose(self.selected_dream_id, self.selected_dream_cars, self.database)
        self.table_window.setupUi(self.widget)
        model = pandasChooseModel(self.database, self.selected_dream_id)
        self.table_window.tableView.setModel(model)
        self.widget.show()

    def choose_owned_cars(self):
        self.widget = QtWidgets.QWidget()
        self.table_window = Ui_Choose(self.selected_owned_id, self.selected_owned_cars, self.database)
        self.table_window.setupUi(self.widget)
        model = pandasChooseModel(self.database, self.selected_owned_id)
        self.table_window.tableView.setModel(model)
        self.widget.show()

    def choose_criterias(self):
        self.criterias_widget = QtWidgets.QWidget()
        self.criterias_list = Ui_Criteria()
        self.criterias_list.setupUi(self.criterias_widget, self.criterias)
        self.criterias_widget.show()

    def recommend_topsis(self):
        #Done: wywołanie metody Michała - topsis

        # wszystko od naciśnięcia guzika dzieje się tutaj
        # wybrane ID są w self.selected_id
        # kryteria są w self.criterias

        # lista wag, zgodnie z kolejnością: cena, przebieg, pojemność, rok produkcji
        # minimalizacja by default
        print(self.selected_cars)
        weights = [1, 1, 1, 1]
        keys = self.criterias.keys()
        if 'Cena' in keys:
            if self.criterias['Cena'] == "MAXIMUM":
                weights[0] = -1
        if 'Rok produkcji' in keys:
            if self.criterias['Rok produkcji'] == "MAXIMUM":
                weights[1] = -1
        if 'Pojemność' in keys:
            if self.criterias['Pojemność'] == "MAXIMUM":
                weights[2] = -1
        if 'Przebieg' in keys:
            if self.criterias['Przebieg'] == "MAXIMUM":
                weights[3] = -1

        lista_nazw = ["Cena", "Rok produkcji", "Przebieg", "Pojemność"]
        topsis_df = self.database[lista_nazw]
        topsis_df = topsis_df.iloc[self.selected_id]

        topsis_np = topsis_df.to_numpy()

        # unormowanie
        norma = np.linalg.norm(topsis_np)
        topsis_np = topsis_np/norma

        # uwzględnienie 'wag'
        topsis_np = np.nan_to_num(topsis_np * weights)

        # ideal point:
        p_ideal = np.min(topsis_np, axis=0)

        # non-ideal:
        p_non_ideal = np.max(topsis_np)

        # adding necessary columns for further calculations:
        ideal_dist = np.array([])
        non_ideal_dist = np.array([])

        # calculating distace with given norm:
        for i in range(topsis_np.shape[0]):
            ideal_dist = np.append(ideal_dist, np.linalg.norm(topsis_np[i, :] - p_ideal))
            non_ideal_dist = np.append(non_ideal_dist, np.linalg.norm(topsis_np[i, :] - p_non_ideal))

        # necessary calculations:
        ranking = non_ideal_dist/(non_ideal_dist + ideal_dist)
        ranking = np.reshape(ranking, (len(ranking), 1))

        final_df = self.database.iloc[self.selected_id]
        final_df["ranking"] = ranking

        final_df = final_df.sort_values("ranking", ascending=False)
        self.topsis_sorted = final_df
        self.show_cars_fulfilling_criteria(topsis=True)



    
    def recommend_rsm(self):
        #TODO: wywołanie metody Michała - rsm
        pass

    def rate_car(self):
        #TODO: wywołanie metody sprawdzającej czy warto kupić samochód
        #self.selected_cars
        pass

    sorted_database = None
    topsis_sorted = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DatCar = QtWidgets.QMainWindow()
    ui = Ui_DatCar()
    ui.setupUi(DatCar)
    ui.read_data()
    ui.initialize_criteria()
    DatCar.show()
    sys.exit(app.exec_())
