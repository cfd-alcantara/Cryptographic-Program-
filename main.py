import time
from cipher import *


run_program = ''
cryptographic_algorithm = ''

def choose_cryptographic_algorithm():
    while True:
        print('Choose one from the four cryptographic algorithms to use for encryption and decryption')
        print('1. Ceasar Cipher\n2. Monoalphabetic Cipher\n3. Vernam Cipher\n4. N/A\n5. Close the Program')
        choice = input('Enter the number of your choice (1-5): ').lower()
        if choice not in ('1', '2', '3', '4', '5'):
            print('Invalid input. Input should only be number 1-4\n')
            time.sleep(2)
        else:
            return choice

def prompt_run_again():
    while True:
        print('\nRun the program again?')
        response = input('Y/N: ').lower()
        if response == 'y':
            print()
            return response
        elif response == 'n':
            print('Goodbye, thank you for using this program!!')
            return response
        else:
            print('Invalid input. Input either Y for yes or N for no')
            time.sleep(2)

while True:
    print('Console-Based Cryptographic Program\n')

    cryptographic_algorithm = choose_cryptographic_algorithm()
    if cryptographic_algorithm == '1':
        caesar_cipher()
    elif cryptographic_algorithm == '2':
        monoalphabetic_cipher()
    elif cryptographic_algorithm == '3':
        vernam_cipher()
    elif cryptographic_algorithm == '4':
        print('N/A')
    elif cryptographic_algorithm == '5':
        print('Thank for using this Console-Based Cryptographic Program!')
        time.sleep(2)
        break
    run_program = prompt_run_again()
    if run_program == 'n':
        break

