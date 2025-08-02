import random
sec = random.randint(0, 10)
print('''
    ___________________________________________
   | Welcome to Guessing Game !!               |
   | You have to guess a number between 0 to 10|
   |___________________________________________|
''')
i = 0
while i < 3:
    guess = int(input(">> "))
    i += 1
    if guess == sec:
        print("you did it")
        break
else:
    print("get in p")
    print(f'selected number was {sec}')
