def criar_o_email(numemais):
    
    with open("credentials.txt", "r") as arquivo:
        numli=arquivo.read()
        numli=numli.split("\n")

    senha=numli[0]
    
    letras_minusculas = tuple(chr(i) for i in range(97, 123))
    letras_maiusculas = tuple(chr(i) for i in range(65, 91))

    caracteres = letras_maiusculas+letras_minusculas

    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    import random
    import pyautogui
    mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    for i in range (0,numemais):

        yahoo=""
        for i in range(0,12):    
            yahoo=yahoo+random.choice(caracteres)
        yahoo=yahoo+"@sharklasers.com"

        

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome()

        #baixando o benedito do VPN :(
        
        driver.get('https://chromewebstore.google.com/detail/browsec-vpn-free-vpn-for/omghfjlpggmjjaagoclmmobgdodcjboh')
        time.sleep(0.5)
        pyautogui.moveTo(1025,320)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(590,240)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.moveTo(900,60)
        time.sleep(4)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.keyDown("Tab")
        time.sleep(0.1)
        pyautogui.keyDown("Tab")
        time.sleep(0.1)
        pyautogui.keyDown("Enter")
        time.sleep(0.1)
        pyautogui.moveTo(720,430)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(720,365)
        time.sleep(0.5)
        pyautogui.click()

        time.sleep(0.5)
        pyautogui.keyDown("Esc")
        time.sleep(0.5)

        print(f"User: {yahoo} | Passord {senha} | Progresso: {round((i+1)*100/numemais, 2)}% & {i+1}/{numemais} | ProgressoConta: 1/4 | Estado: Estage 1")


        driver.get('https://www.guerrillamail.com') 
        time.sleep(1)
        pyautogui.moveTo(332, 500)  
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(410,500)
        pyautogui.write(yahoo)
        time.sleep(0.5)
        pyautogui.click()
        
        guerrilha=""
        for i in range(0,12):    
            guerrilha=guerrilha+random.choice(caracteres)

        with open("logins.txt", "r") as arquivo:
            complicado=arquivo.read()
            complicado=complicado.split("\n")

        if len(complicado)-1 > 250:
            with open("login2.txt", "a") as arquivo:
                arquivo.write(guerrilha+"\n")

        else:
            with open("logins.txt", "a") as arquivo:
                arquivo.write(guerrilha+"\n")

        print(f"User: {yahoo} | Passord {senha} | Progresso: {round((i+1)*100/numemais, 2)}% & {i+1}/{numemais} | ProgressoConta: 2/4 | Estado: Estage 2")

        #colocar em um proxy ou um vpn
        driver.get('https://www.pokerstars.com/signup/')


        a1 = driver.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
        a1.click()
        time.sleep(0.5)
        colema = driver.find_element(by='xpath', value='//*[@id="email"]')
        colema.send_keys(yahoo)
        a3 = driver.find_element(by='xpath', value='//*[@id="userId"]')
        a3.send_keys(guerrilha)
        colsen = driver.find_element(by='xpath', value='//*[@id="password"]')
        colsen.send_keys(senha)
        time.sleep(0.5)     

        pyautogui.keyDown("Tab")
        time.sleep(2)
        pyautogui.click()
        time.sleep(1)
        conf1=driver.find_element(by='xpath', value='//*[@class="_0d9eedb"]')
        conf1.click()
        time.sleep(0.5)
        conf2=driver.find_element(by='xpath', value='//*[@class="_f92fbce _cb4cb62 _18f4de1 _f7a0730"]')
        conf2.click()

        time.sleep(5)
        print(f"User: {yahoo} | Passord {senha} | Progresso: {round((i+1)*100/numemais, 2)}% & {i+1}/{numemais} | ProgressoConta: 3/4 | Estado: Estage 3")

        #guerrilha=nome.user
        #guerrilha_senha=senha.user
        #yahoo=email.user


        driver.get("https://www.pokerstars.com/homegames/invite/?args=eyJ0eXBlIjoiSk9JTl9DTFVCIiwiY2x1YklkIjo0OTA2MjU2LCJpbnZpdGF0aW9uQ29kZSI6ImF0Z2UyNTI5In0%3D")
        time.sleep(4)
        
        club1=driver.find_element(by="xpath", value='//*[@id="yourName"]')
        club1.send_keys(guerrilha)
        time.sleep(0.5)
        club1=driver.find_element(by="xpath", value='//*[@id="joinClubSubmit"]')
        club1.click()
        time.sleep(1)
        driver.quit()
        print(f"\033[32mUser: {yahoo} | Passord {senha} | Progresso: {round((i+1)*100/numemais, 2)}% & {i+1}/{numemais} | ProgressoConta: 4/4 | Estado: Completo\033[33m")
        print("")
        print("=-"*30)
        print("")
