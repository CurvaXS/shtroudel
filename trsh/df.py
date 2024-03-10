import subprocess

chr_path = 'C:\Program Files\Google\Chrome\Application'
cd_command = f'cd {chr_path}'
subprocess.run(cd_command, shell=True, check=True)


user_data = 'D:\donttch\Mock-chrome\chromeprofile'
other = f'chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\donttch\Mock-chrome\chromeprofile"'
subprocess.run(other, shell=True, check=True)