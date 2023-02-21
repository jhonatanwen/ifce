#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um número: ");
	scanf("%i", &num);

	printf("O valor %i tem como sucessor o valor %i e antecessor o valor %i\n", num, num + 1, num - 1);

	return 0;
}