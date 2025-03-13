import time
from cipher import *


run_program = ''
cryptographic_algorithm = ''

def choose_cryptographic_algorithm():
    while True:
        print('Choose one from the four cryptographic algorithms to use for encryption and decryption')
        print('1. Ceasar Cipher\n2. Monoalphabetic Cipher\n3. Bitwise XOR Cipher\n4. Own Cipher\n5. Close the Program')
        choice = input('Enter the number of your choice (1-5): ').lower()
        if choice not in ('1', '2', '3', '4', '5'):
            print('Invalid input. Input should only be number 1-4\n')
            time.sleep(2)
            os.system('cls')
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
    os.system('cls')
    print('Console-Based Cryptographic Program\n')

    cryptographic_algorithm = choose_cryptographic_algorithm()
    if cryptographic_algorithm == '1':
        caesar_cipher()
    elif cryptographic_algorithm == '2':
        monoalphabetic_cipher()
    elif cryptographic_algorithm == '3':
        bitwise_xor_cipher()
    elif cryptographic_algorithm == '4':
        own_cipher()
    elif cryptographic_algorithm == '5':
        os.system('cls')
        print('Thank for using this Console-Based Cryptographic Program!')
        time.sleep(2)
        break
    run_program = prompt_run_again()
    if run_program == 'n':
        break

