#include <stdio.h>

int main() {
	float conta = 0.0, taxa = 1 / 10.0, total = 0.0;

	printf("Entre o valor da conta: ");
	scanf("%f", &conta);

	total = conta + conta * taxa;

	printf("ATENÇÃO: A sua conta de R$%.2f terá um adicional de 10%% pelo serviço, sendo esse valor de R$%.2f!\n", conta, conta * taxa);
	printf("VALOR DA CONTA: R$%.2f\nTAXA DE SERVIÇO: R$%.2f +\n__________________\nTOTAL: R$%.2f", conta, conta * taxa, total);

	return 0;
}