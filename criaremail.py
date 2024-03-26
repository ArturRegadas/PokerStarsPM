
with open("nomes.txt", "r") as arquivo:
    nome=arquivo.read()
    nome=nome.split("\n")

with open("sobrenomes.txt", "r") as arquivo:
    sobrenome=arquivo.read()
    sobrenome=sobrenome.split("\n")

letras_minusculas = tuple(chr(i) for i in range(97, 123))
letras_maiusculas = tuple(chr(i) for i in range(65, 91))

caracteres = letras_maiusculas+letras_minusculas

import credentials1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string
import pyautogui

yahoo=""
for i in range(0,8):    
    yahoo=yahoo+random.choice(caracteres)

with open("logins.txt", "a") as arquivo:
    arquivo.write(yahoo+"\n")

    
yahoo_senha=""
for i in range(0,8):
    yahoo_senha=yahoo_senha+random.choice(caracteres)
yahoo_senha=yahoo_senha+"21!"
with open("logins.txt", "a") as arquivo:
    arquivo.write(yahoo_senha+"\n")









mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://login.yahoo.com/account/create?.lang=pt-BR&.intl=br&.src=yhelp')

nomeinserido = driver.find_element(by='xpath', value='//*[@id="usernamereg-firstName"]')
nomeinserido.send_keys(random.choice(nome))
pyautogui.keyDown("Tab")
pyautogui.write(random.choice(sobrenome))
time.sleep(1)

email = driver.find_element(by='xpath', value='//*[@id="usernamereg-userId"]')
email.send_keys(yahoo)

pyautogui.keyDown("Tab")
pyautogui.keyDown("Tab")
print(yahoo_senha)
pyautogui.write(yahoo_senha)
time.sleep(1)

mes = driver.find_element(by='xpath', value='//*[@id="usernamereg-month"]')
mes.click()
pyautogui.keyDown("f")
pyautogui.keyDown("Enter")
dia = driver.find_element(by='xpath', value='//*[@id="usernamereg-day"]')
dia.send_keys(random.randint(1,29))

ano = driver.find_element(by='xpath', value='//*[@id="usernamereg-year"]')
ano.send_keys(random.randint(1985,2000))

criar = driver.find_element(by='xpath', value='//*[@id="reg-submit-button"]')
criar.click()

time.sleep(10)
driver.quit()