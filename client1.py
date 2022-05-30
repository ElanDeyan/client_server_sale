import socket
import threading
import time

PORT = 50007
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def handle_mensagens():
    while(True):
        msg = client.recv(2048).decode()
        mensagem_split = msg.split("=")
        print(mensagem_split[1] + ": " + mensagem_split[2])

def enviar(mensagem):
    client.send(mensagem.encode(FORMAT))

def enviar_mensagem():
    while(True):
        mensagem = input()
        enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite o seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

iniciar()