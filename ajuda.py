from base64 import encode
from re import M
import time
import keyboard
from os import read, system
from cryptography.fernet import Fernet

with open('chave.key', 'rb') as filekey: 
    key = filekey.read() 
fernet = Fernet(key) 
with open('Login.txt', 'rb') as enc_file: 
    encrypted = enc_file.read() 
original = fernet.decrypt(encrypted)
print(repr(original))
print(type(original))
original = str(original)[:-1]+"\\r\\ngabriela'"
print(repr(original))
print(type(original))
original = original.replace("b", "")
original = original.replace("'","")
print(repr(original))
print(type(original))
original = bytes(original, encoding="utf-8")
print(repr(original))
print(type(original))
input()
'''encrypted = fernet.encrypt(original)
with open('Login.txt', 'wb') as encrypted_file: 
    encrypted_file.write(encrypted) 

input()

with open('chave.key', 'rb') as filekey: 
    key = filekey.read() 
fernet = Fernet(key) 
with open('Login.txt', 'rb') as enc_file: 
    encrypted = enc_file.read() 
original = fernet.decrypt(encrypted)
print(str(original))
input()'''