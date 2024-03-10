from my_sel import webdriver
from multiprocessing import Pool
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import random


#url = "https://2ip.ru/"
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

proxy = [
    '72.10.164.178:13999', '67.43.236.20:6605',
    '72.10.164.178:28093', '67.43.228.253:29367',
    '192.252.209.155:14455', '138.68.180.109:80',
    '159.203.61.169:3128','91.205.197.226:8080',
    '5.252.23.206:1080', '91.202.230.219:8080',
]

#options.add_argument(f"--proxy-server={random.choice(proxy)}")
service = Service(executable_path='./chromedriver.exe')


def get_data(url):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url=url)
        time.sleep(1)

        #code_input = driver.find_element_by_css_selector('placeholder="Введите код"')
        code_input = driver.find_element(By.CSS_SELECTOR, value='[placeholder="Введите код"]')
        code_input.clear()
        code_input.send_keys('хуй')
        time.sleep(10)

        code_button = driver.find_element(By.CSS_SELECTOR, value='[data-v-ea610df3]').click()
        time.sleep(10)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    process_count = int(input("Кол-во окон: "))
    url = "https://drgn4q.casino/bonus"
    urls_list = [url] * process_count
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)