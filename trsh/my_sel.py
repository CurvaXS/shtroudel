from trsh.my_sel import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random

choreme_driver = r'C:\Users\keksp\OneDrive\Рабочий стол\mkr\chromedriver.exe'
serv = webdriver.ChromeService(executable_path=choreme_driver)
opt1 = Options()
driver = webdriver.Chrome(service=serv ,options=opt1)

def input():
    code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')
    code_input.clear()
    code_input.send_keys(f'')
    code_button = driver.find_element(By.CSS_SELECTOR, value='[data-v-ea610df3]').click()

def single(proxy, i):
    opt1.add_argument(f"--proxy-server: {proxy}")
    opt1.add_experimental_option('debuggerAddress', f'localhost:100{i}')

def multi(a, k, proxys):
    for j in range(a):
        for i in range(k):
            opt1.add_argument(f"--proxy-server: {random.choice(proxys)}")
            opt1.add_experimental_option("debuggerAddress", f'localhost:100{i}')
            print(f'localhost: 100{i}')