#include <stdio.h>

int main() {
	float valor_hora = 0.0, horas_trabalhadas = 0.0, inss = 0.0, porcentagem_inss = 0.0, quant_porcentagem = 0.0, salario_bruto = 0.0, salario_liquido = 0.0;

	printf("Entre o valor hora: ");
	scanf("%f", &valor_hora);
	getchar();

	printf("Entre as horas trabalhadas: ");
	scanf("%f", &horas_trabalhadas);
	getchar();

	printf("Entre quantos porcento seram pedidos no INSS: ");
	scanf("%f", &quant_porcentagem);

	salario_bruto = horas_trabalhadas * valor_hora;
	porcentagem_inss = quant_porcentagem / 100.0;
	inss = salario_bruto * porcentagem_inss;
	salario_liquido = salario_bruto - inss;

	printf("Seu salário bruto foi de R$%.2f\n", salario_bruto);
	printf("Seu salário líquido, descontando o INSS, foi igual a R$%.2f\n", salario_liquido);

	return 0;
}