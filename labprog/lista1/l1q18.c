#include <stdio.h>

int main() {
	const float pi = 3.14159;
	float raio = 0.0, area = 0.0, diametro = 0.0, circunferencia = 0.0;

	printf("Entre o raio do círculo: ");
	scanf("%f", &raio);

	diametro = 2 * raio;
	circunferencia = pi * diametro;
	area = pi * raio * raio;

	printf("Diametro do circulo: %f u.m.\n", diametro);
	printf("Circunferência do circulo: %f u.m.\n", circunferencia);
	printf("Área do circulo: %f u.a.\n", area);

	return 0;
}