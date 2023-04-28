#include <stdio.h>

int main() {
    int digito = 0;
    int maior_num = 0;
    int menor_num = 0;
    int num = 0;

    for(;;) {
        printf("Digite um número qualquer (digite '0' para sair): ");
        scanf("%i", &num);
        getchar();

        if(maior_num != 0 && menor_num != 0) digito = num;
        if(num != 0 && digito == 0) maior_num = menor_num = num;
        if(num == 0 && digito == 0) break;
        if(num > maior_num) maior_num = num;
        if(num < menor_num) menor_num = num;

        printf("O maior número atualmente fornecido é: %i\n", maior_num);
        printf("O menor número atualmente fornecido é: %i\n", menor_num);
    }

    return 0;
}