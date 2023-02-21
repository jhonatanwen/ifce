#include <stdio.h>

int main() {
    int num = 0;

    printf("Entre com o valor: ");
    scanf("%i", &num);

    printf("Hexadecimal: %X\n", num);
    printf("Octal: %o\n", num);

    return 0;
}