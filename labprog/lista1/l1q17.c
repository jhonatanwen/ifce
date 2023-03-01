#include <stdio.h>

int main() {
	int num = 0, absolut_num;

	printf("Entre um número inteiro: ");
	scanf("%i", &num);

	absolut_num = num >= 0 ? num : -num;

	printf("O valor absoluto desse número é: %i", absolut_num);

	return 0;
}