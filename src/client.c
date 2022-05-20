#include <header.h>
int copy(char *src, char *dst)
{
    struct message m1; /* msg para/do servidor */
    long position;     /* posição de leitura */
    long client = 110; /* quem envia */
    initialize();
    position = 0; /* inicia leitura no 1o byte */
    do
    {
        /*Lê um bloco de dados do arquivo origem*/
        m1.opcode = READ;       /* prepara mensagem */
        m1.offset = position;   /* 1o byte: ajustado por read */
        m1.count = BUF_SIZE;    /* quantos bytes */
        strcpy(&m1.name, src);  /* nome arq. */
        send(FILE_SERVER, &m1); /* envia req. */
        receive(client, &m1);   /* recebe resp. */
        /*grava um bloco de dados no arquivo destino*/
        m1.opcode = WRITE;
        m1.offset = position;
        m1.count = m1.result; /* result = # bytes */
        strcpy(&m1.name, dst);
        send(FILE_SERVER, &m1);
        receive(client, &m1);
        position += m1.result; /* result = # bytes */
    } while (m1.result > 0);   /* zero: nada foi lido */
    /* retorna “ok” ou erro */
    return (m1.result >= 0 ? OK : m1.result);
}