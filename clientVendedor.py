import socket
import threading
import time
import json

# Link pra enviar objeto entre sockets
# https://stackoverflow.com/questions/47391774/send-and-receive-objects-through-sockets-in-python


PORT = 50007
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)

class ProcessLeilao:
    nome = ''
    produto = ''
    descProduto = ''
    valorInicial = 0

leilao = ProcessLeilao()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
#! dados_leilao = []


def criar_leilao():
    leilao_as_dict = vars(leilao)
    leilao_string = json.dumps(leilao_as_dict)
    print(leilao_string)
    time.sleep(10)
    client.send(leilao_string.encode(encoding=FORMAT))

def enviar_nome():
    nome = input('Digite o seu nome: ')
    leilao.nome = nome

def enviar_produto():
    produto = input('Digite o nome do produto a leiloar: ')
    leilao.produto = produto

def enviar_desc_produto():
    desc_produto = input('Digite uma breve descricao de seu produto: ')
    leilao.descProduto = desc_produto

def valor_inicial_produto():
    while(True):
        valor_inicial = float(input("Digite um valor inicial para seu produto: "))
        if(type(valor_inicial) == float):
            leilao.valorInicial = valor_inicial
            break
        else:
            print("Por favor, insira um valor válido.")

def iniciar_leilao():
    enviar_nome()
    enviar_produto()
    enviar_desc_produto()
    valor_inicial_produto()
    criar_leilao()
    print(client.recv(2048).decode())


def iniciar():
    print("Bem-vindo ao leilão\nDeseja criar um novo leilão ou encerrar?")
    while(True):
        opcao = int(input("Digite 1 para criar\nDigite 2 para encerrar: "))
        if(opcao == 1):
            iniciar_leilao()
        elif(opcao == 2):
            print("Ainda não disponível")
        else:
            print("Por favor escolha uma das opcoes acima")
    #thread1 = threading.Thread(target=iniciar_leilao)
    #thread1.start()

iniciar()

# comentário
"""
def handle_mensagens():
    while(True):
        msg = client.recv(2048).decode()
        mensagem_split = msg.split("=")
        print(mensagem_split[1] + ": " + mensagem_split[2])
"""
"""
def enviar_mensagem():
    while(True):
        mensagem = input()
        enviar("msg=" + mensagem)
"""