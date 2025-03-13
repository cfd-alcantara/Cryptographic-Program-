import time
import string
import random
import secrets

def mode_input():
    while True:
        print('Encrypt(E) or Decrypt(D)?')
        mode = input('E/D: ').lower()
        if mode == 'e':
            print('\nEncryption mode')
            return mode

        elif mode == 'd':
            print('\nDecryption mode')
            return mode
        else:
            print('Invalid input. Input either E for encryption or D for Decryption')
            time.sleep(2)

def input_plaintext():
    while True:
        plaintext = input("\nEnter the plaintext to encrypt: ")
        if plaintext == '':
            print('Plaintext is empty')
            time.sleep(2)
        else:
            return plaintext

def input_ciphertext():
    while True:
        ciphertext = input("\nEnter the ciphertext to decrypt: ")
        if ciphertext == '':
            print('Ciphertext is empty')
            time.sleep(2)
        else:
            return ciphertext

def print_encryption_result(plain_text, key, cipher_text):
    print(f'\nPLAINTEXT: {plain_text}')
    print(f'Key: {key}')
    print(f'ENCRYPTED MESSAGE or CIPHERTEXT: {cipher_text}')

def print_decryption_result(cipher_text, key, plain_text):
    print(f'\nCIPHERTEXT: {cipher_text}')
    print(f'Key: {key}')
    print(f'DECRYPTED MESSAGE or PLAINTEXT: {plain_text}')

def is_hex(ciphertext):
    return all(i in string.hexdigits for i in ciphertext)

def convert_binary(ciphertext):
    return ''.join(chr(int(b, 2)) for b in ciphertext.split())

def generate_repeating_key(string, length):
    generated_key = ''.join(random.choice(string) for i in range(length))
    return generated_key

def generate_nonrepeating_key(string, length):
    generated_key = ''.join(secrets.SystemRandom().sample(string, length))
    return generated_key

def expand_key_to_match(plaintext, key):
    key_index = 0
    expanded_key = ''
    for i in range(len(plaintext)):
        expanded_key += key[key_index]
        
        if key_index == len(key)-1:
            key_index = 0
        else:
            key_index += 1

    return expanded_key