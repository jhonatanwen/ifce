#include <stdio.h>

int main() {
	int a = 0, b = 0, temp = 0;

	printf("Digite o valor da variável A: ");
	scanf("%i", &a);
	getchar();

	printf("Digite o valor da variável B: ");
	scanf("%i", &b);

	temp = a, a = b, b = temp;

	printf("Os valores de A e B trocaram-se entre si\n");
	printf("A = %i\n", a);
	printf("B = %i\n", b);

	return 0;
}