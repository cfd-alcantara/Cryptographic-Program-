import time
import string
import ast
import os
from utils import mode_input, ask_key_method, input_key, input_plaintext, input_ciphertext, print_encryption_result, print_decryption_result, generate_repeating_key, is_hex, generate_nonrepeating_key, expand_key_to_match

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase

def caesar_cipher():
    os.system('cls')
    print('Caesar Cipher\n')
    mode = mode_input()


    while True: #Gets key and validates
        key = input('\nEnter the key (1-26): ')

        try:
            key = int(key)
            if key >= 1 and key <= 26:
                break
            else:
                print('Invalid input. Input should only be numbers 1-26')
                time.sleep(2)
        except:
            print('Invalid input. Input should only be numbers 1-26')
            time.sleep(2)

    if mode == 'e':
        ciphertext = ''

        plaintext = input_plaintext()
        for letter in plaintext:
            if letter.isalpha():
                letters = lower_case_letters if letter.islower() else upper_case_letters
                index = letters.find(letter)
                index += key
                if index >= 26:
                    index -= 26
                ciphertext += letters[index]
            else:
                ciphertext += letter

        os.system('cls')
        print('Caesar Cipher Result')
        print_encryption_result(plaintext, key, ciphertext)
    else:
        plaintext = ''

        ciphertext = input_ciphertext()
        for letter in ciphertext:
            if letter.isalpha():
                letters = lower_case_letters if letter.islower() else upper_case_letters
                index = letters.find(letter)
                index -= key
                if index < 0:
                    index += 26
                plaintext += letters[index]
            else:
                plaintext += letter

        os.system('cls')
        print('Caesar Cipher Result')
        print_decryption_result(ciphertext, key, plaintext)

def bitwise_xor_cipher():
    os.system('cls')
    print("Bitwise XOR Cipher\n")

    mode = mode_input()

    if mode == 'e':
        plaintext = input_plaintext()

        key_method = ask_key_method()
        if key_method == 'm':
            key = input_key()

            if len(key) < len(plaintext):
                key = expand_key_to_match(plaintext, key)
        else:
            key = generate_repeating_key(upper_case_letters + lower_case_letters, len(plaintext))

        ciphertext = ''
        for i in range(len(plaintext)):
            ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))

        hex_ciphertext = ciphertext.encode().hex()


        os.system('cls')
        print('Bitwise XOR Cipher Result')
        print_encryption_result(plaintext, key, hex_ciphertext)

    else:
        decrypted_text = ""
        ciphertext = input_ciphertext()
        orig_ciphertext = ciphertext

        key = input_key()

        try:
            if is_hex(ciphertext) == True:
                ciphertext = bytes.fromhex(ciphertext).decode()

            if len(key) < len(ciphertext):
                key = expand_key_to_match(ciphertext, key)

            for i in range(len(ciphertext)):
                decrypted_text += chr(ord(ciphertext[i]) ^ ord(key[i]))

            os.system('cls')
            print('Bitwise XOR Cipher Result')
            print_decryption_result(orig_ciphertext, key, decrypted_text)
        except:
            print('Wrong key')

def monoalphabetic_cipher():
    os.system('cls')
    print("Monoalphabetic Cipher\n")

    mode = mode_input()
    if mode == 'e':

        # Generate cipher key
        key = generate_nonrepeating_key(upper_case_letters, len(upper_case_letters))
        key = dict(zip(upper_case_letters, key))

        plaintext = input_plaintext()
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    ciphertext += key[char.upper()].lower()
                else:
                    ciphertext += key[char]
            else:
                ciphertext += char

        os.system('cls')
        print('Monoalphabetic Cipher Result')
        print_encryption_result(plaintext, key, ciphertext)
    else:
        ciphertext = input_ciphertext()
        try:
            key = input_key()
            key = ast.literal_eval(key)

            reverse_key = {v: k for k, v in key.items()}
            plaintext = ''
            for char in ciphertext:
                if char.isalpha():
                    if char.islower():
                        plaintext += reverse_key[char.upper()].lower()
                    else:
                        plaintext += reverse_key[char]
                else:
                    plaintext += char
            os.system('cls')
            print('Monoalphabetic Cipher Result')
            print_decryption_result(ciphertext, key, plaintext)

        except:
            print('Key is invalid')

def own_cipher():
    os.system('cls')
    print()
    mode = mode_input()

    if mode == 'e':
        plaintext = input_plaintext()


        key_method = ask_key_method()
        if key_method == 'm':
            key = input_key()

            if len(key) < len(plaintext):
                key = expand_key_to_match(plaintext, key)
        else:
            key = generate_repeating_key(upper_case_letters + lower_case_letters, len(plaintext))

        if len(key) < len(plaintext):
            key = expand_key_to_match(plaintext, key)

        ciphertext = ''
        for i in range(len(plaintext)):
            dec_value = ord(plaintext[i])

            difference = ord(plaintext[i]) - ord(key[i])
            if difference % 2 == 0:
                dec_value += 5
            else:
                dec_value -= 21
            ciphertext += chr(dec_value)

        os.system('cls')
        print('Own Cipher Result')
        print_encryption_result(plaintext, key, ciphertext.encode().hex())

    else:
        ciphertext = input_ciphertext()
        orig_ciphertext = ciphertext
        if is_hex(ciphertext):
            ciphertext = bytes.fromhex(ciphertext).decode()

        key = input_key()

        if len(key) < len(ciphertext):
            key = expand_key_to_match(ciphertext, key)

        plaintext = ''
        
        for i in range(len(ciphertext)):
            dec_value = ord(ciphertext[i])

            test_character = chr(dec_value - 5)

            if (ord(test_character) - ord(key[i])) % 2 == 0:
                plaintext += test_character
            else:
                plaintext += chr(dec_value + 21)

        os.system('cls')
        print('Own Cipher Result')
        print_decryption_result(orig_ciphertext, key, plaintext)
