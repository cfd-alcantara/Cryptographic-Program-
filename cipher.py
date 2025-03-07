import time
import string

lower_case_letters = string.ascii_lowercase
upper_case_letters = string.ascii_uppercase

def mode_input():
    while True:
        print('Encrypt(E) or Decrypt(D)?')
        mode = input('E/D: ').lower()
        if mode == 'e':
            print('\nEncryption mode\n')
            return mode

        elif mode == 'd':
            print('\nDecryption mode\n')
            return mode
        else:
            print('Invalid input. Input either E for encryption or D for Decryption')
            time.sleep(2)

def ceasar_cipher():
    plain_text = ''
    cipher_text = ''

    print('\nCeasar Cipher\n')
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
        

        
