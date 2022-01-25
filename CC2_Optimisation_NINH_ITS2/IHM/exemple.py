# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exemple.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import PasFix_NINH_ITS2 as e1q1
import PasVariantAccelere_NINH_ITS2 as e1q2
import Bissection_NINH_ITS2 as e1q3
import NewtonRaph_NINH_ITS2 as e2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 110, 361, 151))
        font = QtGui.QFont()
        font.setFamily("Tekton Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 170, 71, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.e1q1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 200, 71, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.e1q2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 230, 71, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.e1q3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 110, 71, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.e2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 771, 391))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 751, 341))
        self.textBrowser.setObjectName("textBrowser")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400; font-style:normal;\">Exemple - Exercice </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400; font-style:normal;\">Exercice 1:</span></p><p><span style=\" font-size:9pt;\">f(x) = x</span><span style=\" font-size:9pt; vertical-align:super;\">5</span><span style=\" font-size:9pt;\"> - 5x</span><span style=\" font-size:9pt; vertical-align:super;\">3 </span><span style=\" font-size:9pt;\">- 20x + 5</span></p><p><span style=\" font-size:9pt;\">1.Recherche avec un pas fixe. </span></p><p><span style=\" font-size:9pt;\">2. Recherche avec un pas fixe accéléré. </span></p><p><span style=\" font-size:9pt;\">3. Recherche via la méthode de la bissection.</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400; font-style:normal;\">Exercice 2:</span></p><p><span style=\" font-size:9pt;\">Trouvez l’optimum de la fonction suivante en utilisant </span></p><p><span style=\" font-size:9pt;\">les méthodes demandées : </span></p><p align=\"center\"><span style=\" font-size:9pt;\">f(x) = x</span><span style=\" font-size:9pt; vertical-align:super;\">5</span><span style=\" font-size:9pt;\"> - 5x</span><span style=\" font-size:9pt; vertical-align:super;\">3 </span><span style=\" font-size:9pt;\">- 20x + 5</span></p><p><span style=\" font-size:9pt;\">1. Méthode de Newton-Raphson avec un point initial x</span><span style=\" font-size:9pt; vertical-align:sub;\">0</span><span style=\" font-size:9pt;\"> = 5</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Résultat"))
        self.pushButton_2.setText(_translate("MainWindow", "Résultat"))
        self.pushButton_3.setText(_translate("MainWindow", "Résultat"))
        self.pushButton_4.setText(_translate("MainWindow", "Résultat"))
        self.groupBox.setTitle(_translate("MainWindow", "Résultat :"))
    
    def e1q1(self):
        e1q1.y1='x(i)**5 - 5*x(i)**3 -20*x(i) +5'
        e1q1.x1=0.0
        e1q1.s=0.05
        e1q1.i = 1
        r=(e1q1.pasfixe(e1q1.i))
        # a=print("Point minimum x* = "+str(r[1])+"\nf(x*)="+str(e1q1.f(r[0]))))
        a=("Point minimum x* = "+str(r[1])+"\nf(x*)="+str(e1q1.f(r[0])))
        self.textBrowser.setText(a)
    def e1q2(self):
        e1q2.y1 = 'x(i,s,x1)**5 - 5*x(i,s,x1)**3 -20*x(i,s,x1) +5'
        e1q2.x1=0.0
        e1q2.s=0.05
        e1q2.i = 1
        r=e1q2.pasVA(e1q2.i,e1q2.s)
        b=("Le point x* ≈ "+str(r)+" est l\'optimum ")
        self.textBrowser.setText(b)
    def e1q3(self):
        e1q3.y = 'x**5 - 5*x**3 -20*x +5'
        e1q3.valeurE = 0.1
        e1q3.a=0
        e1q3.b=1
        b=e1q3.bissection(e1q3.a, e1q3.b, e1q3.valeurE)
        x=('\n------------------Solution------------------'+'\n'+'En prenant le point médian de cet intervalle (L'+str(b[2])+') commeoptimal, on obtient :'+'\nx*= '+str(b[0])+' et f(x*)= '+str(b[1]))

        self.textBrowser.setText(x)
    def e2(self):
        e2.y1='x**3 - 7*x**2 + 8*x -3'
        e2.y2='3*x**2 - 14*x + 8'
        e2.xi=5
        e2.eps=0.001
        e2.i=1
        
        while True :
            e2.xF=e2.xi-e2.f(e2.xi)/e2.f1(e2.xi)
            a=(f'\n---------------Iteration {e2.i}---------------'+f'\nx{e2.i+1}='+str(e2.xF)+ f'\n|f\'(x{e2.i+1})|=' +str(abs(e2.f(e2.xF)))+'\n')    

            self.textBrowser.setText(a)   
            if (e2.f(e2.xF)<e2.eps):
                break
            e2.xi=e2.xF
            e2.i=e2.i+1
        b=('\n------------------Solution------------------'+'\n'+f'\non a |f(x{e2.i+1})|='+str(e2.f(e2.xF))+ '< eps. Notre solution est donc : x* = ' +str(e2.xF))   

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

