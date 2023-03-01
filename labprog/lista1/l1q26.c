#include <stdio.h>
#include <math.h>

int main() {
	int x1, x2, y1, y2;
	double d;

	printf("Entre dois pontos de valor inteiro no plano cartesiano de forma espaçada e seguindo a forma (x,y): ");
	scanf("(%i,%i) (%i,%i)", &x1, &y1, &x2, &y2);

	d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

	printf("A distância do ponto (%i,%i) para o (%i,%i) é de %.2f", x1, y1, x2, y2, d);

	return 0;
}