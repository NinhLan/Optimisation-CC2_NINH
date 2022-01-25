# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bissection.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Bissection_NINH_ITS2 as e1q3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 270, 581, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 351, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 130, 581, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 351, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 351, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 420, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.e1q3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 901, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 200, 581, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 470, 811, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 751, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 320, 351, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 350, 581, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 26))
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
        self.label_3.setText(_translate("MainWindow", "Veuillez entrer la valeur  près de la valeur exacte, valeurE:"))
        self.label_2.setText(_translate("MainWindow", "Veuillez entrer la foction f(x):"))
        self.label_4.setText(_translate("MainWindow", "Veuillez entrer le 1er valeur d\'intervalle: "))
        self.pushButton.setText(_translate("MainWindow", "Trouver resultat"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Méthode de la Bissection</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resultat:"))
        self.label_5.setText(_translate("MainWindow", "Veuillez entrer le 2ème valeur d\'intervalle: "))

    def e1q3(self):
        e1q3.y = self.lineEdit.text()
        e1q3.valeurE = float(self.lineEdit_2.text())
        e1q3.a=int(self.lineEdit_3.text())
        e1q3.b=int(self.lineEdit_4.text())
        b=e1q3.bissection(e1q3.a, e1q3.b, e1q3.valeurE)
        x=('\n------------------Solution------------------'+'\n'+'En prenant le point médian de cet intervalle (L'+str(b[2])+') commeoptimal, on obtient :'+'\nx*= '+str(b[0])+' et f(x*)= '+str(b[1]))

        self.textBrowser.setText(x)

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
