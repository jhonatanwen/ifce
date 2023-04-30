#include <stdio.h>
#include <string.h>

int main() {
    char candidato_n5[] = "Pedro", candidato_n7[] = "Renata";
    int voto = 0, votos_candidato_n5 = 0, votos_candidato_n7 = 0, votos_brancos = 0, votos_nulos = 0;

    while(voto >= 0) {
        int resposta = 0;

        printf("Insira o número do candidato em que quer votar: ");
        scanf("%i", &voto);
        getchar();

        switch (voto) {
            case 5:
                printf("Você tem certeza que quer votar no candidato(a) %s?\n1 - SIM\n2 - NÃO\n>>>>> ", candidato_n5);
                scanf("%i", &resposta);
                getchar();

                if(resposta == 1) {
                    printf("Seu voto foi contabilizado.\n\n");
                    votos_candidato_n5++;
                }

                if(resposta != 1) {
                    printf("Seu voto foi cancelado. Tente novamente.\n\n");
                }

                break;
            case 7:
                printf("Você tem certeza que quer votar no candidato(a) %s?\n1 - SIM\n2 - NÃO\n>>>>> ", candidato_n7);
                scanf("%i", &resposta);
                getchar();

                if(resposta == 1) {
                    printf("Seu voto foi contabilizado.\n\n");
                    votos_candidato_n7++;
                }

                if(resposta != 1) {
                    printf("Seu voto foi cancelado. Tente novamente.\n\n");
                }
                break;
            case 0:
                printf("Você tem certeza que quer votar em branco?\n1 - SIM\n2 - NÃO\n>>>>> ");
                scanf("%i", &resposta);
                getchar();

                if(resposta == 1) {
                    printf("Seu voto foi contabilizado.\n\n");
                    votos_brancos++;
                }

                if(resposta != 1) {
                    printf("Seu voto foi cancelado. Tente novamente.\n\n");
                }

                break;
            default:
                if(voto >= 0) {
                    printf("O número que você digitou não existe\n\n");
                    printf("Ele será contato como voto nulo.\nVocê tem certeza que quer votar nulo?\n1 - SIM\n2 - NÃO\n>>>>> ");
                    scanf("%i", &resposta);
                    getchar();

                    if(resposta == 1) {
                        printf("Seu voto foi contabilizado.\n\n");
                        votos_nulos++;
                    }

                    if(resposta != 1) {
                        printf("Seu voto foi cancelado. Tente novamente.\n\n");
                        getchar();
                    }

                    break;
                }

                printf("Votação encerrada.\n\n");
                break;
        }
    }

    char vencedor[50];
    double total = (double) votos_candidato_n5 + votos_candidato_n7 + votos_brancos + votos_nulos;
    double porcentagem_n5 = (votos_candidato_n5 * 100.0) / total;
    double porcentagem_n7 = (votos_candidato_n7 * 100.0) / total;
    double porcentagem_brancos = (votos_brancos * 100.0) / total;
    double porcentagem_nulos = (votos_nulos * 100.0) / total;

    if(votos_candidato_n5 > votos_candidato_n7) strcpy(vencedor, candidato_n5);
    if(votos_candidato_n7 > votos_candidato_n5) strcpy(vencedor, candidato_n7);
    if(votos_candidato_n5 == votos_candidato_n7) strcpy(vencedor, "EMPATE");

    printf("[PORCENTAGENS]\n");

    printf("%s - %.1f%%\n%s - %.1f%%\nBranco - %.1f%%\nNulos - %.1f%%\n\n", candidato_n5, porcentagem_n5, candidato_n7, porcentagem_n7, porcentagem_brancos, porcentagem_nulos);

    printf("[RESULTADO]\n");

    if(votos_candidato_n5 == votos_candidato_n7) printf("O(A) vencedor(a) é %s!\n", vencedor);
    if(votos_candidato_n5 != votos_candidato_n7) printf("%s\n", vencedor);

    return 0;
}