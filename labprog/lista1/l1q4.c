#include <stdio.h>
#include <math.h>

int main() {
	int num = 0;

	printf("Entre com um valor inteiro: ");
	scanf("%i", &num);

	printf("O triplo de %i: %i\n", num, num * 3);
	printf("O quadrado de %i: %d\n", num, num * num);
	printf("O meio de %i: %.2f\n", num, num / 2.0);

	return 0;
}