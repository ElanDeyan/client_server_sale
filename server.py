import socket
import threading
import json

SERVER_IP = '127.0.0.1'
PORT = 50007
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

leiloes = []
id_leilao = 0

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
                    leilao_dados["maior_lance"] = leilao_dados["valorInicial"]
                    leilao_dados["email_vencedor"] = ""
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
                    if(leilao["estado_leilao"] == "Aberto"):
                        leiloes_list += f"{leilao}\n"
                print(leiloes_list)
                if(leiloes_list == ''):
                    msg = "Não há leiloes disponíveis"
                else:
                    msg = leiloes_list
                conn.send(msg.encode(encoding=FORMAT))
            elif(client_op == "UPDATE"):
                leilao_encontrado = ''
                leiloes_list = ''
                for leilao in leiloes:
                    if(leilao["estado_leilao"] == "Aberto"):
                        leiloes_list += f"{leilao}\n"
                if(leiloes_list == ''):
                    msg = "Não temos leilões disponíveis"
                else:
                    msg = leiloes_list
                conn.send(msg.encode(encoding=FORMAT))
                id_lance = conn.recv(2048).decode()
                id_lance = int(id_lance)
                for leilao in leiloes:
                    if(leilao["id"] == id_lance and leilao["estado_leilao"] == "Aberto"):
                        leilao_encontrado = leilao
                        break
                    else:
                        conn.send("Insira id entre os apresentados".encode(encoding=FORMAT))
                conn.send("Certo, agora diga-me o lance a fazer".encode(encoding=FORMAT))
                msg = ''
                while(True):
                    valor_lance = conn.recv(2048).decode()
                    valor_lance = float(valor_lance)
                    if(valor_lance < leilao_encontrado["valorInicial"]):
                        conn.send("Por favor, faça um lance igual ou maior que o lance mínimo".encode(encoding=FORMAT))
                    else:
                        if(valor_lance > leilao_encontrado["maior_lance"]):
                            leilao_encontrado["maior_lance"] = valor_lance
                            msg = "É o maior lance até o momento!\nQual seu email para que, quando acabar, possamos entrar em contato?"
                            conn.send(msg.encode(encoding=FORMAT))
                            email_vencedor = conn.recv(4096).decode()
                            leilao_encontrado["email_vencedor"] = email_vencedor
                            conn.send("Dados recebidos e cadastrados! Obrigado".encode(encoding=FORMAT))
                        elif(valor_lance == leilao_encontrado["maior_lance"]):
                            msg = "É igual ao maior lance, o anterior ainda fica com o título quando encerrarem."
                            conn.send(msg.encode(encoding=FORMAT))
                        else:
                            msg = "É menor que o maior lance..."
                            conn.send(msg.encode(encoding=FORMAT))
                        break
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