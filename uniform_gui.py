# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uniform_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(0, 410, 75, 23))
        self.pushButton_exit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 101))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_confirm = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_confirm.setGeometry(QtCore.QRect(230, 70, 75, 23))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.label_row = QtWidgets.QLabel(self.groupBox)
        self.label_row.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label_row.setAlignment(QtCore.Qt.AlignCenter)
        self.label_row.setObjectName("label_row")
        self.label_colunm = QtWidgets.QLabel(self.groupBox)
        self.label_colunm.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_colunm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_colunm.setObjectName("label_colunm")
        self.lineEdit_row = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_row.setGeometry(QtCore.QRect(70, 30, 121, 20))
        self.lineEdit_row.setObjectName("lineEdit_row")
        self.lineEdit_column = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_column.setGeometry(QtCore.QRect(70, 70, 121, 20))
        self.lineEdit_column.setObjectName("lineEdit_column")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(30, 200, 291, 121))
        self.label_result.setObjectName("label_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_confirm.setText(_translate("MainWindow", "確認"))
        self.label_row.setText(_translate("MainWindow", "因子數："))
        self.label_colunm.setText(_translate("MainWindow", "水準數："))
        self.label_result.setText(_translate("MainWindow", "TextLabel"))

