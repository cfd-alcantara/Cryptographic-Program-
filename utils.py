import time
import string
import random
import secrets

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