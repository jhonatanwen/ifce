#include <stdio.h>

int main() {
	int horas = 0, minutos = 0, segundos = 0;

	printf("Entre as horas, minutos e segundos que você quer converter(no formato H M S): ");
	scanf("%i %i %i", &horas, &minutos, &segundos);

	printf("O tempo entrado convertido em segundos: %i\n", horas * 60 * 60 + minutos * 60 + segundos);

	return 0;
}