
# Ana Clara Da Silva Sales (clara.sales@escolar.ifrn.edu.br)
# Ana Gabrielly Da Silva Freitas (ana.gabrielly@escolar.ifrn.edu.br)
# Ana Maria Dos Santos Dantas (dantas.ana1@escolar.ifrn.edu.br)
# Ananda Emily Da Silva Gurgel (ananda.gurgel@escolar.ifrn.edu.br)
# Isaac Alef Barros Da Silva (isaac.barros@escolar.ifrn.edu.br)
# João Lourenço de Azevedo Neto (joao.lourenco@escolar.ifrn.edu.br)


# Importar bibliotecas usadas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import time

perguntas_facies = []
perguntas_medias = []
perguntas_dificies = []

def random_perguntas():

    # abre o arquivo txt das perguntas
    with open('../Projeto_programação_completo/perguntas.txt', 'r', encoding='utf-8') as arquivo:
        auxiliar = arquivo.readlines()

    # adiciona as perguntas do arquivo txt nas listas
    for i in auxiliar:
        try:
            pergunta = i.split("#")
            if pergunta[0] == "facil":
                perguntas_facies.append(i)
            elif pergunta[0] == "medio":
                perguntas_medias.append(i)
            elif pergunta[0] == "dificil":
                perguntas_dificies.append(i)
            else:
                pass
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("ERROR!!!")
            msg.setText(e)
            msg.exec_()

# chama função para adicionar as perguntas nas listas
random_perguntas()

class Ui_Interface_jogo(object):

    def __init__(self):
        # variável que auxiliar na mudança das imagens e visibilidade da senha
        self.asd = 2

        # armazena a dificuldade escolhida
        self.dificuldade = ""

        # armazena as respostas corretas das perguntas
        self.resposta_correta = 0

        # faz a contagem de acertos e erros
        self.acertos = 0
        self.erros = 0

    def ver_senha_login(self):

        # variáveis para mudar o icon do botao
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("senha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("contrasenha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # verifica a partir da variável auxiliar para saber qual imagem e se está ou não visível a senha
        # se tiver na "contrasenha.png" não estara visível (o padrao) e muda para
        # a imagem "senha.png" e estará visível, e vice e versa

        if self.asd == 2:
            self.botao_ver_senha_login.setIcon(icon2)

            # deixa a senha visível
            ui.colocar_senha_login.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.asd = 1

        else:
            self.botao_ver_senha_login.setIcon(icon)

            # esconde a senha (o padrao)
            ui.colocar_senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
            self.asd = 2

    def ver_senha_cadastrar(self):

        # variáveis para mudar o icon do botao
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("senha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("contrasenha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        # verifica a partir da variável auxiliar para saber qual imagem e se está ou não visível a senha
        # se tiver na "contrasenha.png" não estara visível (o padrao) e muda para
        # a imagem "senha.png" e estará visível, e vice e versa

        if self.asd == 2:
            self.botao_ver_senha_cadastrar.setIcon(icon2)

            # deixa a senha visível
            ui.colocar_senha_cadastro.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.asd = 1

        else:
            self.botao_ver_senha_cadastrar.setIcon(icon)

            # esconde a senha (o padrao)
            ui.colocar_senha_cadastro.setEchoMode(QtWidgets.QLineEdit.Password)
            self.asd = 2

    # messagem da tela do jogo, perguntando ser o usuário deseja volta para tela inicial
    def voltar_jogo(self):
        msgBox = QMessageBox()
        msgBox.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText('Deseja voltar pra tela inicial?')
        correctBtn = msgBox.addButton('Sim', QMessageBox.YesRole)
        incorrectBtn = msgBox.addButton('Não', QMessageBox.NoRole)

        msgBox.exec_()

        if msgBox.clickedButton() == correctBtn:
            # formata as informações do jogo: pontos, perguntas etc
            self.stackedWidget.setCurrentWidget(self.pagina_inicial)
            self.formatar_jogo()
            self.acertos = 0
            self.erros = 0
            random_perguntas()

    # volta formata a pontuação e as informações, colocando as informações padrões
    def formatar_jogo(self):
        self.pergunta.setText("Pergunta:")
        self.botao_letra_a.setText("A")
        self.botao_letra_b.setText("B")
        self.botao_letra_c.setText("C")
        self.botao_letra_d.setText("D")
        self.botao_letra_e.setText("E")
        self.acertos = 0
        self.erros = 0

    # função vai pegar as perguntas que tem nas listas e irá colocar na tela das perguntas
    def jogo(self):
        global aux1

        # irá pegar as perguntas fáceis e irá crescendo o nível, passsando por médias e difíceis , caso a pessoa escolha fácil
        if self.dificuldade == 'facil':
            if len(perguntas_facies) > 0:
                self.pergunta.setText("")
                aux1 = perguntas_facies[random.randint(0, len(perguntas_facies) - 1)]
                perguntas_facies.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas fáceis irá passar para as médias
            elif len(perguntas_facies) == 0 and len(perguntas_medias) > 0:
                aux1 = perguntas_medias[random.randint(0, len(perguntas_medias) - 1)]
                perguntas_medias.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas médias irá passar para as difíceis
            elif len(perguntas_facies) == 0 and len(perguntas_medias) == 0 and len(perguntas_dificies) > 0:
                aux1 = perguntas_dificies[random.randint(0, len(perguntas_dificies) - 1)]
                perguntas_dificies.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas difíceis irá mostrar a pontuação e a mensagem final
            else:
                self.pergunta.setText("")
                self.formatar_texto()
                self.pergunta.setStyleSheet("""
                                font: 16pt "MS Shell Dlg 2";

                                background-color: rgb(63, 73, 39);
                                border-radius:30px""")
                self.formatar_resposta()

                # mensagem da pontuação
                msg1 = QMessageBox()
                msg1.setIcon(QMessageBox.Information)
                msg1.setWindowTitle("pontuação")
                msg1.setText(f"acertos:{self.acertos}\nerros:{self.erros}")
                msg1.exec_()

                # mensagem do fim do jogo
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Fim de Jogo")
                msg.setText(
                    "Obrigado por jogar, esse jogo deu muito trabalho! \nespero que tenha gostado S2")
                msg.exec_()

                self.formatar_jogo()

                # irá reiniciar a lista das perguntas que foram sendo retiradas
                # após serem passadas na tela de perguntas
                random_perguntas()

        # irá pegar as perguntas médias e irá crescendo o nível, passsando por difíceis também, caso a pessoa escolha médio
        elif self.dificuldade == 'medio':

            if len(perguntas_medias) > 0:
                aux1 = perguntas_medias[random.randint(0, len(perguntas_medias) - 1)]
                perguntas_medias.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas médias irá passar para as difíceis
            elif len(perguntas_medias) == 0 and len(perguntas_dificies) > 0:
                aux1 = perguntas_dificies[random.randint(0, len(perguntas_dificies) - 1)]
                perguntas_dificies.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas difíceis irá mostrar a pontuação e a mensagem final
            else:
                self.pergunta.setText("")
                self.formatar_texto()
                self.pergunta.setStyleSheet("""
                                font: 16pt "MS Shell Dlg 2";

                                background-color: rgb(63, 73, 39);
                                border-radius:30px""")
                self.formatar_resposta()

                # mensagem da pontuação
                msg1 = QMessageBox()
                msg1.setIcon(QMessageBox.Information)
                msg1.setWindowTitle("pontuação")
                msg1.setText(f"acertos:{self.acertos}\nerros:{self.erros}")
                msg1.exec_()

                # mensagem do fim do jogo
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Fim de Jogo")
                msg.setText(
                    "Obrigado por jogar, esse jogo deu muito trabalho! \nespero que tenha gostado S2")
                msg.exec_()

                self.formatar_jogo()

                # irá reiniciar a lista das perguntas que foram sendo retiradas
                # após serem passadas na tela de perguntas
                random_perguntas()

        # irá pegar somente as perguntas difíceis já que é o último nível
        elif self.dificuldade == 'dificil':
            if len(perguntas_dificies) > 0:
                aux1 = perguntas_dificies[random.randint(0, len(perguntas_dificies) - 1)]
                perguntas_dificies.remove(aux1)
                aux1 = aux1.split("#")
                self.pergunta.setText(aux1[1])
                self.botao_letra_a.setText(aux1[2])
                self.botao_letra_b.setText(aux1[3])
                self.botao_letra_c.setText(aux1[4])
                self.botao_letra_d.setText(aux1[5])
                self.botao_letra_e.setText(aux1[6])
                self.resposta_correta = aux1[7]

            # quando acabar as perguntas difíceis irá mostrar a pontuação e a mensagem final
            else:
                self.pergunta.setText("")
                self.formatar_texto()
                self.pergunta.setStyleSheet("""
                                font: 16pt "MS Shell Dlg 2";

                                background-color: rgb(63, 73, 39);
                                border-radius:30px""")
                self.formatar_resposta()

                # mensagem da pontuação
                msg1 = QMessageBox()
                msg1.setIcon(QMessageBox.Information)
                msg1.setWindowTitle("pontuação")
                msg1.setText(f"acertos:{self.acertos}\nerros:{self.erros}")
                msg1.exec_()

                # mensagem do fim do jogo
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Fim de Jogo")
                msg.setText(
                    "Obrigado por jogar, esse jogo deu muito trabalho! \nespero que tenha gostado S2")
                msg.exec_()

                self.formatar_jogo()

                # irá reiniciar a lista das perguntas que foram sendo retiradas
                # após serem passadas na tela de perguntas
                random_perguntas()

        # formatar os botões para tirar os textos das perguntas e alternativas
        self.formatar_resposta()
        self.pergunta.setStyleSheet("""font: 16pt "MS Shell Dlg 2";

        background-color: rgb(63, 73, 39);
    border-radius:30px
    """)

    # formatar os textos das perguntas
    def formatar_texto(self):
        lista = [self.botao_letra_a, self.botao_letra_b, self.botao_letra_c, self.botao_letra_d, self.botao_letra_e]
        for bnt in lista:
            bnt.setText("")

    # função para formatar os botões para tirar os textos das perguntas e alternativas
    def formatar_resposta(self):

        lista = [self.botao_letra_a, self.botao_letra_b, self.botao_letra_c, self.botao_letra_d, self.botao_letra_e]
        for bnt in lista:
            bnt.setStyleSheet("""
                                    QPushButton{

            font: 16pt "MS Shell Dlg 2";

            background-color: rgb(63, 73, 39);
        border-radius:30px;
        }
                                    QPushButton:hover{
        color: rgb(61, 61, 61);
            background-color: rgb(238, 238, 238);
        }

                                    QPushBotton{
        background-color: rgb(208, 0, 0);
            color: rgb(255, 255, 255);
        }""")

    # função para confirmar da escolha do usuario e ver resposta correta/errada
    def pergunta_certa(self, s):
        global aux1
        msg = QMessageBox()
        msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setText("confirma resposta selecionada? ")
        msg.setIcon(QMessageBox.Question)
        resp = msg.exec_()
        resposta_certa = False

        if resp == QMessageBox.Yes:

            # Verifica alternativa por alternativa se a resposta que você escolheu está certa
            # caso estaja vai colocar a opção escolhida em verde e soma 1 ponto na pontuação de acertos
            if s == '1' and self.resposta_correta == self.botao_letra_a.text():
                resposta_certa = True
                self.botao_letra_a.setStyleSheet(u"""
                                                        background-color: rgb(79, 238, 0);
                                                        border-radius: 15px;
                                                        border: 2px solid white;
                                                        color: rgb(255, 255, 255);
                                                        """)
                msg = QMessageBox()
                msg.setWindowTitle("Resposta correta!")
                msg.setText("resposta certa! ")
                try:
                    msg.setText(aux1[8])
                except Exception as e:
                    pass
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.acertos += 1
            elif s == '2' and self.resposta_correta == self.botao_letra_b.text():
                resposta_certa = True
                self.botao_letra_b.setStyleSheet(u"""
                                                        background-color: rgb(79, 238, 0);
                                                        border-radius: 15px;
                                                        border: 2px solid white;
                                                        color: rgb(255, 255, 255);
                                                        """)
                msg = QMessageBox()
                msg.setWindowTitle("Resposta correta!")
                msg.setText("resposta certa! ")
                try:
                    msg.setText(aux1[8])
                except Exception as e:
                    pass
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.acertos += 1
            elif s == '3' and self.resposta_correta == self.botao_letra_c.text():
                resposta_certa = True
                self.botao_letra_c.setStyleSheet(u"""
                                                        background-color: rgb(79, 238, 0);
                                                        border-radius: 15px;
                                                        border: 2px solid white;
                                                        color: rgb(255, 255, 255);
                                                        """)
                msg = QMessageBox()
                msg.setWindowTitle("Resposta correta!")
                msg.setText("resposta certa! ")
                try:
                    msg.setText(aux1[8])
                except Exception as e:
                    pass
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.acertos += 1
            elif s == '4' and self.resposta_correta == self.botao_letra_d.text():
                resposta_certa = True
                self.botao_letra_d.setStyleSheet(u"""
                                                        background-color: rgb(79, 238, 0);
                                                        border-radius: 15px;
                                                        border: 2px solid white;
                                                        color: rgb(255, 255, 255);
                                                        """)
                msg = QMessageBox()
                msg.setWindowTitle("Resposta correta!")
                msg.setText("resposta certa! ")
                try:
                    msg.setText(aux1[8])
                except Exception as e:
                    pass
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.acertos += 1
            elif s == '5' and self.resposta_correta == self.botao_letra_e.text():
                resposta_certa = True
                self.botao_letra_e.setStyleSheet(u"""
                                                        background-color: rgb(79, 238, 0);
                                                        border-radius: 15px;
                                                        border: 2px solid white;
                                                        color: rgb(255, 255, 255);
                                                        """)
                msg = QMessageBox()
                msg.setWindowTitle("Resposta correta!")
                msg.setText("resposta certa! ")
                try:
                    msg.setText(aux1[8])
                except Exception as e:
                    pass
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.acertos += 1

            # Caso a resposta esteja errada, irá deixá-la em vermelho e colocará em verde a resposta certa
            # E vai somar 1 ponto na pontuação de erros
            else:

                # mostrando a resposta certa
                if self.resposta_correta == self.botao_letra_a.text():
                    self.botao_letra_a.setStyleSheet(u"""
                                                                            background-color: rgb(79, 238, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif self.resposta_correta == self.botao_letra_b.text():
                    self.botao_letra_b.setStyleSheet(u"""
                                                                            background-color: rgb(79, 238, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif self.resposta_correta == self.botao_letra_c.text():
                    self.botao_letra_c.setStyleSheet(u"""
                                                                            background-color: rgb(79, 238, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif self.resposta_correta == self.botao_letra_d.text():
                    self.botao_letra_d.setStyleSheet(u"""
                                                                            background-color: rgb(79, 238, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif self.resposta_correta == self.botao_letra_e.text():
                    self.botao_letra_e.setStyleSheet(u"""
                                                                            background-color: rgb(79, 238, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)

                # mostrando a resposta errada
                if s == '1':
                    self.botao_letra_a.setStyleSheet(u"""
                                                                            background-color: rgb(255, 0, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif s == '2':
                    self.botao_letra_b.setStyleSheet(u"""
                                                                            background-color: rgb(255, 0, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif s == '3':
                    self.botao_letra_c.setStyleSheet(u"""
                                                                            background-color: rgb(255, 0, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif s == '4':
                    self.botao_letra_d.setStyleSheet(u"""
                                                                            background-color: rgb(255, 0, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)
                elif s == '5':
                    self.botao_letra_e.setStyleSheet(u"""
                                                                            background-color: rgb(255, 0, 0);
                                                                            border-radius: 15px;
                                                                            border: 2px solid white;
                                                                            color: rgb(255, 255, 255);
                                                                            """)

                # mensagem de error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Resposta Errada!")
                msg.exec_()

                self.erros += 1
                self.formatar_resposta()
                self.jogo()

            self.jogo()

    # função para passar da tela de carregamento para tela de login
    def passar(self):
        self.stackedWidget.setCurrentWidget(self.pagina_login)

    # função para cadastrar o usuário
    def cadastrar(self):
        # recebe o nome e a senha
        nome = self.colocar_usuario_cadastro.text()
        senha = self.colocar_senha_cadastro.text()

        # junta as informações
        i = nome + "#" + senha + "#"

        # separa as informações por #
        ie = i.split("#")

        encotrei = False

        # abre o banco de dados com as informações dos usuários
        with open("../Projeto_programação_completo/usuarios_jogo.txt", "r") as aux:
            auxiliar = aux.readlines()

        # irá ver se o usuário já está cadastrado
        if auxiliar:
            for e in auxiliar:
                usu = e.split("#")
                if usu[0] == ie[0]:
                    encotrei = True
                    break

            # caso já esteja fala que já está cadastrado
            if encotrei:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("OPA")
                msg.setText("Usuario já cadastrado no banco de dados!")
                msg.exec_()
                self.colocar_usuario_cadastro.setText("")
                self.colocar_senha_cadastro.setText("")

            # caso não esteja, cadastra o usuário
            else:
                with open("../Projeto_programação_completo/usuarios_jogo.txt", "a") as arquivo:
                    arquivo.write("\n")
                    arquivo.write(i)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("SUCESSO!")
                msg.setText("Usuario cadrastrado no banco de dados!")
                msg.exec_()
                self.colocar_usuario_cadastro.setText("")
                self.colocar_senha_cadastro.setText("")

    # função para fazer o login do usuário
    def entrar(self):

        # recebe nome e senha
        nome = self.colocar_usuario_login.text()
        senha = self.colocar_senha_login.text()

        encotrei = False

        # abre o banco de dados
        with open("../Projeto_programação_completo/usuarios_jogo.txt", "r") as aux:
            auxiliar = aux.readlines()

        # pesquisa no banco de dados e verifica se os dados recebidos estão corretos
        if auxiliar:
            for e in auxiliar:
                usu = e.split("#")
                if usu[0] == nome and usu[1] == senha:
                    encotrei = True
                    break

            # caso esteja, bem-vindo ao Quiz
            if encotrei:
                msg = QMessageBox()
                msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Seja bem-vindo ao Quiz")
                msg.exec_()
                self.colocar_usuario_login.setText("")
                self.colocar_senha_login.setText("")
                self.stackedWidget.setCurrentWidget(self.pagina_inicial)

            # caso não, fala que usuário ou senha estão incorretos
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error")
                msg.setText("Usuário ou senha incorretos!")
                msg.exec_()

    # função para sair do jogo e ir para a tela de login
    def sair(self):

        # abre uma QMessageBox para o usuário confimar
        msg = QMessageBox()
        msg.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Deseja sair do jogo?")
        resp = msg.exec_()

        if resp == QMessageBox.Yes:
            self.stackedWidget.setCurrentWidget(self.pagina_login)

    def tela_jogo(self, s):
        if s == '1':
            self.dificuldade = "facil"
        elif s == '2':
            self.dificuldade = "medio"
        elif s == '3':
            self.dificuldade = "dificil"

        self.stackedWidget.setCurrentWidget(self.pagina_perguntas)

    def setupUi(self, Interface_jogo):

        Interface_jogo.setObjectName("Interface_jogo")
        Interface_jogo.resize(655, 545)
        self.centralwidget = QtWidgets.QWidget(Interface_jogo)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 660, 557))
        self.stackedWidget.setMinimumSize(QtCore.QSize(120, 0))
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet("background-color: rgb(183, 157, 124);")
        self.stackedWidget.setObjectName("stackedWidget")

        # página de carregamento
        self.pagina_carregamento = QtWidgets.QWidget()
        self.pagina_carregamento.setObjectName("pagina_carregamento")
        self.barra_de_progresso = QtWidgets.QProgressBar(self.pagina_carregamento)
        self.barra_de_progresso.setGeometry(QtCore.QRect(170, 320, 361, 41))
        self.barra_de_progresso.setProperty("value", 0)
        self.barra_de_progresso.setObjectName("barra_de_progresso")
        self.label_6 = QtWidgets.QLabel(self.pagina_carregamento)
        self.label_6.setGeometry(QtCore.QRect(290, 400, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.pagina_carregamento)
        self.label.setGeometry(QtCore.QRect(130, 20, 441, 361))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Documento de Gaby.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.barra_de_progresso.raise_()
        self.label_6.raise_()

        # adiciona a página de login
        self.stackedWidget.addWidget(self.pagina_carregamento)
        self.pagina_login = QtWidgets.QWidget()


        # página de login
        self.pagina_login.setObjectName("pagina_login")
        self.label_7 = QtWidgets.QLabel(self.pagina_login)
        self.label_7.setGeometry(QtCore.QRect(220, 30, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(63, 73, 39);")
        self.label_7.setObjectName("label_7")
        self.colocar_usuario_login = QtWidgets.QLineEdit(self.pagina_login)
        self.colocar_usuario_login.setGeometry(QtCore.QRect(290, 210, 171, 31))
        self.colocar_usuario_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colocar_usuario_login.setObjectName("colocar_usuario_login")
        self.label_8 = QtWidgets.QLabel(self.pagina_login)
        self.label_8.setGeometry(QtCore.QRect(180, 200, 121, 41))
        self.label_8.setObjectName("label_8")
        self.colocar_senha_login = QtWidgets.QLineEdit(self.pagina_login)
        self.colocar_senha_login.setGeometry(QtCore.QRect(290, 280, 171, 31))
        self.colocar_senha_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colocar_senha_login.setObjectName("colocar_senha_login")
        self.label_9 = QtWidgets.QLabel(self.pagina_login)
        self.label_9.setGeometry(QtCore.QRect(190, 270, 121, 41))
        self.label_9.setObjectName("label_9")
        self.botao_entrar = QtWidgets.QPushButton(self.pagina_login)
        self.botao_entrar.setGeometry(QtCore.QRect(80, 430, 121, 41))
        self.botao_entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_entrar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("3005767_account_door_enter_login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_entrar.setIcon(icon)
        self.botao_entrar.setIconSize(QtCore.QSize(25, 25))
        self.botao_entrar.setObjectName("botao_entrar")
        self.botao_sair_login = QtWidgets.QPushButton(self.pagina_login)
        self.botao_sair_login.setGeometry(QtCore.QRect(460, 430, 121, 41))
        self.botao_sair_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair_login.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("3994382_access_close_exit_logout_sign out_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_sair_login.setIcon(icon1)
        self.botao_sair_login.setIconSize(QtCore.QSize(25, 25))
        self.botao_sair_login.setObjectName("botao_sair_login")
        self.botao_ir_cadastrar = QtWidgets.QPushButton(self.pagina_login)
        self.botao_ir_cadastrar.setGeometry(QtCore.QRect(270, 430, 121, 41))
        self.botao_ir_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_ir_cadastrar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_ir_cadastrar.setObjectName("botao_ir_cadastrar")
        self.label_14 = QtWidgets.QLabel(self.pagina_login)
        self.label_14.setGeometry(QtCore.QRect(420, 150, 281, 241))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Documento de Gaby.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.pagina_login)
        self.label_16.setGeometry(QtCore.QRect(400, 430, 51, 41))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("pc seta.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.pagina_login)
        self.label_17.setGeometry(QtCore.QRect(210, 430, 51, 41))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("pc seta.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.botao_ver_senha_login = QtWidgets.QPushButton(self.pagina_login)
        self.botao_ver_senha_login.setGeometry(QtCore.QRect(430, 280, 31, 31))
        self.botao_ver_senha_login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botao_ver_senha_login.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("contrasenha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_ver_senha_login.setIcon(icon2)
        self.botao_ver_senha_login.setFlat(True)
        self.botao_ver_senha_login.setObjectName("botao_ver_senha_login")
        self.label_14.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_7.raise_()
        self.colocar_usuario_login.raise_()
        self.colocar_senha_login.raise_()
        self.botao_entrar.raise_()
        self.botao_sair_login.raise_()
        self.botao_ir_cadastrar.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.botao_ver_senha_login.raise_()

        # adiciona a página de cadastrar
        self.stackedWidget.addWidget(self.pagina_login)
        self.pagina_cadastrar = QtWidgets.QWidget()

        # página de cadastrar
        self.pagina_cadastrar.setObjectName("pagina_cadastrar")
        self.label_10 = QtWidgets.QLabel(self.pagina_cadastrar)
        self.label_10.setGeometry(QtCore.QRect(160, 30, 321, 131))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(63, 73, 39);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.pagina_cadastrar)
        self.label_11.setGeometry(QtCore.QRect(160, 220, 121, 41))
        self.label_11.setObjectName("label_11")
        self.colocar_usuario_cadastro = QtWidgets.QLineEdit(self.pagina_cadastrar)
        self.colocar_usuario_cadastro.setGeometry(QtCore.QRect(320, 230, 171, 31))
        self.colocar_usuario_cadastro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colocar_usuario_cadastro.setObjectName("colocar_usuario_cadastro")
        self.colocar_senha_cadastro = QtWidgets.QLineEdit(self.pagina_cadastrar)
        self.colocar_senha_cadastro.setGeometry(QtCore.QRect(320, 310, 171, 31))
        self.colocar_senha_cadastro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colocar_senha_cadastro.setObjectName("colocar_senha_cadastro")
        self.label_12 = QtWidgets.QLabel(self.pagina_cadastrar)
        self.label_12.setGeometry(QtCore.QRect(170, 300, 121, 41))
        self.label_12.setObjectName("label_12")
        self.botao_cadastrar_cadastrar = QtWidgets.QPushButton(self.pagina_cadastrar)
        self.botao_cadastrar_cadastrar.setGeometry(QtCore.QRect(130, 460, 121, 41))
        self.botao_cadastrar_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_cadastrar_cadastrar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_cadastrar_cadastrar.setObjectName("botao_cadastrar_cadastrar")
        self.botao_voltar_cadastro = QtWidgets.QPushButton(self.pagina_cadastrar)
        self.botao_voltar_cadastro.setGeometry(QtCore.QRect(410, 460, 121, 41))
        self.botao_voltar_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar_cadastro.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("216437_back_arrow_icon (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar_cadastro.setIcon(icon3)
        self.botao_voltar_cadastro.setIconSize(QtCore.QSize(25, 25))
        self.botao_voltar_cadastro.setObjectName("botao_voltar_cadastro")
        self.label_18 = QtWidgets.QLabel(self.pagina_cadastrar)
        self.label_18.setGeometry(QtCore.QRect(300, 450, 61, 51))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("pc seta.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.botao_ver_senha_cadastrar = QtWidgets.QPushButton(self.pagina_cadastrar)
        self.botao_ver_senha_cadastrar.setGeometry(QtCore.QRect(460, 310, 31, 31))
        self.botao_ver_senha_cadastrar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.botao_ver_senha_cadastrar.setText("")
        self.botao_ver_senha_cadastrar.setIcon(icon2)
        self.botao_ver_senha_cadastrar.setFlat(True)
        self.botao_ver_senha_cadastrar.setObjectName("botao_ver_senha_cadastrar")

        # adiciona a página inicial
        self.stackedWidget.addWidget(self.pagina_cadastrar)
        self.pagina_inicial = QtWidgets.QWidget()

        # página inicial
        self.pagina_inicial.setObjectName("pagina_inicial")
        self.botao_sair = QtWidgets.QPushButton(self.pagina_inicial)
        self.botao_sair.setGeometry(QtCore.QRect(225, 380, 201, 71))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("QPushButton{\n"
"font: italic 22pt \"Sans Serif\";\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_sair.setIcon(icon1)
        self.botao_sair.setIconSize(QtCore.QSize(25, 25))
        self.botao_sair.setObjectName("botao_sair")
        self.botao_sobre = QtWidgets.QPushButton(self.pagina_inicial)
        self.botao_sobre.setGeometry(QtCore.QRect(225, 270, 201, 71))
        self.botao_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sobre.setStyleSheet("QPushButton{\n"
"font: italic 22pt \"Sans Serif\";\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("103515_text_document_information_icon (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_sobre.setIcon(icon4)
        self.botao_sobre.setIconSize(QtCore.QSize(25, 25))
        self.botao_sobre.setObjectName("botao_sobre")
        self.botao_iniciar_jogo = QtWidgets.QPushButton(self.pagina_inicial)
        self.botao_iniciar_jogo.setGeometry(QtCore.QRect(225, 160, 201, 71))
        self.botao_iniciar_jogo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_iniciar_jogo.setStyleSheet("QPushButton{\n"
"font: italic 22pt \"Sans Serif\";\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("211668_controller_b_game_icon (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_iniciar_jogo.setIcon(icon5)
        self.botao_iniciar_jogo.setIconSize(QtCore.QSize(25, 25))
        self.botao_iniciar_jogo.setObjectName("botao_iniciar_jogo")
        self.label_5 = QtWidgets.QLabel(self.pagina_inicial)
        self.label_5.setGeometry(QtCore.QRect(245, 40, 171, 51))
        self.label_5.setMouseTracking(False)
        self.label_5.setStyleSheet("font: 22pt \"Broadway\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(63, 73, 39);\n"
"selection-color: rgb(170, 85, 255);\n"
"font: 45pt \"Broadway\";")
        self.label_5.setObjectName("label_5")

        # adiciona a página do sobre
        self.stackedWidget.addWidget(self.pagina_inicial)
        self.pagina_sobre = QtWidgets.QWidget()

        # página sobre
        self.pagina_sobre.setObjectName("pagina_sobre")
        self.sobre = QtWidgets.QTextBrowser(self.pagina_sobre)
        self.sobre.setGeometry(QtCore.QRect(80, 210, 501, 261))
        self.sobre.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sobre.setStyleSheet("background-color: rgb(214, 200, 171);")
        self.sobre.setObjectName("sobre")
        self.botao_voltar = QtWidgets.QPushButton(self.pagina_sobre)
        self.botao_voltar.setGeometry(QtCore.QRect(20, 490, 101, 31))
        self.botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setAcceptDrops(False)
        self.botao_voltar.setStatusTip("")
        self.botao_voltar.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_voltar.setIcon(icon3)
        self.botao_voltar.setIconSize(QtCore.QSize(25, 25))
        self.botao_voltar.setObjectName("botao_voltar")
        self.label_3 = QtWidgets.QLabel(self.pagina_sobre)
        self.label_3.setGeometry(QtCore.QRect(260, 140, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_13 = QtWidgets.QLabel(self.pagina_sobre)
        self.label_13.setGeometry(QtCore.QRect(190, -30, 301, 281))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Documento de Gaby.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_13.raise_()
        self.label_3.raise_()
        self.sobre.raise_()
        self.botao_voltar.raise_()

        # adiciona a página da dificuldade
        self.stackedWidget.addWidget(self.pagina_sobre)
        self.pagina_dificuldade = QtWidgets.QWidget()

        # página da dificuldade
        self.pagina_dificuldade.setObjectName("pagina_dificuldade")
        self.label_2 = QtWidgets.QLabel(self.pagina_dificuldade)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 311, 41))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.pagina_dificuldade)
        self.label_4.setGeometry(QtCore.QRect(190, 60, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(63, 73, 39);")
        self.label_4.setObjectName("label_4")
        self.botao_facil = QtWidgets.QPushButton(self.pagina_dificuldade)
        self.botao_facil.setGeometry(QtCore.QRect(230, 200, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_facil.setFont(font)
        self.botao_facil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_facil.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("211667_a_controller_game_icon (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_facil.setIcon(icon6)
        self.botao_facil.setIconSize(QtCore.QSize(25, 25))
        self.botao_facil.setObjectName("botao_facil")
        self.botao_medio = QtWidgets.QPushButton(self.pagina_dificuldade)
        self.botao_medio.setGeometry(QtCore.QRect(230, 300, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_medio.setFont(font)
        self.botao_medio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_medio.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_medio.setIcon(icon6)
        self.botao_medio.setIconSize(QtCore.QSize(25, 25))
        self.botao_medio.setObjectName("botao_medio")
        self.botao_dificil = QtWidgets.QPushButton(self.pagina_dificuldade)
        self.botao_dificil.setGeometry(QtCore.QRect(230, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_dificil.setFont(font)
        self.botao_dificil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_dificil.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_dificil.setIcon(icon6)
        self.botao_dificil.setIconSize(QtCore.QSize(25, 25))
        self.botao_dificil.setObjectName("botao_dificil")
        self.botao_voltar_dificuldade = QtWidgets.QPushButton(self.pagina_dificuldade)
        self.botao_voltar_dificuldade.setGeometry(QtCore.QRect(510, 470, 121, 41))
        self.botao_voltar_dificuldade.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar_dificuldade.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_voltar_dificuldade.setIcon(icon3)
        self.botao_voltar_dificuldade.setIconSize(QtCore.QSize(25, 25))
        self.botao_voltar_dificuldade.setObjectName("botao_voltar_dificuldade")

        # adiciona a página das perguntas
        self.stackedWidget.addWidget(self.pagina_dificuldade)
        self.pagina_perguntas = QtWidgets.QWidget()

        # página das perguntas
        self.pagina_perguntas.setObjectName("pagina_perguntas")
        self.botao_letra_a = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_letra_a.setGeometry(QtCore.QRect(90, 170, 441, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_letra_a.setFont(font)
        self.botao_letra_a.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_letra_a.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_letra_a.setObjectName("botao_letra_a")
        self.botao_letra_b = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_letra_b.setGeometry(QtCore.QRect(90, 240, 441, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_letra_b.setFont(font)
        self.botao_letra_b.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_letra_b.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_letra_b.setObjectName("botao_letra_b")
        self.botao_letra_c = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_letra_c.setGeometry(QtCore.QRect(90, 310, 441, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_letra_c.setFont(font)
        self.botao_letra_c.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_letra_c.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_letra_c.setObjectName("botao_letra_c")
        self.botao_letra_d = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_letra_d.setGeometry(QtCore.QRect(90, 380, 441, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_letra_d.setFont(font)
        self.botao_letra_d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_letra_d.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_letra_d.setObjectName("botao_letra_d")
        self.botao_letra_e = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_letra_e.setGeometry(QtCore.QRect(90, 450, 441, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_letra_e.setFont(font)
        self.botao_letra_e.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_letra_e.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: rgb(61, 61, 61);\n"
"    background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.botao_letra_e.setObjectName("botao_letra_e")
        self.botao_voltar_perguntas = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_voltar_perguntas.setGeometry(QtCore.QRect(550, 500, 91, 31))
        self.botao_voltar_perguntas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar_perguntas.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_voltar_perguntas.setIcon(icon3)
        self.botao_voltar_perguntas.setIconSize(QtCore.QSize(22, 22))
        self.botao_voltar_perguntas.setObjectName("botao_voltar_perguntas")
        self.botao_comecar_perguntas = QtWidgets.QPushButton(self.pagina_perguntas)
        self.botao_comecar_perguntas.setGeometry(QtCore.QRect(550, 460, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.botao_comecar_perguntas.setFont(font)
        self.botao_comecar_perguntas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_comecar_perguntas.setStyleSheet("QPushButton{\n"
"    \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(63, 73, 39);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(208, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.botao_comecar_perguntas.setObjectName("botao_comecar_perguntas")
        self.pergunta = QtWidgets.QLabel(self.pagina_perguntas)
        self.pergunta.setGeometry(QtCore.QRect(20, 10, 611, 141))
        self.pergunta.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"    background-color: rgb(63, 73, 39);\n"
"border-radius:30px")
        self.pergunta.setAlignment(QtCore.Qt.AlignCenter)
        self.pergunta.setWordWrap(True)
        self.pergunta.setObjectName("pergunta")
        self.stackedWidget.addWidget(self.pagina_perguntas)
        Interface_jogo.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interface_jogo)
        self.stackedWidget.setCurrentIndex(0)
        self.botao_sair_login.clicked.connect(Interface_jogo.close) # type: ignore

        QtCore.QMetaObject.connectSlotsByName(Interface_jogo)

        # função especial para tirar os botões maximizar,minimizar e sair
        Interface_jogo.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        ### configuração dos botões da interface

        # botao cadastro da página de login que vai para a página de cadastro
        self.botao_ir_cadastrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_cadastrar))

        # botao cadastrar da página de cadastro que irá chamar a função
        # que verifica se o usuario já existe e se não, adicioná-lo
        self.botao_cadastrar_cadastrar.clicked.connect(self.cadastrar)

        # botao voltar da página de cadastro para voltar para a página de login
        self.botao_voltar_cadastro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_login))

        # botao entrar da página de login que irá chamar a função
        # que verifica o usuário e senha, para só assim entrar no jogo
        self.botao_entrar.clicked.connect(self.entrar)

        # botao sobre da página inicial para ir para a página sobre
        self.botao_sobre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_sobre))

        # botao voltar da página sobre para voltar para a página inicial
        self.botao_voltar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_inicial))

        # botao iniciar jogo da página inicial para ir para a página de escolher a dificuldade
        self.botao_iniciar_jogo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_dificuldade))

        # botao sair da página inicial para voltar para a página de login
        self.botao_sair.clicked.connect(self.sair)

        # botoes da pagina dificuldade para escolher a dificuldade
        # e de acordo com a escolha ele irá iniciar uma opção na função jogo
        self.botao_facil.clicked.connect(lambda: self.tela_jogo('1'))
        self.botao_medio.clicked.connect(lambda: self.tela_jogo('2'))
        self.botao_dificil.clicked.connect(lambda: self.tela_jogo('3'))

        # botao comecar na página das perguntas para iniciar a lista de perguntas
        self.botao_comecar_perguntas.clicked.connect(self.jogo)

        # botoes da página de perguntas para definir a alternativa correta
        self.botao_letra_a.clicked.connect(lambda: self.pergunta_certa("1"))
        self.botao_letra_b.clicked.connect(lambda: self.pergunta_certa("2"))
        self.botao_letra_c.clicked.connect(lambda: self.pergunta_certa("3"))
        self.botao_letra_d.clicked.connect(lambda: self.pergunta_certa("4"))
        self.botao_letra_e.clicked.connect(lambda: self.pergunta_certa("5"))

        # botao voltar na página da dificuldade para voltar para a página inicial
        self.botao_voltar_dificuldade.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_inicial))

        # botao voltar na página das perguntas para voltar para a página inicial
        self.botao_voltar_perguntas.clicked.connect(self.voltar_jogo)

        # botao na página login para chamar a funcao de deixar a senha visível ou não
        self.botao_ver_senha_login.clicked.connect(self.ver_senha_login)

        # botao na página cadastrar para chamar a funcao de deixar a senha visível ou não
        self.botao_ver_senha_cadastrar.clicked.connect(self.ver_senha_cadastrar)

    def retranslateUi(self, Interface_jogo):
        _translate = QtCore.QCoreApplication.translate
        Interface_jogo.setWindowTitle(_translate("Interface_jogo", "MainWindow"))
        self.label_6.setText(_translate("Interface_jogo", "Carregando..."))
        self.label_7.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Login</span></p></body></html>"))
        self.label_8.setText(_translate("Interface_jogo", "<html><head/><body><p><span style=\" font-size:18pt;\">Usuário:</span></p></body></html>"))
        self.label_9.setText(_translate("Interface_jogo", "<html><head/><body><p><span style=\" font-size:18pt;\">Senha:</span></p></body></html>"))
        self.botao_entrar.setText(_translate("Interface_jogo", "Entrar"))
        self.botao_sair_login.setText(_translate("Interface_jogo", "Sair"))
        self.botao_ir_cadastrar.setText(_translate("Interface_jogo", "Cadastrar"))
        self.label_10.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Cadastrar</span></p></body></html>"))
        self.label_11.setText(_translate("Interface_jogo", "<html><head/><body><p><span style=\" font-size:18pt;\">Usuário:</span></p></body></html>"))
        self.label_12.setText(_translate("Interface_jogo", "<html><head/><body><p><span style=\" font-size:18pt;\">Senha:</span></p></body></html>"))
        self.botao_cadastrar_cadastrar.setText(_translate("Interface_jogo", "Cadastrar"))
        self.botao_voltar_cadastro.setText(_translate("Interface_jogo", "Voltar"))
        self.botao_sair.setText(_translate("Interface_jogo", "Sair"))
        self.botao_sobre.setText(_translate("Interface_jogo", "Sobre"))
        self.botao_iniciar_jogo.setText(_translate("Interface_jogo", "Iniciar Jogo"))
        self.label_5.setText(_translate("Interface_jogo", "Quiz "))
        self.sobre.setHtml(_translate("Interface_jogo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Programa criado pelos alunos do 2° ano de informática de 2022.2 no ano de 2023</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#2f361e;\">Criado por:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#2f361e;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ana Clara Da Silva Sales (clara.sales@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ana Gabrielly Da Silva Freitas (ana.gabrielly@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ana Maria Dos Santos Dantas (dantas.ana1@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ananda Emily Da Silva Gurgel (ananda.gurgel@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Isaac Alef Barros Da Silva (isaac.barros@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">João Lourenço de Azevedo Neto (joao.lourenco@escolar.ifrn.edu.br)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Foi criado com o intuito de gerar um quiz sobre conhecimentos gerais.</span></p></body></html>"))
        self.botao_voltar.setText(_translate("Interface_jogo", "Voltar"))
        self.label_3.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\">Sobre o projeto </p></body></html>"))
        self.label_2.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\">-------------------------------------------------------------------------</p></body></html>"))
        self.label_4.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\">Dificuldade</p></body></html>"))
        self.botao_facil.setText(_translate("Interface_jogo", "Fácil"))
        self.botao_medio.setText(_translate("Interface_jogo", "Médio"))
        self.botao_dificil.setText(_translate("Interface_jogo", "Díficil"))
        self.botao_voltar_dificuldade.setText(_translate("Interface_jogo", "Voltar"))
        self.botao_letra_a.setText(_translate("Interface_jogo", " A"))
        self.botao_letra_b.setText(_translate("Interface_jogo", "B"))
        self.botao_letra_c.setText(_translate("Interface_jogo", "C"))
        self.botao_letra_d.setText(_translate("Interface_jogo", "D"))
        self.botao_letra_e.setText(_translate("Interface_jogo", "E"))
        self.botao_voltar_perguntas.setText(_translate("Interface_jogo", "Voltar"))
        self.botao_comecar_perguntas.setText(_translate("Interface_jogo", "Começar"))
        self.pergunta.setText(_translate("Interface_jogo", "<html><head/><body><p align=\"center\">Pergunta: </p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Interface_jogo = QtWidgets.QMainWindow()
    ui = Ui_Interface_jogo()
    ui.setupUi(Interface_jogo)
    Interface_jogo.show()

    # trocando as letras e numeros pelos asteriscos nos lineedit do login e cadastro
    ui.colocar_senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.colocar_senha_cadastro.setEchoMode(QtWidgets.QLineEdit.Password)

    # para ir mudando os números na QprogressBar
    for i in range(101):
        ui.barra_de_progresso.setValue(i)
        time.sleep(0.02)
        app.processEvents()  # para ir atualizando a página a cada mudança de número

    # passar para a tela de login depois que terminar o carregamento
    ui.passar()

    sys.exit(app.exec_())