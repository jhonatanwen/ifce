#include <stdio.h>

int main() {
	int dias = 0;
	float salario_bruto = 0.0, salario_liquido = 0.0, valor_dia = 50.25, gratificacao = 0.0, porcentagem_gratificacao = 0.0, imposto = 0.0, porcentagem_imposto = 1 / 10.0, pagamento = 0.0;

	printf("Entre a quantidade de dias trabalhados: ");
	scanf("%i", &dias);

	if(dias > 20) {
		porcentagem_gratificacao = 3 / 10.0;
	} else if(dias > 10 && dias <= 20) {
		porcentagem_gratificacao = 2 / 10.0;
	}

	pagamento = dias * valor_dia;
	gratificacao = pagamento * porcentagem_gratificacao;
	salario_bruto = pagamento + gratificacao;
	imposto = salario_bruto * porcentagem_imposto;
	salario_liquido = salario_bruto - imposto;

	printf("Seu pagamento foi de R$%.2f\n", pagamento);

	if(dias > 10) {
		printf("Você recebeu uma bonificação de R$%.2f pelo seu bom trabalho\n", gratificacao);
	}

	printf("Sendo assim, seu salário bruto foi de R$%.2f\n", salario_bruto);
	printf("Seu imposto de renda foi igual a R$%.2f\n", imposto);
	printf("Portanto, seu salário líquido foi igual a >>|R$%.2f|<<\n", salario_liquido);

	return 0;
}