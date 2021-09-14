from re import M
import time
from typing import List
import keyboard
from os import read, system
from cryptography.fernet import Fernet

logged = 0
key_delay = 0.2 #delay entre pressionar as teclas
T = L = time.time() #contando tempo entre pressionar as teclas
cad = ["Cadastrar usuário", "cadastrar"]
uncad = ["Excluir usuário", "excluir"]
logoff = ["Fazer logoff", "logoff"]
actions = [cad, uncad, logoff]
mostrador = 0

#Limpa a tela
def clear():
    system('cls')

#criptografia dos logins e senha
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

#Trata os dados de cadastro novo
def crypt_cadastro(Novo):
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
        Lista = temp.read()
    with open("temp.txt", 'w') as temp:
        temp.write("")
    with open("temp.txt", 'w') as temp:
        temp.write(str(Lista))
    with open("temp.txt", 'a') as temp:
        temp.write(Novo)

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

#trata os dados de exclusão de usuário
def crypt_excluir(Novo):
    clear()
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
    del(Lista[Novo+1])
    del(Lista[Novo])
    Lista = '\n'.join(Lista)
    with open("temp.txt", 'w') as temp:
        temp.write(Lista)    

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
    
    print("O usuário foi excluído com sucesso!")
    time.sleep(1)

#criptografia do Menu

#Faz o login com usuário e senha
#falta: implementar hierarquia
def login():
    global logged
    logged = 0
    dados = crypt_login()
    L1 = input("Digite o seu login: ")
    i = 0
    for linhas in dados:
        if L1 == linhas and i%2==0:
            clear()
            print("O usuário é válido!") 
            L2 = input("Digite a senha: ")
            if L2 == dados[i+1]:
                clear()
                print("Bem-vindo(a)", dados[i])
                logged = 1
                time.sleep(1)
                break
            else:           
                clear()
                print("Senha incorreta")
                logged = 3
                break
        i+=1
    if logged==0:
        clear()
        print("Usuário inválido")

#Faz o display da tela
def screen():
    global mostrador, T, L
    clear()
    print('''

        Escolha uma opção:
            {0}
            {1}
            {2}
        '''.format(actions[0][0], actions[1][0], actions[2][0]))
    L = time.time()


    if keyboard.is_pressed("w") and abs(L-T)>=key_delay:
        if mostrador>0:
            actions[mostrador][0]=actions[mostrador][0].replace("-","")
            actions[mostrador-1][0] = "----"+actions[mostrador-1][0]
            mostrador-=1
            T = time.time()
    elif keyboard.is_pressed("s") and abs(L-T)>=key_delay:
        if mostrador<2:
            actions[mostrador][0]=actions[mostrador][0].replace("-","")
            actions[mostrador+1][0] = "----"+actions[mostrador+1][0]
            mostrador+=1
            T = time.time()

#Cadastra um novo usuário
def cadastrar():
    input()
    clear()
    i = input("Deseja cadastrar um novo usuário? s/n ")
    if i == "s" or i == "sim":
        N_login = input("Digite o novo login: ")
        if N_login in crypt_login():
            print("Não é possível cadastrar esse usuário")
            time.sleep(1)
        else:
            N_senha = input("Digite a nova senha: ")
            N_add = "\n" + N_login + "\n" + N_senha
            crypt_cadastro(N_add)
        clear()

#Exclui um usuário existente
def excluir():
    input()    
    clear()
    i = input('Tem certeza que deseja apagar um usuário? s/n\n')
    if i == "s" or i == "sim":
        v = 0
        i = 0
        dados = crypt_login()
        clear()
        Ex_usuario = input("Qual usuário deseja excluir? ")
        for linhas in dados:
            if Ex_usuario == linhas and i%2==0:
                v = 1
                print(dados)
                Ex_senha = input("Qual a senha para este usuário? ")
                if Ex_senha==dados[i+1]:
                    crypt_excluir(i)
                else:
                    print("Senha incorreta")
                    time.sleep(1)
            i+=1
        if v==0:
            print("Nome de usuário incorreto")
            time.sleep(1)
                    
#Encerra o programa
def logoff():
    clear()
    print(" Fazendo logoff...")
    time.sleep(2)
    print(" Obrigado! Até a próxima!")
    time.sleep(2)
    exit()

#Mantém preso enquanto não fizer login
while logged!=1:
    login()

#Main loop
while True:
    screen()
    
    #Verifica tecla de confirmação
    if keyboard.is_pressed("Enter") and abs(T-L)>=key_delay:
        func = locals()[actions[mostrador][1]]
        T = time.time()
        func()
