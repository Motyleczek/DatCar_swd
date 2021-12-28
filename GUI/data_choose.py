import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choose(object):
    def __init__(self, car_list, database) -> None:
        super().__init__()
        self.database = database
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
        self.Form = Form
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tableView.clicked.connect(self.viewClicked)
        self.filter.textChanged.connect(self.filter_car)

    def filter_car(self):
        _data = self.database[self.database.Marka.str.contains(self.filter.toPlainText()) | self.database.Model.str.contains(self.filter.toPlainText()) | self.database.Kolor.str.contains(self.filter.toPlainText()) | self.database["Skrzynia biegów"].str.contains(self.filter.toPlainText()) | self.database.Nadwozie.str.contains(self.filter.toPlainText()) ]
        new_model = pandasModel(_data, self.chosen_indexes)
        self.tableView.setModel(new_model)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Table"))
        self.label_29.setText(_translate("Form", "Filtracja:"))
    
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



