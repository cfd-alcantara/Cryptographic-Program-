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

    plaintext = input("Enter the plaintext to encrypt or decrypt: ").upper()

    key = input(f"Enter the key (length should be {len(plaintext)}): ").upper()

    while len(key) != len(plaintext):
        print(f"The key must be {len(plaintext)} characters long.")
        key = input(f"Enter the key (length should be {len(plaintext)}): ").upper()

    print("Plaintext:", plaintext)
    print("Key:", key)

    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))

    print("Ciphertext:", ciphertext)

    decrypted_text = ""
    for i in range(len(ciphertext)):
        decrypted_text += chr(ord(ciphertext[i]) ^ ord(key[i]))

    print("Decrypted Text:", decrypted_text)



def monoalphabetic_cipher():
    print("\nMonoalphabetic Cipher\n")

    # Generate cipher key
    shift = int(input("Enter the shift value for the cipher (1-25): "))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    key = dict(zip(alphabet, shifted_alphabet))

    mode = mode_input()
    if mode == 'e':
        plaintext = input("Enter the message to encrypt: ")
        encrypted_message = ''
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    encrypted_message += key[char]
                else:
                    encrypted_message += key[char.lower()].upper()
            else:
                encrypted_message += char
        print("Encrypted message:", encrypted_message)
    else:
        ciphertext = input("Enter the message to decrypt: ")
        reverse_key = {v: k for k, v in key.items()}
        decrypted_message = ''
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    decrypted_message += reverse_key[char]
                else:
                    decrypted_message += reverse_key[char.lower()].upper()
            else:
                decrypted_message += char
        print("Decrypted message:", decrypted_message)
