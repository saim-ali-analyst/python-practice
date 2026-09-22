import random
number = random.randint(1,100)
print('Welcome to the guessing game ')
print('guess the number between 1 to 100')
attampts = 0

while True:
    user = int(input('Enter your number'))
    attampts += 1
    difference = abs(user - number)
    if user == number :
        print('corrent you have won the game')
        print(f'Total attampts : {attampts}')
        break
    elif difference < 10:
        print('print you are close')
    elif user < number:
        print('you are low')
    elif user > number:
        print('you are high')
    
