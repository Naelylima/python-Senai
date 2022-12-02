import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit


class Janela(QMainWindow): #Herança
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 300
        self.altura = 300
        self.titulo = " Primeira Janela "

        self.end_email = QLineEdit(self)
        self.end_email.move(80, 50)  # posição dentro da janela (distancia da esquerda - distancia do topo)
        self.end_email.resize(150, 25)  # (altura - largura do botão)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(80, 130)  # posição dentro da janela (distancia da esquerda - distancia do topo)
        self.caixa_texto.resize(150, 25)# (altura - largura do botão)

        self.label1 = QLabel(self)
        self.label1.setText("Digite o email do destinatario: ")
        self.label1.move(60, 10)
        self.label1.setStyleSheet('QLabel {font:bold;font-size:13px;color:"white"}')
        self.label1.resize(300, 50)

        self.label2 = QLabel(self)
        self.label2.setText("Digite sua mensagem: ")
        self.label2.move(60, 90)
        self.label2.setStyleSheet('QLabel {font:bold;font-size:13px;color:"white"}')
        self.label2.resize(300, 50)

        botao1 = QPushButton('Ligar', self)
        botao1.move(80, 200)  # posição dentro da janela (distancia da esquerda - distancia do topo)
        botao1.resize(150, 50)  # (altura - largura do botão)
        botao1.setStyleSheet('QPushButton {background-color:#46C0DC;font:bold;font-size:10px}')  # PARA ESTILIZAR
        botao1.clicked.connect(self.principal)



    def setar_tamanhos(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)


    def principal(self):
        j.close()
        mensagem = self.caixa_texto.text()
        destinatario = self.end_email.text()
        print(mensagem, destinatario)

        opcoes_chrome = Options()
        opcoes_chrome.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=opcoes_chrome)

        driver.get("https://github.com/Naelylima")
        sleep(0.2)
        driver.maximize_window()
        sleep(1)
        imagem_printada = driver.find_element('xpath', '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div['
                                                       '1]/div[1]/a/img')
        sleep(0.2)
        imagem_printada.screenshot('foto.png')
        driver.close()
        sleep(1)
        pyautogui.press('winleft')
        sleep(1)
        pyautogui.write('google chrome')
        # sleep(0.2)
        pyautogui.press('enter')
        sleep(3)
        pyautogui.write('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox') #link da pagina do gmail aberta (trocar se necessario)
        sleep(0.5)
        pyautogui.press('enter')
        sleep(2)

        while True:
            try:
                if pyautogui.locateOnScreen('botaoescreverdogmail.png'):
                    pyautogui.moveTo('botaoescreverdogmail.png')
                    pyautogui.click()
                    sleep(2)
                    pyautogui.write(destinatario)
                    sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    sleep(0.5)
                    pyautogui.write('IMAGEM SELECIONADA!')
                    sleep(1)
                    pyautogui.press('tab')
                    sleep(0.5)
                    pyautogui.write(mensagem)
                    sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    sleep(1.5)
                    pyautogui.write(os.getcwd() + "\\foto.png")
                    pyautogui.press('enter')
                    sleep(1)
                    pyautogui.press('tab')
                    pyautogui.press('enter')
                    break

            except Exception:
                continue

stylesheet = """
                Janela {
                    background-image: url("fundo.jpg");
                    background-repeat: no-repeat; 
                    background-position: center;
                    background-color: white
                    }
                """

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    aplicacao.setStyleSheet(stylesheet)
    j = Janela()
    j.show()
    j.setar_tamanhos()
    sys.exit(aplicacao.exec())
