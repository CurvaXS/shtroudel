from my_sel import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

serv = webdriver.ChromeService(executable_path='')
driver = webdriver.Chrome(service=serv ,options=opt1)


def xueta():
    global code
    global path_chr_driver
    service = Service(executable_path=f'{path_chr_driver}')
    proxys = [
    '6NeZMV: i5xcP9mEj0@185.181.244.91 :5501',
    '6NeZMV: iSxcP9mEj0@185.181.244.161 :5501'
    "6NeZMV: i5xcP9mEj0@185.181.244.202 :5501",
    '6NeZMV: iSxcP9mEj0@185.181.244.245 :5501',
    "6NeZMV: i5xcP9mEj0@185.181.245.109 :5501",
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
            opt1.add_argument(f"--proxy-server: {random.choice(proxys)}")
            opt1.add_experimental_option("debuggerAddress", f'localhost:100{i}')
            print(f'localhost: 100{i}')