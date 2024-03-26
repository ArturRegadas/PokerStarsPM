import credentials1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.pokerstars.com/account/prhub')

next = driver.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
next.click()

time.sleep(3)
email = driver.find_element(by='xpath', value='//*[@id="userId"]')
email.send_keys(credentials1.username)

time.sleep(1)


nextpass = driver.find_element(by='xpath', value='//*[@id="password"]')
nextpass.send_keys(credentials1.password)
time.sleep(0.5)
signin = driver.find_element(by='xpath', value='//*[@class="_f92fbce _cb4cb62 _18f4de1 _f7a0730"]')
signin.click()
time.sleep(0.5)


time.sleep(1)

driver.get('https://cashier.pokerstars.com/cashier/?language=en&country=BR&site=1&platform=Web&timezone=1&applePaySupported=false&brand=PokerStars&TimeZoneId=1&u=BSVAXI&hermesappkey=3f85e4c7-6d13-4d37-9f53-00f01da87bff#/play-money')
time.sleep(15)
mudfic = driver.find_element(by="xpath", value='//*[@class="btn btn-default collect"]')
mudfic.click()
time.sleep(1)
driver.quit()