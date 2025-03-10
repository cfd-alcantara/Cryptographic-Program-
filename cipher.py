import time
import string
import ast
from utils import mode_input, generate_repeating_key, is_hex, convert_binary, generate_nonrepeating_key

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase

def caesar_cipher():
    plain_text = ''
    cipher_text = ''

    print('\nCaesar Cipher\n')
    mode = mode_input()
    while True:
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
        user_plain_text = input('enter the text to encrypt: ')
        for letter in user_plain_text:
            if letter.islower():
                index = lower_case_letters.find(letter)
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                cipher_text += lower_case_letters[new_index]
            elif letter.isupper():
                index = upper_case_letters.find(letter)
                new_index = index + key
                if new_index >= 26:
                    new_index -= 26
                cipher_text += upper_case_letters[new_index]
            else:
                cipher_text += letter
        print(f'\nPLAINTEXT: {user_plain_text}')
        print(f'ENCRYPTED MESSAGE or CIPHERTEXT: {cipher_text}')
    else:
        user_cipher_text = input('enter the text to decrypt: ')
        for letter in user_cipher_text:
            if letter.islower():
                index = lower_case_letters.find(letter)
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                plain_text += lower_case_letters[new_index]
            elif letter.isupper():
                index = upper_case_letters.find(letter)
                new_index = index - key
                if new_index < 0:
                    new_index += 26
                plain_text += upper_case_letters[new_index]
            else:
                plain_text += letter
        print(f'\nCIPHERTEXT: {user_cipher_text}')
        print(f'DECRYPTED MESSAGE or PLAINTEXT: {plain_text}') 

def vernam_cipher():
    print("\nVernam Cipher\n")

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


        print("Ciphertext in Binary: ", (binary_ciphertext))
        print("Ciphertext in Hexadecimal: ", (hex_ciphertext))

    else:
        decrypted_text = ""
        ciphertext = input("Enter the ciphertext to decrypt: ").upper()
        key = input(f"Enter the key: ").upper()

        if is_hex(ciphertext) == True:
            ciphertext = bytes.fromhex(ciphertext).decode()
        else:
            ciphertext = convert_binary(ciphertext)

        for i in range(len(ciphertext)):
            decrypted_text += chr(ord(ciphertext[i]) ^ ord(key[i]))

        print("Decrypted Text:", decrypted_text)

def monoalphabetic_cipher():
    print("\nMonoalphabetic Cipher\n")

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
                
        print(key)
        print("Encrypted message:", encrypted_message)
    else:
        ciphertext = input("Enter the message to decrypt: ")
        key_str = input("Enter the encryption key as a dictionary: \n")  
        key = ast.literal_eval(key_str)

        print(key)

        reverse_key = {v: k for k, v in key.items()}
        print(reverse_key)
        decrypted_message = ''
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_message += reverse_key[char.upper()].lower()
                else:
                    decrypted_message += reverse_key[char]
            else:
                decrypted_message += char
        print("Decrypted message:", decrypted_message)
