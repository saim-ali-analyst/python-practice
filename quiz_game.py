# ==========================================
#   Kon Banega Crorepati Quiz Game
#   Author: Saim Ali
# ==========================================

print('===================== Kon Banega Crorepati ===================')

name = input('What is your name? ')
print('Welcome to Kon Banega Crorepati', name)
print("Let's play")

total_price = 0

print('Please select the number of the answer (1, 2, 3, 4)')
print('Your first question\n')
print('What is the capital of Pakistan?\n')
print(''' 1, Karachi
 2, Peshawar
 3, Islamabad
 4, Mardan ''')

while True:

    q1 = int(input('Please select the right answer: '))

    if q1 == 3:
        print('Correct answer')
        total_price = total_price + 1000
        print('You have won', total_price, 'Rupees')

        print('Your second question is\n')
        print('How many provinces are there in Pakistan?')
        print(''' 1, 5
 2, 10
 3, 4
 4, 3 ''')

        q2 = int(input('Please select the right answer: '))

        if q2 == 3:
            print('Correct answer')
            total_price = total_price + 1000
            print('You have won', total_price, 'Rupees')

            print("Do not want to play? Press 'Quit'")
            print("Want to play? Press 'Not Quit'")
            c1 = input('Do you want to play more or quit? ')

            if c1 == 'Quit':
                print('Exited from game')
                print('Total money earned', total_price)
                break

            else:
                print('Great', name)
                print('Your third question is\n')
                print('What is the national animal of Pakistan?')
                print(''' 1, Eagle
 2, Tiger
 3, Dragon
 4, Markhor ''')

                q3 = int(input('Please select the right answer: '))

                if q3 == 4:
                    print('Correct answer')
                    print('Game is finished')
                    total_price = total_price + 1000
                    print('You have won', total_price, 'Rupees')
                    break

                else:
                    print('Wrong answer')
                    print('Money earned', total_price)
                    break

        else:
            print('Wrong answer')
            print('Money earned', total_price)
            break

    else:
        print('Wrong answer')
        print('Money earned', total_price)
        break


print('========= Game result ==========')
print('Participant name:', name)
print('Total earned reward:', total_price)
