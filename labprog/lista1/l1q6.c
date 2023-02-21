#include <stdio.h>

int main() {
	float altura = 0.0;
	char sexo = '?';

	printf("Entre sua altura em metros e seu sexo[M|m ou F|f] respectivamente: ");
	scanf("%f %c", &altura, &sexo);

	switch(sexo) {
		case 'M':
		case 'm':
			printf("O seu peso ideal é igual a: %.2fkg\n", 72.7 * altura - 58);
			break;
		case 'F':
		case 'f':
			printf("O seu peso ideal é igual a: %.2fkg\n", 62.1 * altura - 44.7);
			break;
		default:
			printf("ERRO: você ou digitou algum caractere fora do esperado ou não digitou nada");
			break;
	}


	return 0;
}