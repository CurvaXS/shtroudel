from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import time
import subprocess

# r_prx = random.choice(proxys)

temporary_number_of_sessions = 0

choreme_driver = r'D:\donttch\From_Telegram_to_Chrome\shtroudel\chromedriver.exe'
serv = webdriver.ChromeService(executable_path=choreme_driver)
opt1 = Options()
driver = webdriver.Chrome(service=serv ,options=opt1)

def single(i, proxy):
    opt1.add_argument(f"--proxy-server={proxy}")
    opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
    driver.get('https://2ip.ru/')
    time.sleep(9999)

def multi(session_quantity):
    k=session_quantity
    for j in range(session_quantity):
        for i in range(k):
            #opt1.add_argument(f"--proxy-server:{rand_proxy}")
            opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
            print(f'localhost:100{i}')
        
        driver = webdriver.Chrome(service=serv, options=opt1)
        driver.get("https://drgn4q.casino/bonus")
        k -= 1
    time.sleep(1)

def input_code(code, session_quantity):
    k=session_quantity
    for j in range(session_quantity):
        for i in range(k):
            opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
            print(f'localhost:100{i}')
        
        driver = webdriver.Chrome(service=serv, options=opt1)
        
        code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')
        code_input.clear()
        code_input.send_keys(f'{code}')
        code_button = driver.find_element(By.CSS_SELECTOR, value='[data-v-ea610df3]').click()
        k -= 1

    time.sleep(1)



def path_to_chromeprofiles():
    fff = input("Введите путь на профили хрома: ")
    kol = input("Введите кол-во сессий: ")
    #Пример:
    #fff = r'D:\donttch\Mock-chrome\chromeprofile_'
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    num_instances = int(kol)
    #кол-во окон (рекомедн. 1-10):
    for i in range(num_instances):
        link = fr"{fff}{i}"
        subprocess.Popen([chrome_path, f"--remote-debugging-port=100{i}", f"--user-data-dir={link}"])
            # Add a delay to ensure each instance has time to start
        time.sleep(1)

def main():
    global temporary_number_of_sessions
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