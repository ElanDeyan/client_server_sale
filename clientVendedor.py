import socket
import time
import json

PORT = 50007
FORMAT = 'utf-8'
SERVER = '127.0.0.1' # '10.0.2.2'
ADDR = (SERVER, PORT)
CLIENT_ID = '1'
class ProcessLeilao:
    nome = ''
    descProduto = ''
    valorInicial = 0

leilao = ProcessLeilao()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send(CLIENT_ID.encode(encoding=FORMAT))

def criar_leilao():
    leilao_as_dict = vars(leilao)
    leilao_string = json.dumps(leilao_as_dict, ensure_ascii=True)
    time.sleep(1)
    client.send(leilao_string.encode(encoding=FORMAT))

def enviar_nome():
    nome = input('Digite o seu nome: ')
    leilao.nome = nome

def enviar_desc_produto():
    desc_produto = input('Digite uma breve descricao de seu produto: ')
    leilao.descProduto = desc_produto

def valor_inicial_produto():
    while(True):
        try:
            valor_inicial = input("Digite um valor inicial para seu produto: ")
            if(float(valor_inicial)):
                valor_inicial = float(valor_inicial)
                leilao.valorInicial = valor_inicial
                break
            else:
                print("Por favor, insira um valor válido.", flush=True)
        except ValueError:
            print("Por favor, insira um valor válido.", flush=True)

def iniciar_leilao():
    enviar_nome()
    enviar_desc_produto()
    valor_inicial_produto()
    criar_leilao()
    print(client.recv(5000000).decode(), flush=True)

def encerrar_leilao():
    server_recv = client.recv(5000000).decode()
    print(server_recv, flush=True)
    while(True):
        if(server_recv.startswith("[ALERTA]")):
            break
        id_to_be_deleted = input()
        time.sleep(0.5)
        if(id_to_be_deleted.isdigit()):
            client.send(id_to_be_deleted.encode(encoding=FORMAT))
            print(client.recv(50000).decode(), flush=True)
            break
        else:
            print("Insira um inteiro válido", flush=True)

def iniciar_vendedor():
    print("Bem-vindo ao leilão\nDeseja criar um novo leilão ou encerrar?")
    while(True):
        try:
            opcao = input("\nDigite 1 para criar\nDigite 2 para encerrar: ")
            opcao = int(opcao)
            if(opcao == 1):
                client.send("CREATE".encode(encoding=FORMAT))
                iniciar_leilao()
            elif(opcao == 2):
                client.send("DELETE".encode(encoding=FORMAT))
                encerrar_leilao()
            else:
                client.send("ERROR".encode(encoding=FORMAT))
                print(client.recv(2048).decode(), flush=True)
        except ValueError:
            client.send("ERROR".encode(encoding=FORMAT))
            print(client.recv(2048).decode(), flush=True)

iniciar_vendedor()