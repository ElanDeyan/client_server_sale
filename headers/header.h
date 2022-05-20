/*Definições necessárias pelos clientes e servidores */
#define MAX_PATH 255 /*tamanho máximo de nome_arq*/
#define BUF_SIZE 1024 /*dados transferidos*/
#define FILE_SERVER 243 /* endereço do servidor*/
/*Definições de operações permitidas*/
#define CREATE 1 /*cria um novo arquivo*/
#define READ 2 /*lê pedaço de arquivo*/
#define WRITE 3 /*escreve pedaço de arquivo*/
#define DELETE 4 /*apaga arquivo existente*/
/*Códigos de erro*/
#define OK 0 /*operação feita corretamente*/
#define E_BAD_OPCODE -1 /*operação inexistente*/
#define E_BAD_PARAM -2 /*erro em algum parâmetro*/
#define E_IO -3 /*erro de E/S*/

/*Definição do formato da mensagem*/
struct message {
long source; /*identificador da origem*/
long dest; /*identificador do destino*/
long opcode; /*qual operação*/
long count; /*quantidade de bytes*/
long offset; /*onde no arq. começa a operação */
long extra1; /*campo extra*/
long extra2; /*campo extra*/
long result; /*resultado da operação*/
/* valor depende da op. */
char name[MAX_PATH]; /*nome do arquivo*/
char data[BUF_SIZE]; /*dados lidos ou p/ escrever*/
};