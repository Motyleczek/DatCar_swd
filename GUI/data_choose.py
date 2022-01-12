import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choose(object):
    def __init__(self, car_list, database) -> None:
        super().__init__()
        self.database = database
        self._data = database
        self.chosen_indexes = car_list

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1298, 885)
        Form.setAcceptDrops(False)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 1521, 885))
        self.tableView.setObjectName("tableView")
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.filter = QtWidgets.QPlainTextEdit(Form)
        self.filter.setGeometry(QtCore.QRect(1120, 30, 101, 31))
        self.filter.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filter.setObjectName("filter")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(1120, 5, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_29.setObjectName("label_29")

        self.filter_model = QtWidgets.QPlainTextEdit(Form)
        self.filter_model.setGeometry(QtCore.QRect(1120, 100, 101, 31))
        self.filter_model.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filter_model.setObjectName("filter_model")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(1120, 80, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_30.setObjectName("label_30")

        self.filter_nadwozie = QtWidgets.QPlainTextEdit(Form)
        self.filter_nadwozie.setGeometry(QtCore.QRect(1120, 170, 101, 31))
        self.filter_nadwozie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filter_nadwozie.setObjectName("filter_nadwozie")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(1120, 150, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_32.setObjectName("label_32")

        self.filter_skrzynia = QtWidgets.QPlainTextEdit(Form)
        self.filter_skrzynia.setGeometry(QtCore.QRect(1120, 250, 101, 31))
        self.filter_skrzynia.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filter_skrzynia.setObjectName("filter_skrzynia")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(1120, 230, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_33.setObjectName("label_33")

        self.filter_kolor = QtWidgets.QPlainTextEdit(Form)
        self.filter_kolor.setGeometry(QtCore.QRect(1120, 320, 101, 31))
        self.filter_kolor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filter_kolor.setObjectName("filter_kolor")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(1120, 300, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_31.setObjectName("label_31")
        self.Form = Form
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tableView.clicked.connect(self.viewClicked)
        self.filter.textChanged.connect(self.filter_car)
        self.filter_model.textChanged.connect(self.filter_car)
        self.filter_kolor.textChanged.connect(self.filter_car)
        self.filter_nadwozie.textChanged.connect(self.filter_car)
        self.filter_skrzynia.textChanged.connect(self.filter_car)

    def filter_car(self):
        self._data = self.database
        if self.filter.toPlainText() != "":
            self._data = self._data[self._data.Marka.str.contains(self.filter.toPlainText())]
        if self.filter_kolor.toPlainText() != "":
            self._data = self._data[self._data.Kolor.str.contains(self.filter_kolor.toPlainText())]
        if self.filter_model.toPlainText() != "":
            self._data = self._data[self._data.Model.str.contains(self.filter_model.toPlainText())]
        if self.filter_skrzynia.toPlainText() != "":
            self._data = self._data[self._data["Skrzynia biegów"].str.contains(self.filter_skrzynia.toPlainText())]
        if self.filter_nadwozie.toPlainText() != "":
            self._data = self._data[self._data.Nadwozie.str.contains(self.filter_nadwozie.toPlainText())]
        # _data = self.database[self.database.Marka.str.contains(self.filter.toPlainText()) | self.database.Model.str.contains(self.filter_model.toPlainText()) | self.database.Kolor.str.contains(self.filter_kolor.toPlainText()) | self.database["Skrzynia biegów"].str.contains(self.filter_skrzynia.toPlainText()) | self.database.Nadwozie.str.contains(self.filter_nadwozie.toPlainText()) ]
        new_model = pandasModel(self._data, self.chosen_indexes)
        self.tableView.setModel(new_model)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Table"))
        self.label_29.setText(_translate("Form", "Marka:"))
        self.label_30.setText(_translate("Form", "Model:"))
        self.label_31.setText(_translate("Form", "Kolor:"))
        self.label_32.setText(_translate("Form", "Nadwozie:"))
        self.label_33.setText(_translate("Form", "Skrzynia biegów:"))
    
    def viewClicked(self, currentIndex):
        if currentIndex.row() not in self.chosen_indexes:
            self.chosen_indexes.append(currentIndex.row())
            self.setColortoRow(self.tableView.model(), currentIndex)
            self.Form.setWindowTitle("Element został dodany!")
        else:
            self.chosen_indexes.remove(currentIndex.row())
            self.Form.setWindowTitle("Element został usunięty!")
            self.setColortoRow(self.tableView.model(), currentIndex)
        self.tableView.setModel(self.tableView.model())

    def setColortoRow(self, table, currentIndex):
        table.data(currentIndex, role=Qt.BackgroundRole)
    
class pandasModel(QAbstractTableModel):

    def __init__(self, data, selected):
        QAbstractTableModel.__init__(self)
        self._data = data
        self.collection = selected


    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            if role == Qt.BackgroundRole:
                if index.row() in self.collection:
                    return QtGui.QBrush(QtGui.QColor(255, 0, 0, 127))
                else:
                    return QtGui.QBrush(Qt.white)
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
                return self._data.columns[col]
        return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Choose()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



