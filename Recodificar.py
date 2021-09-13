from cryptography.fernet import Fernet

s = int(input('''
    recode = 1
    print = 2
        '''))
if s == 1:
    key = Fernet.generate_key() 
    with open('chave.key', 'wb') as filekey: 
        filekey.write(key)   
    fernet = Fernet(key) 
    with open('Login.txt', 'rb') as data:
        original = data.read()
    encrypted = fernet.encrypt(original) 
    with open('Login.txt', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 
if s == 2:
    with open('chave.key', 'rb') as filekey: 
        key = filekey.read() 
    fernet = Fernet(key) 
    with open('Login.txt', 'rb') as enc_file: 
        encrypted = enc_file.read() 
    original = fernet.decrypt(encrypted)
    print(repr(str(original)))
    input()
