import time
import pickle
import random
import subprocess
from trsh.my_sel import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


code = ''
num_instances = 0
path_chr_driver = r""

def path_to_chromeprofiles():
    fff = input("Введите путь на профили хрома: ")
    #Пример:
    #fff = r'D:\donttch\Mock-chrome\chromeprofile_'

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    num_instances = 10
    #кол-во окон (рекомедн. 1-10):
    for i in range(num_instances):
        link = fr"{fff}{i}"
        subprocess.Popen([chrome_path, f"--remote-debugging-port=100{i}", f"--user-data-dir={link}"])

            # Add a delay to ensure each instance has time to start
        time.sleep(1)

    check = input("Введите GO чтобы начать: ")
    if (check=="GO"):
        global code
        global path_chr_driver
        code = input("Введите код: ")
        path_chr_driver = input("Введите cсылку на хром драйвер: ")
        xueta()
    else:
        print("Неверная комманда! Перезапустите скрипт =(")

def xueta():
    global code
    global path_chr_driver
    service = Service(executable_path=f'{path_chr_driver}')

    proxys = [
            '6NeZMV:iSxcP9mEj0@185.181.244.91:5501',
            '6NeZMV:iSxcP9mEj0@185.181.244.161:5501',
            '6NeZMV:iSxcP9mEj0@185.181.244.202:5501',
            '6NeZMV:iSxcP9mEj0@185.181.244.245:5501',
            '6NeZMV:iSxcP9mEj0@185.181.245.109:5501',
        ]

    def input():
        code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')
        code_input.clear()
        code_input.send_keys(f'{code}')
        code_button = driver.find_element(By.CSS_SELECTOR, value='[data-v-ea610df3]').click()

    opt1 = Options()
    a = 10
    k = a
    for j in range(a):
        for i in range(k):
            opt1.add_argument(f"--proxy-server:{random.choice(proxys)}")
            opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
            print(f'localhost:100{i}')

        driver = webdriver.Chrome(service=service, options=opt1)
        if (driver.current_url == 'https://drgn4q.casino/bonus'):
            input()
        else:
            driver.get("https://drgn4q.casino/bonus")
            time.sleep(1)
            print('xui')
            input()

        k -= 1
    



"""
code = input("Введите код: ")
service = Service(executable_path='./chromedriver.exe')

proxys = [
        '6NeZMV:iSxcP9mEj0@185.181.244.91:5501',
        '6NeZMV:iSxcP9mEj0@185.181.244.161:5501',
        '6NeZMV:iSxcP9mEj0@185.181.244.202:5501',
        '6NeZMV:iSxcP9mEj0@185.181.244.245:5501',
        '6NeZMV:iSxcP9mEj0@185.181.245.109:5501',
    ]

def input():
    code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')
    code_input.clear()
    code_input.send_keys(f'{code}')
    code_button = driver.find_element(By.CSS_SELECTOR, value='[data-v-ea610df3]').click()

opt1 = Options()
a = 3
k = a
for j in range(a):
    for i in range(k):
        opt1.add_argument(f"--proxy-server:{random.choice(proxys)}")
        opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')
        print(f'localhost:100{i}')

    driver = webdriver.Chrome(service=service, options=opt1)
    if (driver.current_url == 'https://drgn4q.casino/bonus'):
        input()
    else:
        driver.get("https://drgn4q.casino/bonus")
        time.sleep(1)
        input()

        k -= 1
"""

if __name__ == "__main__":
    print('Pivo!')
    path_to_chromeprofiles()

#code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')


    

