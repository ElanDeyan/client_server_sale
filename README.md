# client_server_sale

Objetivo: Construir um aplicativo de Leilão com o uso de Sockets.

Usei como base para a aplicação um vídeo no YouTube que mostra o desenvolvimento de um chat usando Sockets na linguagem de programação Python. Link colocado na seção “Referências”.
Fui estabelecendo o funcionamento do leilão e fazendo pesquisas até chegar no resultado final.

## Requerimentos mínimos:

- Linguagem de programação: Python, versão em meu notebook verificada às 16:16 do dia 9/6/22 - 3.10.0

- Conseguir executar arquivos .py através do terminal de comando.

- Bibliotecas importadas no Código-Fonte: ‘socket’, ‘threading’, ‘json’, ‘time’.

- Sistema operacional: Indiferente, desde que possa executar o código em Python, de preferência na versão 3.10.0. Foram feitos testes com os seguintes sistemas: Windows 11 (executando o server.py) e Linux Mint Cinammon 64-bit Edge e Fedora Workstation Live 36. Não sei definir se precisa ser algum específico.

- Software para máquina virtual: Foi utilizado o Oracle VM VirtualBox para criar as máquinas virtuais. Não sei se outro software geraria algum impasse...

- Caso não queira utilizar com máquina virtual, pode substituir as linhas SERVER = '10.0.2.2' no código dos clientes por 
```python
SERVER = '127.0.0.1'
```
Instruções para a instalação:

1)Instale o python na sua versão atual através do site oficial.
Caso já tenha o python instalado, verfique sua versão e, se possível, atualize.

2)Copie o código fonte e os coloque em 3 arquivos diferentes, um para o servidor, um para o comprador e um para o vendedor. Os códigos-fonte também estão disponíveis no link para o google drive na seção “Referências”.

3)A aplicação deve começar com o servidor primeiro e depois os clientes.

4)Para a execução dos arquivos, abra a pasta que contém os 3 arquivos e abra o terminal de comando nessa pasta, ou use o comando cd para navegar até esse diretório. Use o comando python3 ‘nome_do_arquivo.py’, por exemplo, python3 server.py , para iniciar a execução do arquivo, nesse exemplo, o servidor. Da mesma maneira para com os clientes em suas respectivas máquinas virtuais.

5)Use sua máquina hospedeira para executar o servidor, que estará conectado no endereço ‘127.0.0.1’ e na porta 50007. Ele aguardará as conexões que virão.

6)Não tenho muita certeza, mas, caso nas máquinas virtuais esteja utilizando distribuições linux, execute o comando sudo ufw disable ,  para desabilitar o firewall. 

7)Agora, você pode criar duas máquinas virtuais diferentes e executá-las apenas depois que o Servidor em seu hospedeiro estiver executando. Cada um dos clientes está sendo conectado no endereço ‘10.0.2.2’ e na porta 50007.

8)Siga as instruções apresentadas na tela. Os clientes escolherão entre as opções apresentadas na tela e poderão inserir os devidos dados. Haverão tomadas de decisão virão a partir de opções enumeradas. Exemplo, “Digite 1 para criar um leilão.” “Por favor, diga o id do artigo que deseja fazer um lance:” E assim por diante.

Referências:

- Tutorial de Socket com Python - Guia Completo de Soquetes. Disponível em: https://youtu.be/VhhNlWdLPzA
- Código-Fonte no meu google-drive: https://drive.google.com/drive/folders/1JxkT380-sRd24cinz3yYmFc_Tpb-T1vD?usp=sharing 
- Link para StackOverflow onde cita o ‘10.0.2.2’. Disponível em: https://stackoverflow.com/questions/48138413/how-to-connect-through-socket-to-virtual-machine 
