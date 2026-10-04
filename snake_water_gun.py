# ==========================================
#   Snake Water Gun Game
#   Author: Saim Ali
# ==========================================

import random

print('============ Welcome to Snake Water Gun Game ============')

name = input('What is your name? ')
choices = ['Snake', 'Water', 'Gun']

user = 0
computer_score = 0
draw = 0

while True:
    choice = input('Choose (Snake / Water / Gun) or type Exit: ').capitalize()

    if choice == 'Exit':
        print('Successfully Exited')
        break

    if choice not in choices:
        print('Invalid choice. Please choose Snake, Water, or Gun.')
        continue

    computer = random.choice(choices)
    print(f'Computer chose: {computer}')

    if choice == computer:
        draw += 1
        print('Draw')
    elif (choice == 'Snake' and computer == 'Water') or \
         (choice == 'Water' and computer == 'Gun') or \
         (choice == 'Gun' and computer == 'Snake'):
        user += 1
        print(f'{name} Wins!')
    else:
        computer_score += 1
        print('Computer Wins!')

print(f'\nTotal {name}: {user} wins')
print(f'Total Computer: {computer_score} wins')
print(f'Total Draws: {draw}')