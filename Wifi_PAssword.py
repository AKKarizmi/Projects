import subprocess
import os
li = os.listdir()
if not "result.txt" in li:
    pas = open("result.txt", "x")
else:
    pass
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [j.split(":")[1][1:-1] for j in data if "All User Profile" in j]
for j in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', j, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        result = "{:<30}| {:<}".format(j, results[0])
        # pas = open("result.txt", "x")
        # if pas.exist():
        pas = open("result.txt", "a")
        pas.write(result)
        pas.close()
        # else:
            # pass
        # print(result)
    except IndexError:
        print("{:<30}| {:<}".format(j, ""))
