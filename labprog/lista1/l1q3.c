#include <stdio.h>

int main() {
    float num = 0;

    printf("Entre com um valor real: ");
    scanf("%f", &num);

    printf("O valor escrito como inteiro é igual a %i", (int)num);

    return 0;
}