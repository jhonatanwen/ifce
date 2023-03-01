#include <stdio.h>

int main() {
	int num0 = 0, num1 = 0;

	printf("Entre dois números inteiros de forma espaçada: ");
	scanf("%i %i", &num0, &num1);

	!(num0 % num1)
	?
	printf("O primeiro número é multiplo do segundo\n")
	:
	printf("O primeiro número não é multiplo do segundo\n");

	return 0;
}