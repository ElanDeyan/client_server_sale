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
dados_leilao = []


def criar_leilao():
    leilao_as_dict = vars(leilao)
    leilao_string = json.dumps(leilao_as_dict)
    print(leilao_string)
    time.sleep(10)
    client.send(leilao_string.encode(encoding=FORMAT))

def enviar_nome():
    nome = input('Digite o seu nome: ')
    # criar_lista_leilao("nome=" + nome)
    leilao.nome = nome

def enviar_produto():
    produto = input('Digite o nome do produto a leiloar: ')
    # criar_lista_leilao("produto=" + produto)
    leilao.produto = produto

def enviar_desc_produto():
    desc_produto = input('Digite uma breve descricao de seu produto: ')
    #criar_lista_leilao("desc_produto=" + desc_produto)
    leilao.descProduto = desc_produto

def valor_inicial_produto():
    while(True):
        valor_inicial = float(input("Digite um valor inicial para seu produto: "))
        if(type(valor_inicial) == float):
            #criar_lista_leilao(f"valor_inicial={valor_inicial}")
            leilao.valorInicial = f"valor_inicial={valor_inicial}"
            break
        else:
            print("Por favor, insira um valor válido.")

def iniciar_leilao():
    enviar_nome()
    enviar_produto()
    enviar_desc_produto()
    valor_inicial_produto()
    criar_leilao()


def iniciar():
    thread1 = threading.Thread(target=iniciar_leilao)
    thread1.start()

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