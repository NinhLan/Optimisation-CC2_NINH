# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bienvenue.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import exemple
import NR
import pasfix
import pasva
import bissection

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 140, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pasfix)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 210, 241, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pasva)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 280, 241, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.bissection)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 350, 241, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.nr)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 430, 241, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.exemple)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400; font-style:normal;\">Veuillez choisir la méthode que vous voulez utiliser</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Recherche avec un pas fixe"))
        self.pushButton_2.setText(_translate("MainWindow", "Recherche avec un pas variant accéleré"))
        self.pushButton_3.setText(_translate("MainWindow", "Méthode de la Bissection"))
        self.pushButton_4.setText(_translate("MainWindow", "Méthode de Newton-Raphson\n"
""))
        self.pushButton_5.setText(_translate("MainWindow", "Exemples - Exercice"))
        
    def pasfix(self):
        pasfix.show()
    def pasva(self):
        pasva.show()
    def bissection(self):
        bissection.show()
    def nr(self):
        nr.show()
    def exemple(self):
        ex.show()
    
                

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ex = exemple.MainWindow
nr = NR.MainWindow
pasfix = pasfix.MainWindow
pasva = pasva.MainWindow
bissection = bissection.MainWindow
ui.setupUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)    
    MainWindow.show()
    sys.exit(app.quit())
