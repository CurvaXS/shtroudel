from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import time
import subprocess

# r_prx = random.choice(proxys)

"""
"""
#chrome_driver = input("Введите путь на драйвер хрома (абсолютаная ссылка): ")
serv = webdriver.ChromeService(executable_path=r'.\chromedriver.exe') 
opt1 = Options()
driver = webdriver.Chrome(service=serv ,options=opt1)

opt1.add_argument("--disable-blink-features=AutomationControlled")
#opt1.add_experimental_option('excludeSwitches', ['enable-logging'])
#opt1.add_experimental_option('useAutomationExtension', False)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
  '''
})


def single(i, proxy):
    opt1.add_argument(f"--proxy-server={proxy}")
    opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
    driver.get('https://drgn4r.casino/bonus')
    time.sleep(9999)
    
 

def multi(session_quantity):
    k=session_quantity
    for j in range(session_quantity):
        for i in range(k):
            #opt1.add_argument(f"--proxy-server:{rand_proxy}")
            opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
            print(f'localhost:100{i}')
        
        driver = webdriver.Chrome(service=serv, options=opt1)
        driver.get("https://drgn4r.casino/bonus")
        k -= 1

def input_code(code, session_quantity):
    k=session_quantity
    for j in range(session_quantity):
        for i in range(k):
            opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
            print(f'localhost:100{i}')
        
        driver = webdriver.Chrome(service=serv, options=opt1)
        code_input = driver.find_element(By.CSS_SELECTOR, '[placeholder="Введите код"]')
        code_input.clear()
        code_input.send_keys(f'{code}')
        code_button = driver.find_element(
            By.XPATH,
            "//button[@class='!rounded-l-none btn size-md color-primary v-popper--has-tooltip']/div[text() = 'Активировать']"
            
        )
        code_button.click()
        
        time.sleep(0.04)

        iframe = driver.find_element(By.XPATH, 
            '//div[@class="relative inline-block w-full whitespace-normal rounded-md bg-bg-wrapper text-left align-middle text-base shadow-modal transition-[max-width] max-w-md"]/div[2]/div/div/div/iframe'
       )
        print(iframe)
        
        driver.switch_to.frame(iframe)
        print('PIZDEC')
        recapt = driver.find_element(By.XPATH, '//span[@id="recaptcha-anchor"]')
        recapt.click()
        print(recapt)
        #driver.switch_to.default_content()
        
        k -= 1

    #time.sleep(1)


def path_to_chromeprofiles():
    print("Если у вас windows 10 - Введите 10")
    print("Если у вас windows 11 - Введите 11")
    print("")
    win_choise = int(input("Введите ответ: "))
    print("")

    if (win_choise == 10):
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    elif (win_choise == 11):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    fff = input("Введите путь на профили хрома: ")
    kol = input("Введите кол-во сессий: ")

    #Пример:
    #fff = r'D:\donttch\Mock-chrome\chromeprofile_'
    
    
    num_instances = int(kol)
    #кол-во окон (рекомедн. 1-10):
    for i in range(num_instances):
        link = fr"{fff}\profile_{i}"
        subprocess.Popen([chrome_path, f"--remote-debugging-port=100{i}", f"--user-data-dir={link}"])
        time.sleep(1)

def main():
    print('')
    print("Создание сессий - create_s")
    print("Использование существующих - load_s")
    print('Ввод кода - code_s')
    print('')
    variable = input('Введите ваш выбор: ')
    print('')
    if (variable == "create_s"):
        path_to_chromeprofiles()
    elif (variable == "load_s"):
        print('Одиночный - S')
        print('Многопоточный - M')
        print('')
        ver = input("Введите выбранный режим: ")

        if (ver == "S" or ver == "s"):
            proxy = input('Введите прокси: ')
            i = input('Введите номер хоста: ')
            single(i, proxy)

        elif (ver == "M" or ver == "m"):
            quantity = int(input("Введите кол-во сессий: "))
            multi(quantity)

    elif (variable == "code_s"):
        tp = int(input("Введите кол-во сессий: "))
        cd = input('Введите код: ')
        input_code(cd, tp)


if __name__ == "__main__":
    main()