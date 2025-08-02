import re

stre = input(">> ")
stre = re.split(r'(\d+)', stre)
print(stre)
temp = stre[0]
print(temp)
for i in stre:
    try:
        if int(i):
            print(f'this is if: {type(i)}')
        else:
            print('not an integer')
            #re = int(i) + 1
            #ad = f'{temp}0{re}'
            #print(ad)
    except:
        pass
