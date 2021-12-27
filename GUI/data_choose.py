import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Choose(object):
    def __init__(self, car_list) -> None:
        super().__init__()
        self.car_list = car_list

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1298, 885)
        Form.setAcceptDrops(False)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 1298, 885))
        self.tableView.setObjectName("tableView")
        self.tableView.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.Form = Form
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.tableView.clicked.connect(self.viewClicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Table"))
    
    def viewClicked(self, currentIndex):
        if currentIndex.row() not in self.car_list:
            self.car_list.append(currentIndex.row())
            self.setColortoRow(self.tableView.model(), currentIndex)
            self.Form.setWindowTitle("Element został dodany!")
        else:
            self.Form.setWindowTitle("Element znajduje się już na liście!")
        self.tableView.setModel(self.tableView.model())

    def setColortoRow(self, table, currentIndex):
        for j in range(table.columnCount()):
            table.data(currentIndex,role=Qt.BackgroundRole)
    
class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data


    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            if role == Qt.BackgroundRole:
                return QtGui.QColor(255,255,100)
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



