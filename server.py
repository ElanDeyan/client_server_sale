import socket
import threading
import time
import json

SERVER_IP = '127.0.0.1' # socket.gethostbyname(socket.gethostname())
PORT = 50007
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class ProcessLeilao:
    id_leilao = 0
    nome = ''
    produto = ''
    descProduto = ''
    valorInicial = 0

conexoes = []
mensagens = []

def iniciar_leilao():
    pass

def enviar_mensagem_individual(connection):
    print(f"[ENVIANDO] Enviando mensagem para {connection['addr']}")
    for i in range(connection['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        connection['conn'].send(mensagem_de_envio.encode(FORMAT))
        connection['last'] = i + 1
        time.sleep(0.5)

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)

def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario entrou com o endereco '{addr}'")
    global conexoes
    global mensagens
# Primeira vez que entrar, o cliente manda o nome e dps as mensagens
    while(True):
        # msg = conn.recv(2048).decode()
        leilao_encoded = conn.recv(2048)
        leilao_string = leilao_encoded.decode(encoding=FORMAT)
        leilao_dados = json.loads(leilao_string)
        print(leilao_dados)
        if(leilao_dados):
            if(leilao_dados.nome.startswith("nome=")):
                mensagem_separada = leilao_dados.nome.split("=")
                nome = mensagem_separada[1]
                conexao_map = { "conn": conn, "addr": addr, "nome": nome, "last": 0 }
                conexoes.append(conexao_map)
                enviar_mensagem_individual(conexao_map)
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()

def start():
    print('[INICIANDO] Iniciando Socket...')
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()