# Referenced: https://www.mankier.com/1/pycryptodome#API_Documentation-CBC_mode

import sys
import base64
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(key, iv, ptext):
    aes_encrypt = AES.new(key, AES.MODE_CBC, iv=iv)
    return base64.b64encode(aes_encrypt.encrypt(pad(ptext, AES.block_size))).decode('utf-8')


def decrypt(key, iv, ctext):
    aes_decrypt = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(aes_decrypt.decrypt(base64.b64decode(ctext)), AES.block_size).decode('utf-8')


def validate_key(key):
    if len(key) != 16 and len(key) != 24 and len(key) != 32:
        print('Invalid Key size')
        return False


def validate_iv(iv):
    if len(iv) != 16:
        print('Invalid IV size')
        return False


valid = False

while valid is False:
    key = getpass(prompt='Key: ').encode('utf-8')
    valid = validate_key(key)

valid = False

while valid is False:
    iv = getpass(prompt='IV: ').encode('utf-8')
    valid = validate_iv(iv)

choice = ''

while True:
    choice = input('Encrypt (1) / Decrypt (2) / \"Quit\" to quit: ')

    if choice == 'quit':
    	sys.exit(0)
    elif int(choice) < 1 or int(choice) > 2:
    	continue
    else:
	    data = input('Text: ').encode('utf-8')
	    if int(choice) == 1:
	        ciphertext = encrypt(key, iv, data)
	        print(ciphertext)
	    elif int(choice) == 2:
	        plaintext = decrypt(key, iv, data)
	        print(plaintext)