# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginIF.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginIF(object):
    def setupUi(self, LoginIF):
        LoginIF.setObjectName("LoginIF")
        LoginIF.resize(417, 319)
        self.centralwidget = QtWidgets.QWidget(LoginIF)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 160, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 192, 59, 15))
        self.label_2.setObjectName("label_2")
        self.Campo_usu = QtWidgets.QLineEdit(self.centralwidget)
        self.Campo_usu.setGeometry(QtCore.QRect(180, 160, 113, 23))
        self.Campo_usu.setObjectName("Campo_usu")
        self.Campo_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.Campo_senha.setGeometry(QtCore.QRect(180, 190, 113, 23))
        self.Campo_senha.setObjectName("Campo_senha")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 351, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../../Transferências/iconfinder/transferir.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 120, 141, 16))
        self.label_4.setStyleSheet("font: italic 12pt \"Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.Botao_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_entrar.setGeometry(QtCore.QRect(100, 230, 80, 23))
        self.Botao_entrar.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.Botao_entrar.setObjectName("Botao_entrar")
        self.Botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.Botao_sair.setGeometry(QtCore.QRect(230, 230, 80, 23))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Botao_sair.setFont(font)
        self.Botao_sair.setStyleSheet("font: 10pt \"Sans Serif\";")
        self.Botao_sair.setObjectName("Botao_sair")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 221, 16))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setObjectName("label_5")
        LoginIF.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginIF)
        self.Botao_sair.clicked.connect(LoginIF.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginIF)
        LoginIF.setFixedSize(LoginIF.width(), LoginIF.height())
        self.Botao_entrar.clicked.connect(self.Entrar)


    def Entrar(self):
        usu = self.Campo_usu.text()
        sen = self.Campo_senha.text()
        if usu == "admin" and sen == "admin":
            from Separador import Ui_Separador
            self.janela = QtWidgets.QMainWindow()
            self.sobre = Ui_Separador()
            self.sobre.setupUi(self.janela)
            self.janela.show()
            LoginIF.close()





    def retranslateUi(self, LoginIF):
        _translate = QtCore.QCoreApplication.translate
        LoginIF.setWindowTitle(_translate("LoginIF", "Login"))
        self.label.setText(_translate("LoginIF", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Usuario:</span></p></body></html>"))
        self.label_2.setText(_translate("LoginIF", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Senha:</span></p></body></html>"))
        self.label_4.setText(_translate("LoginIF", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Sistema CAP</span></p></body></html>"))
        self.Botao_entrar.setText(_translate("LoginIF", "Entrar"))
        self.Botao_sair.setText(_translate("LoginIF", "Sair"))
        self.label_5.setText(_translate("LoginIF", "<html><head/><body><p><span style=\" text-decoration: underline; color:#0055ff;\">Sistema cap: www.cap.ifrn.edu.br</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculadora = QtWidgets.QMainWindow()
    ui = Ui_LoginIF()
    ui.setupUi(Calculadora)
    Calculadora.show()
    sys.exit(app.exec_())