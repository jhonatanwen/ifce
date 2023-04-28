#include <stdio.h>

int main() {
    int F = 0;

    printf("Digite um inteiro positivo para ver seu fatorial: ");
    scanf("%i", &F);

    int F_copy = F;
    int range = F;

    if(F < 0) {
        printf("ERRO: você digitou um número negativo!\n");
        return -1;
    }

    if(F == 0) F = 1;

    for(int i = 0; i < range; i++) {
        if(F == 1) break;
        if(F_copy > 1) {
            F_copy -= 1;
            F *= F_copy;
        }
    }

    printf("O Fatorial de %lu\n", (long)F);

    return 0;
}