import re

stre = "jb001"
stre = re.split(r'(\d+)', stre)
print(stre)
temp = stre[0]
stre.remove('jb')
stre.remove('')
for i in stre:
    re = int(i) + 1
    ad = f'{temp}00{re}'
    print(ad)
