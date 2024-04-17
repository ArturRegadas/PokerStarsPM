def entra_na_torneira1(link_torneio):
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys

    time.sleep(7)

    with open("credentials.txt", "r") as arquivo:
        numli=arquivo.read()
        numli=numli.split("\n")

    senha=numli[0]

    with open("logins.txt", "r") as arquivo:
        bglla=arquivo.read()
        bglla=bglla.split("\n")



    for iosenh in bglla:
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}


        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome()
        
        driver.get("https://www.pokerstars.com/login/")
        time.sleep(3)
        next = driver.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
        next.click()
        time.sleep(0.2)
        
        email = driver.find_element(by='xpath', value='//*[@id="userId"]')
        email.send_keys(iosenh)
        #iosenh
        time.sleep(0.1)


        nextpass = driver.find_element(by='xpath', value='//*[@id="password"]')
        nextpass.send_keys(senha)
        time.sleep(0.1)
        signin = driver.find_element(by='xpath', value='//*[@class="_f92fbce _cb4cb62 _18f4de1 _f7a0730"]')
        signin.click()
        time.sleep(1)

        print(f"User: {iosenh} | Passord: {senha} | Progresso: {round((bglla.index(iosenh)+1)*100/len(bglla), 2)}% &{bglla.index(iosenh)+1}/{len(bglla)} | ProgressoConta: 1/2 | Estado: Estage 1")


        driver.get(link_torneio)
        #link_do_torneio
        time.sleep(3)
        act1 = driver.find_element(by='xpath', value='//*[@id="minilobby-actions"]')
        act1.click()
        time.sleep(2)

        act2 = driver.find_element(by='xpath', value='//*[@id="modalBtnTXTWBCLI_UNEXPECTED_ERROR_MODAL_BUTTON_CONTINUE"]')
        act2.click()
        time.sleep(1)

        act3 = driver.find_element(by='xpath', value='//*[@id="minilobby-actions"]')
        act3.click()
        time.sleep(1)

        act4 = driver.find_element(by='xpath', value='//*[@id="modalBtnTXTWBCLI_COMMON_OK"]')
        act4.click()
        time.sleep(1)

        driver.quit()
        print(f"\033[32mUser: {iosenh} | Passord: {senha} | Progresso: {round((bglla.index(iosenh)+1)*100/len(bglla), 2)}% &{bglla.index(iosenh)+1}/{len(bglla)} | ProgressoConta: 2/2 | Estado: Completo\033[m")
        
        print("")
        print("=-"*30)
        print("")


def entra_na_torneira2(link_torneio):
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys

    time.sleep(7)

    with open("credentials.txt", "r") as arquivo:
        numli=arquivo.read()
        numli=numli.split("\n")

    senha=numli[0]

    with open("login2.txt", "r") as arquivo:
        bglla=arquivo.read()
        bglla=bglla.split("\n")



    for iosenh in bglla:
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}


        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome()
        
        driver.get("https://www.pokerstars.com/login/")
        time.sleep(3)
        next = driver.find_element(by='xpath', value='//*[@id="onetrust-accept-btn-handler"]')
        next.click()
        time.sleep(0.2)
        
        email = driver.find_element(by='xpath', value='//*[@id="userId"]')
        email.send_keys(iosenh)
        #iosenh
        time.sleep(0.1)


        nextpass = driver.find_element(by='xpath', value='//*[@id="password"]')
        nextpass.send_keys(senha)
        time.sleep(0.1)
        signin = driver.find_element(by='xpath', value='//*[@class="_f92fbce _cb4cb62 _18f4de1 _f7a0730"]')
        signin.click()
        time.sleep(1)

        print(f"User: {iosenh} | Passord: {senha} | Progresso: {round((bglla.index(iosenh)+1)*100/len(bglla), 2)}% &{bglla.index(iosenh)+1}/{len(bglla)} | ProgressoConta: 1/2 | Estado: Estage 1")


        driver.get(link_torneio)
        #link_do_torneio
        time.sleep(3)
        act1 = driver.find_element(by='xpath', value='//*[@id="minilobby-actions"]')
        act1.click()
        time.sleep(2)

        act2 = driver.find_element(by='xpath', value='//*[@id="modalBtnTXTWBCLI_UNEXPECTED_ERROR_MODAL_BUTTON_CONTINUE"]')
        act2.click()
        time.sleep(1)

        act3 = driver.find_element(by='xpath', value='//*[@id="minilobby-actions"]')
        act3.click()
        time.sleep(1)

        act4 = driver.find_element(by='xpath', value='//*[@id="modalBtnTXTWBCLI_COMMON_OK"]')
        act4.click()
        time.sleep(1)

        driver.quit()
        print(f"\033[32mUser: {iosenh} | Passord: {senha} | Progresso: {round((bglla.index(iosenh)+1)*100/len(bglla), 2)}% &{bglla.index(iosenh)+1}/{len(bglla)} | ProgressoConta: 2/2 | Estado: Completo\033[m")
        print("")
        print("=-"*30)
        print("")