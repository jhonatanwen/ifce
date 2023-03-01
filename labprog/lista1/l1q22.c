#include <stdio.h>

int main() {
	char c = ' ';

	printf("Entre um caractere: ");
	scanf("%c", &c);

	printf("Inteiro equivalente a %c: %d\n", c, c);
	// Inteiro equivalente a A: 65
	// Inteiro equivalente a B: 66
	// Inteiro equivalente a C: 67
	// Inteiro equivalente a a: 97
	// Inteiro equivalente a b: 98
	// Inteiro equivalente a c: 99
	// Inteiro equivalente a 0: 48
	// Inteiro equivalente a 1: 49
	// Inteiro equivalente a 2: 50
	// Inteiro equivalente a $: 36
	// Inteiro equivalente a *: 42
	// Inteiro equivalente a +: 43
	// Inteiro equivalente a /: 47
	// Inteiro equivalente a  : 32

	return 0;
}