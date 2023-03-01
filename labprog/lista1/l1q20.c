#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um número inteiro: ");
	scanf("%i", &num);

	!(num % 2)
	?
	printf("O número que você entrou é par\n")
	:
	printf("O número que você entrou é impar\n");

	return 0;
}