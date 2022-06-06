import socket
import threading
import time
import json

PORT = 50007
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
CLIENT_ID = '2'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send(CLIENT_ID.encode(encoding=FORMAT))

def ver_lances():
    print(client.recv(500000000).decode(), flush=True)

def fazer_lance():
    print(client.recv(500000000).decode(), flush=True)
    while(True):
        try:
            id_lance = input("Por favor, diga o id do artigo que deseja fazer um lance: ")
            if(id_lance.isdigit()):
                client.send(id_lance.encode(encoding=FORMAT))
                break
        except ValueError:
            print(client.recv(2048).decode(), flush=True)
    print(client.recv(4096).decode(), flush=True)

def iniciar_comprador():
    print("Bem-vindo ao leilão\nDeseja ver os leilões em aberto ou fazer um lance?")
    while(True):
        try:
            opcao = input("\nDigite 1 para ver leilões\nDigite 2 para fazer um lance: ")
            opcao = int(opcao)
            if(opcao == 1):
                client.send("READ".encode(encoding=FORMAT))
                ver_lances()
            elif(opcao == 2):
                client.send("UPDATE".encode(encoding=FORMAT))
                fazer_lance()
            else:
                client.send("ERROR".encode(encoding=FORMAT))
                print(client.recv(2048).decode(), flush=True)
        except ValueError:
            client.send("ERROR".encode(encoding=FORMAT))
            print(client.recv(2048).decode(), flush=True)

iniciar_comprador()