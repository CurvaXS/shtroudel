import subprocess
import time


fff = input("Введите путь на профили хрома: ")
    #Пример:
    #'D:\donttch\Mock-chrome\chromeprofile_'

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
num_instances = int(input("Введите кол-во окон (рекомедн. 1-10): "))

for i in range(num_instances):
    link = fr"{fff}{i}"
    subprocess.Popen([chrome_path, f"--remote-debugging-port=100{i}", f"--user-data-dir={link}"])

        # Add a delay to ensure each instance has time to start
    time.sleep(1)

check = input("Введите GO чтобы начать: ")
if (check=="GO"):
    global code
    code = input("Введите код: ")
        #chrome()
else:
    print("Неверная комманда! Перезапустите скрипт =(")

