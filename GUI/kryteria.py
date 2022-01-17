
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Criteria(object):
    def setupUi(self, Form, dict):
        self.dict = dict
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(510, 411)
        Form.setStyleSheet("background-color:rgb(111, 111, 111)")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 90, 611, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_3.addWidget(self.checkBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.DatCar_label = QtWidgets.QLabel(Form)
        self.DatCar_label.setGeometry(QtCore.QRect(-150, 10, 851, 75))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(48)
        self.DatCar_label.setFont(font)
        self.DatCar_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DatCar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.DatCar_label.setObjectName("DatCar_label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 360, 75, 23))
        self.pushButton.setStyleSheet("background:rgb(204, 88, 90)")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.save_criteria)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Cena"))
        self.comboBox_4.setItemText(0, _translate("Form", "MINIMUM"))
        self.comboBox_4.setItemText(1, _translate("Form", "MAXIMUM"))
        self.checkBox_4.setText(_translate("Form", "Uwzględnij"))
        self.label_3.setText(_translate("Form", "Przebieg"))
        self.comboBox_3.setItemText(0, _translate("Form", "MINIMUM"))
        self.comboBox_3.setItemText(1, _translate("Form", "MAXIMUM"))
        self.checkBox_3.setText(_translate("Form", "Uwzględnij"))
        self.label_2.setText(_translate("Form", "Pojemność"))
        self.comboBox_2.setItemText(0, _translate("Form", "MINIMUM"))
        self.comboBox_2.setItemText(1, _translate("Form", "MAXIMUM"))
        self.checkBox_2.setText(_translate("Form", "Uwzględnij"))
        self.label.setText(_translate("Form", "Rok produkcji"))
        self.comboBox.setItemText(0, _translate("Form", "MINIMUM"))
        self.comboBox.setItemText(1, _translate("Form", "MAXIMUM"))
        self.checkBox.setText(_translate("Form", "Uwzględnij"))
        self.DatCar_label.setText(_translate("Form", "Kryteria"))
        self.pushButton.setText(_translate("Form", "Zatwierdź"))

    def save_criteria(self):
        if self.checkBox.isChecked():
            self.dict["Rok produkcji"] = self.comboBox.currentText()
        if self.checkBox_2.isChecked():
            self.dict["Pojemność"] = self.comboBox_2.currentText()   
        if self.checkBox_3.isChecked():
            self.dict["Przebieg"] = self.comboBox_3.currentText()
        if self.checkBox_4.isChecked():
            self.dict["Cena"] = self.comboBox_4.currentText()
        print(self.dict)
        self.Form.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Criteria()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
