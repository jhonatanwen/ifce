#include <stdio.h>

int main() {
	float volume = 0.0, comprimento = 0.0, largura = 0.0, altura = 0.0;

	printf("Entre, respectivamente, o comprimento, largura e altura da caixa: ");
	scanf("%f %f %f", &comprimento, &largura, &altura);

	volume = comprimento * largura * altura;

	printf("O volume dessa caixa é igual a %.2f u.v.\n", volume);

	return 0;
}