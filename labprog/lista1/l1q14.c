#include <stdio.h>

int main() {
	int celsius = 0;

	printf("Entre uma temperatura em Celsius: ");
	scanf("%i", &celsius);

	printf("A temperatura em Fahrenheit: %.1fF", (9 * celsius + 160) / 5.0);

	return 0;
}