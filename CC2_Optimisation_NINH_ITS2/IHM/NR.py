# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NR.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import NewtonRaph_NINH_ITS2 as nr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 764)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 130, 581, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.l1 = QtWidgets.QLineEdit()
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 351, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 200, 581, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 351, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 270, 581, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 351, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 310, 541, 16))
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 340, 111, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 340, 131, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 370, 341, 91))
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 261, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(260, 20, 71, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 261, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 60, 71, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 370, 341, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(100, 30, 51, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 30, 91, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 520, 811, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 751, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 480, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.nr)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Méthode de Newton-Raphson</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Veuillez entrer la foction f(x):"))
        self.label_3.setText(_translate("MainWindow", "Veuillez entrer la foction dérive f\'(x):"))
        self.label_4.setText(_translate("MainWindow", "Veuillez entrer la valeur d\'epsilone :"))
        self.label_5.setText(_translate("MainWindow", "Vous voulez entrer un intervalle [a,b]  ou un point de départ xi ?"))
        self.radioButton.setText(_translate("MainWindow", "intervalle [a,b]"))
        self.radioButton_2.setText(_translate("MainWindow", "point de départ xi"))
        self.groupBox.setTitle(_translate("MainWindow", "Valeurs d\'intervalle:"))
        self.label_6.setText(_translate("MainWindow", "Veuillez entrer le 1er valeur d\'intervalle:"))
        self.label_7.setText(_translate("MainWindow", "Veuillez entrer le 2ème valeur d\'intervalle:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Valeurs d\'un point de départ:"))
        self.label_10.setText(_translate("MainWindow", "xi = "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Resultat:"))
        self.pushButton.setText(_translate("MainWindow", "Trouver resultat"))

    def nr(self):
        nr.y1=self.lineEdit.text()
        nr.y2=self.lineEdit_2.text()
        nr.eps=float(self.lineEdit_3.text())
        if self.radioButton.isChecked():
            nr.a=int(self.lineEdit_4.text())
            nr.b=int(self.lineEdit_5.text())
            nr.xi=float((nr.a+nr.b)/2)
        if self.radioButton_2.isChecked(): 
            nr.xi=float(self.lineEdit_6.text())
        
        nr.i=1
        
        while True :
            nr.xF=nr.xi-nr.f(nr.xi)/nr.f1(nr.xi)
            a=(f'\n---------------Iteration {nr.i}---------------'+f'\nx{nr.i+1}='+str(nr.xF)+ f'\n|f\'(x{nr.i+1})|=' +str(abs(nr.f(nr.xF)))+'\n')    

            self.textBrowser.setText(a)   
            if (nr.f(nr.xF)<nr.eps):
                break
            nr.xi=nr.xF
            nr.i=nr.i+1
        b=('\n------------------Solution------------------'+'\n'+f'\non a |f(x{nr.i+1})|='+str(nr.f(nr.xF))+ '< eps. Notre solution est donc : x* = ' +str(nr.xF))   

        self.textBrowser.setText(a+b)
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
