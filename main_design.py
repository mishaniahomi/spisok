# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 731)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #F2F2F2;\n"
"    color: #333333;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4F7299;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #6699CC;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #666666;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #333333;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #333333;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #FFFFFF; \n"
"    color: #333333;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #CCCCCC;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(down.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF; \n"
"    color: #333333;\n"
"    border: 1px solid #CCCCCC;\n"
"    selection-background-color: #4F7299;\n"
"    selection-color: #FFFFFF;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4F7299;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTableView {\n"
"    border: 1px solid #CCCCCC;\n"
"    font: 14px Arial;\n"
"}\n"
"\n"
"QTableView QHeaderView::section {\n"
"    background-color: #4F7299;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font: bold;\n"
"}\n"
"\n"
"QTableView QHeaderView::section:hover {\n"
"    background-color: #6699CC;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border: none;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #4F7299;\n"
"    color: #FFFFFF;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("/* Цветовая палитра */\n"
"\n"
"body {\n"
"  background-color: #F5F5F5;\n"
"}\n"
"\n"
"table {\n"
"  background-color: #FFFFFF;\n"
"}\n"
"\n"
"th {\n"
"  background-color: #E0E0E0;\n"
"}\n"
"\n"
"button {\n"
"  background-color: #40739E;\n"
"}\n"
"\n"
"input {\n"
"  background-color: #E0E0E0;\n"
"}\n"
"\n"
"/* Шрифты */\n"
"\n"
"h1 {\n"
"  font-family: Arial;\n"
"  font-size: 16pt;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"table, th, td {\n"
"  font-family: Arial;\n"
"  font-size: 12pt;\n"
"}\n"
"\n"
"button {\n"
"  font-family: Arial;\n"
"  font-size: 12pt;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"input {\n"
"  font-family: Arial;\n"
"  font-size: 12pt;\n"
"}\n"
"\n"
"/* Макет */\n"
"\n"
"#top-bar {\n"
"  display: flex;\n"
"  justify-content: space-between;\n"
"  align-items: center;\n"
"}\n"
"\n"
"#table-container {\n"
"  margin: 0 auto;\n"
"}\n"
"\n"
"table {\n"
"  width: 100%;\n"
"}\n"
"\n"
"#bottom-bar {\n"
"  display: flex;\n"
"  justify-content: space-between;\n"
"  align-items: center;\n"
"}\n"
"\n"
"/* Детали дизайна */\n"
"\n"
"th {\n"
"  text-align: center;\n"
"  padding: 5px;\n"
"}\n"
"\n"
"td {\n"
"  padding: 5px;\n"
"}\n"
"\n"
"button {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  padding: 5px 10px;\n"
"  color: white;\n"
"}\n"
"\n"
"input {\n"
"  border: 1px solid gray;\n"
"  border-radius: 5px;\n"
"  padding: 5px;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_8.addWidget(self.lineEdit_4)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_9.addWidget(self.lineEdit_5)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_10.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_10.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_10.addWidget(self.pushButton_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Списки"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_3.setText(_translate("MainWindow", "Имя"))
        self.label_2.setText(_translate("MainWindow", "Отчество"))
        self.label_6.setText(_translate("MainWindow", "Должность"))
        self.label_7.setText(_translate("MainWindow", "Звание"))
        self.label_4.setText(_translate("MainWindow", "Статус"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Отсутствующие"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Находящиеся"))
        self.comboBox.setItemText(2, _translate("MainWindow", "В ожидании"))
        self.pushButton_4.setText(_translate("MainWindow", "Импорт Exel"))
        self.pushButton.setText(_translate("MainWindow", "Сохр. Exel"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохр. Word"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_5.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить"))
