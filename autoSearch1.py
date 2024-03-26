import credentials1
import emuSearch1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string

browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver\chromedriver.exe')
browser.get('https://www.pokerstars.com/account/prhub')
time.sleep(0.5)
next = browser.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
next.click()
time.sleep(1)

email = browser.find_element(by='xpath', value='//*[@id="userld._99b383d"]')
email.send_keys(credentials1.username)
time.sleep(1)
nextpass = browser.find_element(by='xpath', value='//*[@id="password._99b383d"]')
nextpass.send_keys(credentials1.password)
time.sleep(0.5)



time.sleep(1)


signin = browser.find_element(by='xpath', value='//*[@id="_38fea9f"]')
signin.click()
time.sleep(0.5)
confsignin = browser.find_element(by='xpath', value='//*[@id="idSIButton9"]')
confsignin.click()

time.sleep(5)

browser.get('https://www.bing.com/')
time.sleep(0.5)
for x in range(35):
    randa = random.choice(string.ascii_letters)
    randb = random.choice(string.ascii_letters)
    randc = random.choice(string.ascii_letters)
    rand = str(f'{randa}{randb}{randc}')

    search = browser.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    search.clear()
    search.send_keys(rand)
    time.sleep(0.5)
    enter = browser.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    enter.submit()
    time.sleep(0.5)



emuSearch1()