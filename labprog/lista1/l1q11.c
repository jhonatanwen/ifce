#include <stdio.h>

int main() {
	float qnt_brl = 0.0, cotacao_usd = 0.0;

	printf("Entre, respectivamente, quanto dinheiro deve ser convertido para dolar e a cotação atual do dolar: ");
	scanf("%f %f", &qnt_brl, &cotacao_usd);

	printf("R$%.2f em dolar: $%.2f", qnt_brl, qnt_brl / cotacao_usd);

	return 0;
}