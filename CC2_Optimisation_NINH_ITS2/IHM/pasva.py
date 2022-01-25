# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pasva.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PasVariantAccelere_NINH_ITS2 as e1q2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 140, 581, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 350, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.e1q2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 351, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 400, 811, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 751, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 901, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 681, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 280, 581, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 210, 581, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 351, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Trouver resultat"))
        self.label_4.setText(_translate("MainWindow", "Veuillez entrer la valeur d\'un pas s:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resultat:"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Recherche avec un pas variant accéleré</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Veuillez entrer la foction f(x),(remplace x par x(i,s,x1), par ex :x(i,s,x1)**5 - 5*x(i,s,x1)**3 -20*x(i,s,x1) +5:"))
        self.label_3.setText(_translate("MainWindow", "Veuillez entrer un point de départ x1:"))

    def e1q2(self):
        e1q2.y1 = self.lineEdit.text()
        e1q2.x1=float(self.lineEdit_2.text())
        e1q2.s=float(self.lineEdit_3.text())
        e1q2.i = 1
        r=e1q2.pasVA(e1q2.i,e1q2.s)
        b=("Le point x* ≈ "+str(r)+" est l\'optimum ")
        self.textBrowser.setText(b)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.quit())

