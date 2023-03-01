#include <stdio.h>
#include <math.h>

int main() {
	float num0 = 0.0, num1 = 0.0, num2 = 0.0;
	float media_aritmetica = 0.0, media_geometrica = 0.0;

	printf("Entre 3 números com ponto flutuante, espaçadamente: ");
	scanf("%f %f %f", &num0, &num1, &num2);

	media_aritmetica = (num0 + num1 + num2) / 3.0;
	media_geometrica = pow(num0 * num1 * num2, 1 / 3.0);

	printf("Média aritmética dos 3 números: %f\n", media_aritmetica);
	printf("Média geometrica dos 3 números: %f\n", media_geometrica);

	return 0;
}