
def resgatar15():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys


    with open("credentials.txt", "r") as arquivo:
        numli=arquivo.read()
        numli=numli.split("\n")

    senha=numli[0]

    with open("logins.txt", "r") as arquivo:
        nbglla=arquivo.read()
        nbglla=nbglla.split("\n")

    for user in nbglla:
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.pokerstars.com/login/")
        time.sleep(2)
        next = driver.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
        next.click()
        time.sleep(0.2)

        email = driver.find_element(by='xpath', value='//*[@id="userId"]')
        email.send_keys(user)
        #iosenh
        time.sleep(0.1)


        nextpass = driver.find_element(by='xpath', value='//*[@id="password"]')
        nextpass.send_keys(senha)
        time.sleep(0.1)
        signin = driver.find_element(by='xpath', value='//*[@class="_f92fbce _cb4cb62 _18f4de1 _f7a0730"]')
        signin.click()
        time.sleep(1)
        print(f"User: {user} | Passord: {senha} | Progresso: {nbglla.index(user)+1*100/len(nbglla)}% &{nbglla.index(user)+1}/{len(nbglla)} | ProgressoConta: 1/2 | Estado: Estage 1")

        driver.get('https://cashier.pokerstars.com/cashier/?language=en&country=BR&site=1&platform=Web&timezone=1&applePaySupported=false&brand=PokerStars&TimeZoneId=1&u=BSVAXI&hermesappkey=3f85e4c7-6d13-4d37-9f53-00f01da87bff#/play-money')
        time.sleep(3)
        mudfic = driver.find_element(by="xpath", value='//*[@class="btn btn-default collect"]')
        mudfic.click()
        time.sleep(0.5)
        driver.quit()
        print(f"\033[32mUser: {user} | Passord: {senha} | Progresso: {nbglla.index(user)+1*100/len(nbglla)}% &{nbglla.index(user)+1}/{len(nbglla)} | ProgressoConta: 2/2 | Estado: Completo\033[33m")
        print("=-"*30)