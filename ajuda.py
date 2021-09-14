from base64 import encode
from re import M
import time
from typing import List
import keyboard
from os import read, system
from cryptography.fernet import Fernet

def crypt_excluir(Novo):
    #Lê o novo arquivo codificado
    with open("chave.key", "rb") as file:
        chave_lida = file.read()
    fernet = Fernet(chave_lida) 
    with open('Login.txt', 'rb') as enc_file: 
        encrypted = enc_file.read() 
    login = fernet.decrypt(encrypted) 

    #Salva as informações como string
    with open("temp.txt", 'w') as temp:
        temp.write(str(login, encoding="utf-8").replace("\r",""))
    with open("temp.txt", 'r') as temp:
        Lista = temp.read().splitlines()
    print(Lista)
    input()    
    Lista = Lista.pop(Novo+1)
    Lista = Lista.pop(Novo)
    print(Lista)
    input()
    Lista = '\n'.join(Lista)
    with open("temp.txt", 'w') as temp:
        temp.write(Lista)
    print(Lista)
    input()

    #Codifica e salva no Login
    key = Fernet.generate_key() 
    with open('chave.key', 'wb') as filekey: 
        filekey.write(key)   
    fernet = Fernet(key) 
    with open('temp.txt', 'rb') as data:
        original = data.read()
    encrypted = fernet.encrypt(original) 
    with open('Login.txt', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 

    #Limpa memória temporária
    with open("temp.txt", 'w') as temp:
        temp.write("")

def excluir():
    input()    
    i = input('Tem certeza que deseja apagar um usuário? s/n\n')
    if i == "s" or i == "sim":
        v = 0
        dados = crypt_login()
        Ex_usuario = input("Qual usuário deseja excluir? ")
        for linhas in dados:
            if Ex_usuario == linhas and i%2==0:
                v = 1
                Ex_senha = input("Qual a senha para este usuário? ")
                if Ex_senha==dados[i+1]:
                    crypt_excluir(i)
                else:
                    print("Senha incorreta")
                    time.sleep(1)
                i+=1
        if v==0:
            print("Nome de usuário inválido")
            time.sleep(1)

def crypt_login():
    #Lê o arquivo atual e decodifica com a chave
    with open('chave.key', 'rb') as filekey: 
        key = filekey.read() 
    fernet = Fernet(key) 
    with open('Login.txt', 'rb') as enc_file: 
        encrypted = enc_file.read() 
    original = fernet.decrypt(encrypted)

    #gera uma nova chave e recodifica o arquivo
    key = Fernet.generate_key() 
    with open('chave.key', 'wb') as filekey: 
        filekey.write(key)   
    fernet = Fernet(key) 
    encrypted = fernet.encrypt(original) 
    with open('Login.txt', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 

    #Lê o novo arquivo codificado
    with open("chave.key", "rb") as file:
        chave_lida = file.read()
    fernet = Fernet(chave_lida) 
    with open('Login.txt', 'rb') as enc_file: 
        encrypted = enc_file.read() 
    login = fernet.decrypt(encrypted) 

    #Salva as informações como string
    with open("temp.txt", 'w') as temp:
        temp.write(str(login, encoding="utf-8").replace("\r",""))
    with open("temp.txt", 'r') as temp:
        Lista = temp.read().splitlines()
    with open("temp.txt", 'w') as temp:
        temp.write("")
    return Lista

N_add = ['ghiguti', 'gustavo']
excluir()

input()