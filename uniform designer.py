# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import pkg_resources.py2_warn
import six

from PyQt5 import QtCore, QtGui, QtWidgets

from uniform_gui import Ui_MainWindow
from uniform_design import table

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
         super(MainWindow, self).__init__()
         self.ui = Ui_MainWindow()
         self.ui.setupUi(self)
         
         self.ui.pushButton_exit.clicked.connect(self.exit_clicked)
         self.ui.pushButton_confirm.clicked.connect(self.confirm_clicked)
         
    def exit_clicked(self):
        self.close()
    
    def confirm_clicked(self):
        a = table(int(self.ui.lineEdit_row.text()), int(self.ui.lineEdit_column.text()))
        a.get_table()
        self.ui.label_result.setText(a.result)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
#    sys.exit(app.exec_())
    app.exec_()
    
    
    
