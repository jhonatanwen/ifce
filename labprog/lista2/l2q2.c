#include <stdio.h>

int main() {
    int dia = 0;

    do {
        printf("Insira um número de 1 a 7 para mostrar o seu equivalente nos dias da semana ou 0 para sair: ");
        scanf("%i", &dia);

        switch (dia) {
            case 1:
                printf("Domingo\n");
                break;
            case 2:
                printf("Segunda-feira\n");
                break;
            case 3:
                printf("Terça-feira\n");
                break;
            case 4:
                printf("Quarta-feira\n");
                break;
            case 5:
                printf("Quinta-feira\n");
                break;
            case 6:
                printf("Sexta-feira\n");
                break;
            case 7:
                printf("Sábado\n");
                break;
            default:
                if(dia == 0){
                    break;
                } else {
                    printf("Número de dia não válido\n");
                    break;
                }
        }
    } while (dia != 0);

    return 0;
}