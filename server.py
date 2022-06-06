import time
import socket
import threading
import json

SERVER_IP = '127.0.0.1' # socket.gethostbyname(socket.gethostname())
PORT = 50007
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

leiloes = []
id_leilao = 0

#TODO: Ajustar para responder aquilo que o cliente pedir
"""
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
"""

def handle_clientes(conn, addr):
    client_type = conn.recv(64).decode()
    client_type = int(client_type)
    global id_leilao
    if(client_type == 1):
        print(f"[NOVA CONEXAO] Um novo usuario entrou com o endereco '{addr}'")
        print("Cliente eh vendedor")
        while(True):
            client_op = conn.recv(64).decode()
            print(client_op,flush=True)
            if(client_op == "CREATE"):
                leilao_encoded = conn.recv(5000000)
                leilao_string = leilao_encoded.decode()
                leilao_dados = json.loads(leilao_string)
                if(leilao_dados):
                    conn.send(f"Recebido!\nO indice de seu produto eh {id_leilao}".encode(encoding=FORMAT))
                    leilao_dados["id"] = id_leilao
                    leilao_dados["id_address"] = addr[1]
                    leilao_dados["estado_leilao"] = "Aberto"
                    leiloes.append(leilao_dados)
                    tabela = ''
                    for item in leiloes:
                        tabela += f"{item}\n"
                    print(tabela)
                id_leilao += 1
            elif(client_op == "DELETE"):
                if(len(leiloes) == 0):
                    conn.send("[ALERTA] Não há leilões existentes, quer criar um?".encode(encoding=FORMAT))
                else:
                    leiloes_cliente_array = []
                    leiloes_cliente = 'Certo! Estes são os leilões que você enviou:\n'
                    for leilao in leiloes:
                        if(leilao["id_address"] == addr[1] and leilao["estado_leilao"] == "Aberto"):
                            leiloes_cliente_array.append(leilao)
                            leiloes_cliente += f"{leilao}\n"
                    if(leiloes_cliente != 'Certo! Estes são os leilões que você enviou:\n'):
                        leiloes_cliente += "\nPor favor, diga o id correspondente do produto."
                        conn.send(leiloes_cliente.encode(encoding=FORMAT))
                        id_leilao_del = conn.recv(64).decode()
                        id_leilao_del = int(id_leilao_del)
                        msg = ''
                        for leilao_cliente in leiloes_cliente_array:
                            if(leilao_cliente["id"] == id_leilao_del):
                                leiloes[id_leilao_del]["estado_leilao"] = "Encerrado"
                                msg = f"Leilão encerrado!\n{leilao_cliente}"
                                break
                            else:
                                msg = "Id não encontrado em sua lista de leiloes"
                        conn.send(msg.encode(encoding=FORMAT))
                    else:
                        conn.send("[ALERTA] Não encontrei nenhum leilão em aberto criado por você.".encode(encoding=FORMAT))
            else:
                conn.send("Operação inexistente".encode(encoding=FORMAT))
    elif(client_type == 2):
        print(f"[NOVA CONEXAO] Um novo usuario entrou com o endereco '{addr}'")
        print("Cliente eh comprador")
        while(True):
            client_op = conn.recv(64).decode()
            print(client_op,flush=True)
            if(client_op == "READ"):
                leiloes_list = ''
                for leilao in leiloes:
                    leiloes_list += f"{leilao}\n"
                print(leiloes_list)
                conn.send(leiloes_list.encode(encoding=FORMAT))
            elif(client_op == "UPDATE"):
                leilao_encontrado = ''
                leiloes_list = ''
                for leilao in leiloes:
                    leiloes_list += f"{leilao}\n"
                conn.send(leiloes_list.encode(encoding=FORMAT))
                id_lance = conn.recv(2048).decode()
                id_lance = int(id_lance)
                for leilao in leiloes:
                    if(leilao["id"] == id_lance and leilao["estado_leilao"] == "Aberto"):
                        leilao_encontrado = leilao
                        break
                    else:
                        conn.send("Insira id entre os apresentados".encode(encoding=FORMAT))
                conn.send("Certo, agora diga-me o lance a fazer".encode(encoding=FORMAT))
                conn.recv(2048).decode()
            else:
                conn.send("Operação inexistente".encode(encoding=FORMAT))
    else:
        print("Algo deu errado com a identificação do cliente")
def start():
    print('[INICIANDO] Iniciando Socket...')
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()
"""
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
"""