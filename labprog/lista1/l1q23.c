#include <stdio.h>

int main() {
	int num = 0;
	char numStr[4], invNumStr[4];


	printf("Entre um número de 3 digitos: ");
	scanf("%i", &num);

	sprintf(numStr, "%i", num);
	sprintf(invNumStr, "%c%c%c", numStr[2], numStr[1], numStr[0]);

	printf("O valor %s ao ser invertido fica igual a: %s\n", numStr, invNumStr);

	return 0;
}