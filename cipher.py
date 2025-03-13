import time
import string
import ast
import os
from utils import mode_input, generate_repeating_key, is_hex, convert_binary, generate_nonrepeating_key, expand_key_to_match

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase

def caesar_cipher():
    os.system('cls')
    plain_text = ''
    cipher_text = ''

    print('Caesar Cipher\n')
    mode = mode_input()


    while True: #Gets key and validates
        key = input('Enter the key (1-26): ')
        if not key.isdigit():
            print('Invalid input. Input should only be numbers 1-26')
            time.sleep(2)
            continue

        key = int(key)
        if key >= 1 and key <= 26:
            break
        else:
            print('Invalid input. Input should only be numbers 1-26')
            time.sleep(2)

    if mode == 'e':
        user_plain_text = input('Enter the text to encrypt: ')
        for letter in user_plain_text:
            if letter.isalpha():
                letters = lower_case_letters if letter.islower() else upper_case_letters
                index = letters.find(letter)
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                cipher_text += letters[new_index]
            else:
                cipher_text += letter

        os.system('cls')
        print('Caesar Cipher Result')
        print(f'\nPLAINTEXT: {user_plain_text}')
        print(f'Key: {key}')
        print(f'ENCRYPTED MESSAGE or CIPHERTEXT: {cipher_text}')
    else:
        user_cipher_text = input('Enter the text to decrypt: ')
        for letter in user_cipher_text:
            if letter.isalpha():
                letters = lower_case_letters if letter.islower() else upper_case_letters
                index = letters.find(letter)
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                plain_text += letters[new_index]
            else:
                plain_text += letter

        os.system('cls')
        print('Caesar Cipher Result')
        print(f'\nCIPHERTEXT: {user_cipher_text}')
        print(f'Key: {key}')
        print(f'DECRYPTED MESSAGE or PLAINTEXT: {plain_text}') 

def bitwise_xor_cipher():
    os.system('cls')
    print("Bitwise XOR Cipher\n")

    mode = mode_input()

    if mode == 'e':
        plaintext = input("Enter the plaintext to encrypt: ")
        key = generate_repeating_key(upper_case_letters, len(plaintext))

        print("\nPlaintext:", plaintext)
        print("Key:", key)

        ciphertext = ''
        for i in range(len(plaintext)):
            ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))

        binary_ciphertext = ''
        binary_ciphertext = ' '.join(f'{ord(c):08b}' for c in ciphertext)

        hex_ciphertext = ciphertext.encode().hex()


        os.system('cls')
        print('Bitwise XOR Cipher Result')
        print('\nPlaintext:', plaintext)
        print('Key:', key)
        print("Ciphertext in Binary: ", (binary_ciphertext))
        print("Ciphertext in Hexadecimal: ", (hex_ciphertext))

    else:
        decrypted_text = ""
        ciphertext = input("Enter the ciphertext to decrypt: ").upper()
        key = input(f"Enter the key: ").upper()

        if is_hex(ciphertext) == True:
            converted_ciphertext = bytes.fromhex(ciphertext).decode()
        else:
            converted_ciphertext = convert_binary(ciphertext)

        for i in range(len(converted_ciphertext)):
            decrypted_text += chr(ord(converted_ciphertext[i]) ^ ord(key[i]))

        os.system('cls')
        print('Bitwise XOR Cipher Result')
        print('Ciphertext:', ciphertext)
        print('Key:', key)
        print("Decrypted Text:", decrypted_text)

def monoalphabetic_cipher():
    os.system('cls')
    print("Monoalphabetic Cipher\n")

    mode = mode_input()
    if mode == 'e':

        # Generate cipher key
        key = generate_nonrepeating_key(upper_case_letters, len(upper_case_letters))
        key = dict(zip(upper_case_letters, key))

        plaintext = input("Enter the message to encrypt: ")
        encrypted_message = ''
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    encrypted_message += key[char.upper()].lower()
                else:
                    encrypted_message += key[char]
            else:
                encrypted_message += char

        os.system('cls')
        print('Monoalphabetic Cipher Result')
        print('\nPlaintext:', plaintext) 
        print('Key:', key)
        print("Encrypted message:", encrypted_message)
    else:
        ciphertext = input("Enter the message to decrypt: ")
        key_str = input("Enter the encryption key as a dictionary: \n")  
        key = ast.literal_eval(key_str)

        reverse_key = {v: k for k, v in key.items()}
        decrypted_message = ''
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_message += reverse_key[char.upper()].lower()
                else:
                    decrypted_message += reverse_key[char]
            else:
                decrypted_message += char
        
        os.system('cls')
        print('Monoalphabetic Cipher Result')
        print('\nCiphertext:', ciphertext)
        print('key:', reverse_key)
        print('Decrypted message:', decrypted_message)

def own_cipher():
    os.system('cls')
    print()
    mode = mode_input()

    if mode == 'e':
        plaintext = input("Enter the plaintext to encrypt: ")
        key = input('Enter the key: ')

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
        print('\nPlaintext  :', plaintext)
        print('Key        :', key)
        print('Ciphertext :', ciphertext.encode().hex())

    else:
        ciphertext = input("Enter the ciphertext to decrypt: ")
        converted_ciphertext = bytes.fromhex(ciphertext).decode()
        key = input('Enter the key: ')

        if len(key) < len(converted_ciphertext):
            key = expand_key_to_match(converted_ciphertext, key)

        plaintext = ''
        
        for i in range(len(converted_ciphertext)):
            dec_value = ord(converted_ciphertext[i])

            test_character = chr(dec_value - 5)

            if (ord(test_character) - ord(key[i])) % 2 == 0:
                plaintext += test_character
            else:
                plaintext += chr(dec_value + 21)

        os.system('cls')
        print('Own Cipher Result')
        print('\nCiphertext :', ciphertext)
        print('Key        :', key)
        print('Plaintext  :', plaintext)
