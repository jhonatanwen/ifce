#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um valor inteiro: ");
	scanf("%i", &num);

	printf("O quadrado de %i: %i\n", num,num * num);

	return 0;
}