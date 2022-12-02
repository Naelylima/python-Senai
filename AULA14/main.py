import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

print(os.getcwd())

destinatario = input("Digite o destinatário do e-mail: ")
mensgaem = input('Digite sua mensagem: ')

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
pyautogui.write('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
sleep(0.5)
pyautogui.press('enter')
sleep(2)

while True:
    try:
        if pyautogui.locateOnScreen('botaoescreverdogmail.png'): #Seu gmail precisa estar em português para dar certo.
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
            pyautogui.write(mensgaem)
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
