#include <stdio.h>

int main() {
	int num0 = 0, num1 = 0;

	printf("Entre dois números: ");
	scanf("%i %i", &num0, &num1);

	printf("%i + %i =  %i\n", num0, num1, num0 + num1);
	printf("%i * %i =  %i\n", num0, num1, num0 * num1);
	printf("%i - %i =  %i\n", num0, num1, num0 - num1);
	printf("quociente da divisão %i / %i =  %i\n", num0, num1, num0 / num1);
	printf("resto da divisão %i / %i =  %i\n", num0, num1, num0 % num1);

	return 0;
}