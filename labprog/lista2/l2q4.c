#include <stdio.h>
#include <math.h>

int main() {
    int altura_inicial_A = 0;
    int altura_inicial_B = 0;
    int crescimento_A = 0;
    int crescimento_B = 0;
    char nome_A[50];
    char nome_B[50];

    printf("Digite, respectivamente, o nome da pessoa mais alta e da pessoa mais baixa, de forma espaçada: ");
    scanf("%s %s", nome_A, nome_B);

    getchar();

    printf("Digite, respectivamente, a altura e crescimento da pessoa mais alta e a altura e crescimento da pessoa mais baixa, espaçadamente em cm: ");
    scanf("%i %i %i %i", &altura_inicial_A, &crescimento_A, &altura_inicial_B, &crescimento_B);

    if(altura_inicial_A < altura_inicial_B) {
        printf("ERRO: A altura da pessoa mais alta está menor do que a altura da pessoa mais baixa\n");
        return -1;
    }

    int anos = (int)floor((double)(altura_inicial_B - altura_inicial_A) / (crescimento_A - crescimento_B)) + 1;

    printf("%s irá ficar maior do que %s em %i anos\n", nome_B, nome_A, anos);

    return 0;
}