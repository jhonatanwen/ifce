#include <stdio.h>

int main() {
	int x = 0, n = 0, result = 0;

	printf("Entre os dois valores x e n, respectivamente, espaçadamente: ");
	scanf("%i %i", &x, &n);

	result = x << n;

	printf("Sendo x = %i e n = %i temos que x * 2^n = %i", x, n, result);

	return 0;
}