# ==========================================
#   Secret Language App (Encode / Decode)
#   Author: Saim Ali
# ==========================================

import random
import string

print('========== Welcome to Saim Secret Service ==========')
name = input('What is your name Sir? ')

choice = input('Please select one: Encoding / Decoding ')

if choice == 'Encoding':
    print('Welcome to Encoding,', name)
    m = input('Please input the message you want to encode: ')

    message = m.split()
    result = ['']

    for i in message:
        m2 = i
        if len(m2) < 3:
            m2 = m2[::-1]
        elif len(m2) >= 3:
            random_1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            random_2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            m2 = random_1 + m2[1:] + m2[0] + random_2

        result.append(m2)

    final_result = ' '.join(result)
    print(f'Your message : {final_result}')

elif choice == 'Decoding':
    print('Welcome to Decoding,', name)
    m = input('Please input the message you want to decode: ')

    message = m.split()
    result = ['']

    for i in message:
        m2 = i
        if len(i) < 3:
            m2 = m2[::-1]
        elif len(i) > 3:
            m2 = m2[3:-3]
            m2 = m2[-1] + m2[0:-1]

        result.append(m2)

    t_result = ' '.join(result)
    print(f'Your message : {t_result}')

else:
    print('Invalid option')    





            
