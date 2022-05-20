#include "../headers/header.h"
void main(void)
{
    struct message m1, m2; /* áreas p/mensagens */
    int r;                 /* área p/respostas */
    while (1)
    {
        receive(FILE_SERVER, &m1); /* recebe requisição */
        switch (m1.opcode)
        { /* processa conforme tipo da requisição */
        case CREATE:
            r = do_create(&m1, &m2);
            break;
        case READ:
            r = do_read(&m1, &m2);
            break;
        case WRITE:
            r = do_write(&m1, &m2);
            break;
        case DELETE:
            r = do_delete(&m1, &m2);
            break;
        default:
            r = E_BAD_OPCODE;
        }
        m2.result = r; /* conforme operação */
        send(m1.source, &m2);
    }
}