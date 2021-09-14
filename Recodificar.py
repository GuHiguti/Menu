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
    with open("temp.txt", 'w') as temp:
        temp.write(str(original, encoding="utf-8").replace("\r",""))
    with open("temp.txt", 'r') as temp:
        bonito = temp.read().splitlines()
    with open("temp.txt", 'w') as temp:
        temp.write("")
        
    print("\n\t", end="")
    print(repr(str(original)))    
    print("\n\t", end="")
    print(bonito)
    print("\n\t", end="")
    print("\n\t".join(bonito))
    input()
