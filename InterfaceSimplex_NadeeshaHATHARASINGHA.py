# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Simplex.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

#Interface graphique Simplex/BigM pour 3 variables et 3 contraintes
#Donc marche que pour question 1 et 2

import Bigm as b

class Ui_Simplex(object):
    def setupUi(self, Simplex):
        Simplex.setObjectName("Simplex")
        Simplex.resize(955, 854)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        Simplex.setFont(font)
        Simplex.setMouseTracking(True)
        Simplex.setAutoFillBackground(False)
        Simplex.setStyleSheet("background-color: rgb(255, 250, 242);")
        Simplex.setAnimated(True)
        Simplex.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(Simplex)
        self.centralwidget.setObjectName("centralwidget")
        self.decohori = QtWidgets.QWidget(self.centralwidget)
        self.decohori.setGeometry(QtCore.QRect(-31, -21, 991, 161))
        self.decohori.setAutoFillBackground(False)
        self.decohori.setStyleSheet("background-color:rgb(129, 0, 97);\n"
"\n"
"")
        self.decohori.setObjectName("decohori")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.decohori)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.titre = QtWidgets.QLabel(self.decohori)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setAutoFillBackground(False)
        self.titre.setObjectName("titre")
        self.horizontalLayout_2.addWidget(self.titre)
        self.decoverti = QtWidgets.QWidget(self.centralwidget)
        self.decoverti.setGeometry(QtCore.QRect(0, 140, 201, 691))
        self.decoverti.setAutoFillBackground(False)
        self.decoverti.setStyleSheet("\n"
"background-color: rgb(241, 200, 203);")
        self.decoverti.setObjectName("decoverti")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.decoverti)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.maxi = QtWidgets.QComboBox(self.decoverti)
        self.maxi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.maxi.setObjectName("maxi")
        self.maxi.addItem("")
        self.maxi.addItem("")
        self.verticalLayout.addWidget(self.maxi)
        self.nomcontr = QtWidgets.QLabel(self.centralwidget)
        self.nomcontr.setGeometry(QtCore.QRect(250, 300, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nomcontr.setFont(font)
        self.nomcontr.setMouseTracking(True)
        self.nomcontr.setObjectName("nomcontr")
        self.nomfonc = QtWidgets.QLabel(self.centralwidget)
        self.nomfonc.setGeometry(QtCore.QRect(250, 170, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nomfonc.setFont(font)
        self.nomfonc.setMouseTracking(True)
        self.nomfonc.setObjectName("nomfonc")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 971, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(200, 150, 21, 711))
        self.line_2.setStyleSheet("color: rgb(229, 131, 131);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.resoudre = QtWidgets.QPushButton(self.centralwidget)
        self.resoudre.setGeometry(QtCore.QRect(470, 510, 159, 33))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.resoudre.setFont(font)
        self.resoudre.setMouseTracking(False)
        self.resoudre.setStyleSheet("border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgb(129, 0, 97);\n"
"border-top-color: rgb(255, 123, 97);\n"
"background-color:rgb(255, 241, 234)")
        self.resoudre.setObjectName("resoudre")
        self.nomres = QtWidgets.QLabel(self.centralwidget)
        self.nomres.setGeometry(QtCore.QRect(250, 550, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nomres.setFont(font)
        self.nomres.setMouseTracking(True)
        self.nomres.setObjectName("nomres")
        self.restab = QtWidgets.QTextEdit(self.centralwidget)
        self.restab.setGeometry(QtCore.QRect(250, 590, 651, 221))
        self.restab.setAutoFillBackground(False)
        self.restab.setObjectName("restab")
        self.tablefonc = QtWidgets.QTableWidget(self.centralwidget)
        self.tablefonc.setGeometry(QtCore.QRect(250, 210, 651, 81))
        self.tablefonc.setObjectName("tablefonc")
        self.tablefonc.setColumnCount(5)
        self.tablefonc.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(222, 183, 186))
        self.tablefonc.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(129, 0, 97))
        self.tablefonc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablefonc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablefonc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablefonc.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablefonc.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tablefonc.setItem(0, 0, item)
        self.tablecontr = QtWidgets.QTableWidget(self.centralwidget)
        self.tablecontr.setGeometry(QtCore.QRect(250, 340, 651, 151))
        self.tablecontr.setObjectName("tablecontr")
        self.tablecontr.setColumnCount(5)
        self.tablecontr.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(222, 183, 186))
        self.tablecontr.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablecontr.setItem(1, 0, item)
        self.zx1 = QtWidgets.QLineEdit(self.centralwidget)
        self.zx1.setGeometry(QtCore.QRect(270, 250, 113, 22))
        self.zx1.setObjectName("zx1")
        self.zx2 = QtWidgets.QLineEdit(self.centralwidget)
        self.zx2.setGeometry(QtCore.QRect(400, 250, 113, 22))
        self.zx2.setObjectName("zx2")
        self.zx3 = QtWidgets.QLineEdit(self.centralwidget)
        self.zx3.setGeometry(QtCore.QRect(530, 250, 113, 22))
        self.zx3.setObjectName("zx3")
        self.zb = QtWidgets.QLineEdit(self.centralwidget)
        self.zb.setText('0')
        self.zb.setEnabled(False)
        self.zb.setGeometry(QtCore.QRect(780, 250, 113, 22))
        self.zb.setObjectName("zb")
        self.zop = QtWidgets.QComboBox(self.centralwidget)
        self.zop.setGeometry(QtCore.QRect(670, 250, 73, 22))
        self.zop.setObjectName("zop")
        self.zop.addItem("")
        self.zop.addItem("")
        self.zop.addItem("")
        self.aop = QtWidgets.QComboBox(self.centralwidget)
        self.aop.setGeometry(QtCore.QRect(670, 380, 73, 22))
        self.aop.setObjectName("aop")
        self.aop.addItem("")
        self.aop.addItem("")
        self.aop.addItem("")
        self.bop = QtWidgets.QComboBox(self.centralwidget)
        self.bop.setGeometry(QtCore.QRect(670, 420, 73, 22))
        self.bop.setObjectName("bop")
        self.bop.addItem("")
        self.bop.addItem("")
        self.bop.addItem("")
        self.cop = QtWidgets.QComboBox(self.centralwidget)
        self.cop.setGeometry(QtCore.QRect(670, 450, 73, 22))
        self.cop.setObjectName("cop")
        self.cop.addItem("")
        self.cop.addItem("")
        self.cop.addItem("")
        self.ax1 = QtWidgets.QLineEdit(self.centralwidget)
        self.ax1.setGeometry(QtCore.QRect(280, 380, 113, 22))
        self.ax1.setObjectName("ax1")
        self.bx1 = QtWidgets.QLineEdit(self.centralwidget)
        self.bx1.setGeometry(QtCore.QRect(280, 420, 113, 22))
        self.bx1.setObjectName("bx1")
        self.cx1 = QtWidgets.QLineEdit(self.centralwidget)
        self.cx1.setGeometry(QtCore.QRect(280, 450, 113, 22))
        self.cx1.setObjectName("cx1")
        self.ax2 = QtWidgets.QLineEdit(self.centralwidget)
        self.ax2.setGeometry(QtCore.QRect(400, 380, 113, 22))
        self.ax2.setObjectName("ax2")
        self.bx2 = QtWidgets.QLineEdit(self.centralwidget)
        self.bx2.setGeometry(QtCore.QRect(400, 420, 113, 22))
        self.bx2.setObjectName("bx2")
        self.cx2 = QtWidgets.QLineEdit(self.centralwidget)
        self.cx2.setGeometry(QtCore.QRect(400, 450, 113, 22))
        self.cx2.setObjectName("cx2")
        self.cx3 = QtWidgets.QLineEdit(self.centralwidget)
        self.cx3.setGeometry(QtCore.QRect(530, 450, 113, 22))
        self.cx3.setObjectName("cx3")
        self.bx3 = QtWidgets.QLineEdit(self.centralwidget)
        self.bx3.setGeometry(QtCore.QRect(530, 420, 113, 22))
        self.bx3.setObjectName("bx3")
        self.ax3 = QtWidgets.QLineEdit(self.centralwidget)
        self.ax3.setGeometry(QtCore.QRect(530, 380, 113, 22))
        self.ax3.setObjectName("ax3")
        self.cb = QtWidgets.QLineEdit(self.centralwidget)
        self.cb.setGeometry(QtCore.QRect(780, 450, 113, 22))
        self.cb.setObjectName("cb")
        self.bb = QtWidgets.QLineEdit(self.centralwidget)
        self.bb.setGeometry(QtCore.QRect(780, 420, 113, 22))
        self.bb.setObjectName("bb")
        self.ab = QtWidgets.QLineEdit(self.centralwidget)
        self.ab.setGeometry(QtCore.QRect(780, 380, 113, 22))
        self.ab.setObjectName("ab")
        self.decoverti.raise_()
        self.decohori.raise_()
        self.nomcontr.raise_()
        self.nomfonc.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.resoudre.raise_()
        self.nomres.raise_()
        self.restab.raise_()
        self.tablefonc.raise_()
        self.tablecontr.raise_()
        self.zx1.raise_()
        self.zx2.raise_()
        self.zx3.raise_()
        self.zb.raise_()
        self.zop.raise_()
        self.aop.raise_()
        self.bop.raise_()
        self.cop.raise_()
        self.ax1.raise_()
        self.bx1.raise_()
        self.cx1.raise_()
        self.ax2.raise_()
        self.bx2.raise_()
        self.cx2.raise_()
        self.cx3.raise_()
        self.bx3.raise_()
        self.ax3.raise_()
        self.cb.raise_()
        self.bb.raise_()
        self.ab.raise_()
        Simplex.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Simplex)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 26))
        self.menubar.setObjectName("menubar")
        self.load = QtWidgets.QMenu(self.menubar)
        self.load.setObjectName("load")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        Simplex.setMenuBar(self.menubar)
        self.actionQuestion1 = QtWidgets.QAction(Simplex)
        self.actionQuestion1.setObjectName("actionQuestion1")
        self.actionQuestion2 = QtWidgets.QAction(Simplex)
        self.actionQuestion2.setObjectName("actionQuestion2")
        self.actionQuestion3 = QtWidgets.QAction(Simplex)
        self.actionQuestion3.setObjectName("actionQuestion3")
        self.load.addSeparator()
        self.load.addAction(self.actionQuestion1)
        self.load.addAction(self.actionQuestion2)
        self.menubar.addAction(self.load.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(Simplex)
        QtCore.QMetaObject.connectSlotsByName(Simplex)

    def retranslateUi(self, Simplex):
        _translate = QtCore.QCoreApplication.translate
        Simplex.setWindowTitle(_translate("Simplex", "Configuration"))
        self.titre.setText(_translate("Simplex", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#fffaf2;\">Configuration des Param??tres</span></p></body></html>"))
        self.maxi.setItemText(1, _translate("Simplex", "Maximisation"))
        self.maxi.setItemText(0, _translate("Simplex", "Minimisation"))
        self.nomcontr.setText(_translate("Simplex", "<html><head/><body><p><span style=\" font-size:16pt; color:#e58383;\">&gt;&gt; </span><span style=\" font-size:16pt; color:#810061;\">Contraintes</span></p></body></html>"))
        self.nomfonc.setText(_translate("Simplex", "<html><head/><body><p><span style=\" font-size:16pt; color:#e58383;\">&gt;&gt; </span><span style=\" font-size:16pt; color:#810061;\">Fonction objective:</span></p></body></html>"))
        self.resoudre.setText(_translate("Simplex", "R??soudre"))
        self.nomres.setText(_translate("Simplex", "<html><head/><body><p><span style=\" font-size:16pt; color:#e58383;\">&gt;&gt; </span><span style=\" font-size:16pt; color:#810061;\">R??sultat</span></p></body></html>"))
        item = self.tablefonc.verticalHeaderItem(0)
        item.setText(_translate("Simplex", "Z"))
        item = self.tablefonc.horizontalHeaderItem(0)
        item.setText(_translate("Simplex", "x1"))
        item = self.tablefonc.horizontalHeaderItem(1)
        item.setText(_translate("Simplex", "x2"))
        item = self.tablefonc.horizontalHeaderItem(2)
        item.setText(_translate("Simplex", "x3"))
        item = self.tablefonc.horizontalHeaderItem(4)
        item.setText(_translate("Simplex", "b"))
        __sortingEnabled = self.tablefonc.isSortingEnabled()
        self.tablefonc.setSortingEnabled(False)
        self.tablefonc.setSortingEnabled(__sortingEnabled)
        item = self.tablecontr.verticalHeaderItem(0)
        item.setText(_translate("Simplex", "A"))
        item = self.tablecontr.verticalHeaderItem(1)
        item.setText(_translate("Simplex", "B"))
        item = self.tablecontr.verticalHeaderItem(2)
        item.setText(_translate("Simplex", "C"))
        item = self.tablecontr.horizontalHeaderItem(0)
        item.setText(_translate("Simplex", "x1"))
        item = self.tablecontr.horizontalHeaderItem(1)
        item.setText(_translate("Simplex", "x2"))
        item = self.tablecontr.horizontalHeaderItem(2)
        item.setText(_translate("Simplex", "x3"))
        item = self.tablecontr.horizontalHeaderItem(4)
        item.setText(_translate("Simplex", "b"))
        __sortingEnabled = self.tablecontr.isSortingEnabled()
        self.tablecontr.setSortingEnabled(False)
        self.tablecontr.setSortingEnabled(__sortingEnabled)
        self.zop.setItemText(0, _translate("Simplex", "="))
        self.aop.setItemText(0, _translate("Simplex", "<="))
        self.aop.setItemText(1, _translate("Simplex", ">="))
        self.aop.setItemText(2, _translate("Simplex", "="))
        self.bop.setItemText(0, _translate("Simplex", "<="))
        self.bop.setItemText(1, _translate("Simplex", ">="))
        self.bop.setItemText(2, _translate("Simplex", "="))
        self.cop.setItemText(0, _translate("Simplex", "<="))
        self.cop.setItemText(1, _translate("Simplex", ">="))
        self.cop.setItemText(2, _translate("Simplex", "="))
        self.load.setTitle(_translate("Simplex", "Load"))
        self.menuExit.setTitle(_translate("Simplex", "Exit"))
        self.actionQuestion1.setText(_translate("Simplex", "Question1"))
        self.actionQuestion2.setText(_translate("Simplex", "Question2"))

        #Renvoie aux actions lorque les boutons de l'interface sont cliqu??s
        self.resoudre.clicked.connect(self.resoudre_clicked)
        # self.actionLoad.triggered.connect(self.menu_load_trigger)

        #Renvoie aux actions lorque qu'un choix d'op??rateur est fait pour les contraintes 
        # self.aop.activated.connect(self.aop_changed)
        # self.bop.activated.connect(self.bop_changed)
        # self.cop.activated.connect(self.cop_changed)


        
    def resoudre_clicked(self):
        
        self.restab.clear()
        #Expr(name, id, maxi, cx1, cx2, cx3, cz, op, cb)

        # Expression de Z
        Z = b.Expr("Z", 0, self.maxi.currentIndex(), float(self.zx1.text()), float(self.zx2.text()), float(self.zx3.text()), 1, 3, 0 )
        
        # Expression de c1
        A = b.Expr("A", 1, self.maxi.currentIndex(), float(self.ax1.text()), float(self.ax2.text()), float(self.ax3.text()), 0, self.aop.currentIndex()+1, float(self.ab.text()) )
        
        
        # Expression de c2
        print("Expression de la deuxi??me contrainte B:")
        B = b.Expr("B", 2, self.maxi.currentIndex(), float(self.bx1.text()), float(self.bx2.text()), float(self.bx3.text()), 0, self.bop.currentIndex()+1, float(self.bb.text()))
       
        # Expression de c3
        print("Expression de la deuxi??me contrainte C:")
        C = b.Expr("C", 3, self.maxi.currentIndex(), float(self.cx1.text()), float(self.cx2.text()), float(self.cx3.text()), 0, self.cop.currentIndex()+1, float(self.cb.text()))
        
        
        # Systeme
        sys = b.Systeme(Z, A, B, C)
        affGen = sys.affichageGeneral()
        print(affGen)
        affCan = sys.affichageCanonique()
        print(affCan)
        bigm=sys.ope_bigm()
        elem=sys.ope_elem()
        self.restab.setText("Forme G??n??rale:\n \"n" + affGen + '\n\n Forme Cannonique \n\n' + affCan +'\n\n Op??rations BigM \n\n' + bigm + '\n\n Solution finale \n\n' + elem)

                
                
        
        
        
    # def loadConfig(self, tab):
    #     print("load tableau")
    #     #On charge les informations des fichiers de configuration: un fichier de configuration par champs

    #     self.zx1.setText(tab[0][0])
    #     self.zx2.setText(tab[0][1])
    #     self.zx3.setText(tab[0][2])
    #     self.zb.setText(tab[0][3])
        
    #     self.ax1.setText(tab[1][0])
    #     self.ax2.setText(tab[1][1])
    #     self.ax3.setText(tab[1][2])
    #     self.ab.setText(tab[1][3]) 
        
    #     self.bx1.setText(tab[2][0])
    #     self.bx2.setText(tab[2][1])
    #     self.bx3.setText(tab[2][2])
    #     self.bb.setText(tab[2][3])
        
    #     self.bx1.setText(tab[3][0])
    #     self.bx2.setText(tab[3][1])
    #     self.bx3.setText(tab[3][2])
    #     self.bb.setText(tab[3][3])
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Simplex = QtWidgets.QMainWindow()
    ui = Ui_Simplex()
    ui.setupUi(Simplex)
    Simplex.show()
    sys.exit(app.exec_())

