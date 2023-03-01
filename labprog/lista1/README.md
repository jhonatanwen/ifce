<p align="center">
  <a href="#questão-1">1</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-2">2</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-3">3</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-4">4</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-5">5</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-6">6</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-7">7</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-8">8</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-9">9</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-10">10</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-11">11</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-12">12</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-13">13</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-14">14</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-15">15</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-16">16</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-17">17</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-18">18</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-19">19</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-20">20</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-21">21</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-22">22</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-23">23</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-24">24</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-25">25</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-26">26</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#questão-27">27</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

# 📚 Lista 01 - Programação em C

Lista de exercícios submetida na cadeira de Laboratório de Programação.

## Questão 1:

Diga a ordem de cálculo dos operadores em cada uma das instruções em C a seguir e mostre o valor de x depois que cada instrução for executada.

```
-> Primeiro é feito a operação do operador "*" depois o do operador "/" por último é são feitas respectivamente as operações dos operadores "+" e "-".
Passo a passo e resultado:
x = 7 + 3 * 6 / 2 - 1;
x = 7 + 18 / 2 - 1;
x = 7 + 9 - 1;
x = 16 - 1;
x = 15;

-> Primeiro é feito a operação com operador "%" depois disso é feita a operação com o operador "*" e então a operação com o operador "/", por fim são feitas as operações respectivamente dos operadores "+" e "-".
Passo a passo e resultado:
x = 2 % 2 + 2 * 2 - 2 / 2;
x = 0 + 2 * 2 - 2 / 2;
x = 0 + 4 - 2 / 2;
x = 0 + 4 - 1;
x = 4 - 1;
x = 3;

-> Primeiro são feitas as operações dentro de um operador "()", no caso, por termos operadores "()" dentro deles o mais interno vem primeiro, após isso é feito a ordem de dos operadores "*" e "/", sendo que o primeiro a ser feito é o que está mais a direita, mas, igualmente aos outros casos acima, irá ser feito primeiro a operação do operador "*" e depois a do operador "/", por último a do operador "+".
Passo a passo e resultado:
x = (3 * 9 * (3 + (9 * 3 / (3))));
x = (3 * 9 * (3 + (9 * 3 / 3)));
x = (3 * 9 * (3 + (27 / 3)));
x = (3 * 9 * (3 + (9)));
x = (3 * 9 * (3 + 9));
x = (3 * 9 * (12));
x = (3 * 9 * 12);
x = (27 * 12);
x = (324);
x = 324;
```

## Questão 2:

Faça um programa que leia um valor inteiro decimal X e escreva, na tela, este mesmo valor nas bases
hexadecimal e octal.

```c
#include <stdio.h>

int main() {
    int num = 0;

    printf("Entre com o valor: ");
    scanf("%i", &num);

    printf("Hexadecimal: %X\n", num);
    printf("Octal: %o\n", num);

    return 0;
}
```

## Questão 3:

Faça um programa capaz de ler um valor real e escreve-lo com apenas uma casa decimal.

```c
#include <stdio.h>

int main() {
    float num = 0;

    printf("Entre com um valor real: ");
    scanf("%f", &num);

    printf("O valor escrito como inteiro é igual a %i", (int)num);

    return 0;
}
```

## Questão 4:

Faça um programa capaz de ler um valor inteiro X e escrever seu triplo, seu quadrado, e seu meio.

```c
#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre com um valor inteiro: ");
	scanf("%i", &num);

	printf("O triplo de %i: %i\n", num, num * 3);
	printf("O quadrado de %i: %d\n", num, num * num);
	printf("O meio de %i: %.2f\n", num, num / 2.0);

	return 0;
}
```

## Questão 5:

Escreva um programa que pegue o valor de uma conta de restaurante e imprima o valor total a ser pago, considerando que o restaurante cobra 10% de taxa para o garçom.

```c
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
```

## Questão 6:

Fazer um programa para ler a altura (em metros) e o sexo de uma pessoa e calcular o seu peso ideal atraves da seguinte formula:

- para homens: 72.7 \* altura - 58
- para mulheres: 62.1 \* altura - 44.7

```c
#include <stdio.h>

int main() {
	float altura = 0.0;
	char sexo = '?';

	printf("Entre sua altura em metros e seu sexo[M|m ou F|f] respectivamente: ");
	scanf("%f %c", &altura, &sexo);

	switch(sexo) {
		case 'M':
		case 'm':
			printf("O seu peso ideal é igual a: %.2fkg\n", 72.7 * altura - 58);
			break;
		case 'F':
		case 'f':
			printf("O seu peso ideal é igual a: %.2fkg\n", 62.1 * altura - 44.7);
			break;
		default:
			printf("ERRO: você ou digitou algum caractere fora do esperado ou não digitou nada");
			break;
	}


	return 0;
}
```

## Questão 7:

Faça um programa que leia uma quantidade de horas, minutos e segundos e imprima o total de segundos.

```c
#include <stdio.h>

int main() {
	int horas = 0, minutos = 0, segundos = 0;

	printf("Entre as horas, minutos e segundos que você quer converter(no formato H M S): ");
	scanf("%i %i %i", &horas, &minutos, &segundos);

	printf("O tempo entrado convertido em segundos: %i\n", horas * 60 * 60 + minutos * 60 + segundos);

	return 0;
}
```

## Questão 8:

Escreva um programa que receba um valor inteiro e apresente o resultado do valor lido elevado ao quadrado.

```c
#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um valor inteiro: ");
	scanf("%i", &num);

	printf("O quadrado de %i: %i\n", num,num * num);

	return 0;
}
```

## Questão 9:

Escreva um programa que leia um valor numerico inteiro e apresente como resultado os seus valores sucessor e antecessor.

```c
#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um número: ");
	scanf("%i", &num);

	printf("O valor %i tem como sucessor o valor %i e antecessor o valor %i\n", num, num + 1, num - 1);

	return 0;
}
```

## Questão 10:

Escreva um programa que calcule e apresente o valor do volume de um caixa retangular utilizando a formula

- VOLUME = COMPRIMENTO _ LARGURA _ ALTURA.

```c
#include <stdio.h>

int main() {
	float volume = 0.0, comprimento = 0.0, largura = 0.0, altura = 0.0;

	printf("Entre, respectivamente, o comprimento, largura e altura da caixa: ");
	scanf("%f %f %f", &comprimento, &largura, &altura);

	volume = comprimento * largura * altura;

	printf("O volume dessa caixa é igual a %.2f u.v.\n", volume);

	return 0;
}
```

## Questão 11:

Elabore um programa que apresente o valor da conversao em dolar de um valor lido em real. O programa deve solicitar o valor da cotaçao do dlar e tambem a quantidade de reais que o usuario deseja converter.

```c
#include <stdio.h>

int main() {
	float qnt_brl = 0.0, cotacao_usd = 0.0;

	printf("Entre, respectivamente, quanto dinheiro deve ser convertido para dolar e a cotação atual do dolar: ");
	scanf("%f %f", &qnt_brl, &cotacao_usd);

	printf("R$%.2f em dolar: $%.2f", qnt_brl, qnt_brl / cotacao_usd);

	return 0;
}
```

## Questão 12:

Escreva um programa que pe ca ao usuario para digitar dois numeros, obtenha-os do usuario e imprima a soma, o produto, a diferenca, o quociente e o resto da divisao dos dois numeros.

```c
#include <stdio.h>

int main() {
	int num0 = 0, num1 = 0;

	printf("Entre dois números: ");
	scanf("%i %i", &num0, &num1);

	printf("%i + %i =  %i\n", num0, num1, num0 + num1);
	printf("%i * %i =  %i\n", num0, num1, num0 * num1);
	printf("%i - %i =  %i\n", num0, num1, num0 - num1);
	printf("quociente da divisão %i / %i =  %i\n", num0, num1, num0 / num1);
	printf("resto da divisão %i / %i =  %i\n", num0, num1, num0 % num1);

	return 0;
}
```

## Questão 13:

Escreva um programa que leia duas variaveis A e B e efetue a troca dos valores. O objetivo é que a variavel A passe a conter o valor de B e a variavel B passe a possuir o valor de A. Apresente os valores apos a efetivacao do processamento da troca.

```c
#include <stdio.h>

int main() {
	int a = 0, b = 0, temp = 0;

	printf("Digite o valor da variável A: ");
	scanf("%i", &a);
	getchar();

	printf("Digite o valor da variável B: ");
	scanf("%i", &b);

	temp = a, a = b, b = temp;

	printf("Os valores de A e B trocaram-se entre si\n");
	printf("A = %i\n", a);
	printf("B = %i\n", b);

	return 0;
}
```

## Questão 14:

Escreva um programa que leia uma temperatura em graus Celsius e apresente convertida em graus Fahrenheit.

- F = (9 \* C + 160) / 5

```c
#include <stdio.h>

int main() {
	int celsius = 0;

	printf("Entre uma temperatura em Celsius: ");
	scanf("%i", &celsius);

	printf("A temperatura em Fahrenheit: %.1fF", (9 * celsius + 160) / 5.0);

	return 0;
}
```

## Questão 15:

Uma empresa contrata um vendedor a R$ 50,25 por dia. Crie um programa que solicite o numero de dias trabalhados pelo vendedor e imprima o valor lıquido a ser pago ao mesmo

- sabendo que se ele trabalhou ate 10 dias nao tem direito a gratificaçao, se ele trabalhou acima de 10 dias e ate 20 dias tem direito a gratificacao de 20%, se ele trabalhou acima de 20 dias tem direito a gratificacao de 30%.

- Sempre sao descontados 10% de imposto de renda em cima do valor bruto.

```c
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
```

## Questão 16:

Desenvolva um programa que calcule o salario liquido de um professor. Para elaborar o programa, é necessario possuir alguns dados, tais como o

- valor da hora aula n
- numero de horas trabalhadas no mes
- percentual de desconto do INSS.

Em primeiro lugar, deve-se estabelecer o seu salario bruto para fazer o desconto e ter o valor do salario liquido.
Obs.: o programa deve informar o salario bruto e salarioliquido do professor.

```c
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
```

## Questão 17:

Escrever um programa que receba um valor inteiro do usuario e apresente o seu valor absoluto (modulo). _Nao utilize estrutura de decisao if_

```c
#include <stdio.h>

int main() {
	int num = 0, absolut_num;

	printf("Entre um número inteiro: ");
	scanf("%i", &num);

	absolut_num = num >= 0 ? num : -num;

	printf("O valor absoluto desse número é: %i", absolut_num);

	return 0;
}
```

## Questão 18:

Escreva um programa que leia o raio de um cırculo e imprima seu diametro, o valor de sua circunferencia e sua area.

- Use o valor de 3,14159 para ”pi”.

```c
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
```

## Questão 19:

Escreva um programa que imprima um retˆangulo, uma elipse, uma seta e um losango.

```c
#include <stdio.h>

int main() {
	printf("********\t    ***\t\t  *\t\t*\n");
	printf("*      *\t *\t*\t ***\t      *   *\n");
	printf("*      *\t*\t *\t*****\t     *     *\n");
	printf("*      *\t*\t *\t  *\t    *\t    *\n");
	printf("*      *\t*\t *\t  *\t   *\t     *\n");
	printf("*      *\t*\t *\t  *\t    *\t    *\n");
	printf("*      *\t*\t *\t  *\t     *     *\n");
	printf("*      *\t *\t*\t  *\t      *   *\n");
	printf("********\t   ***\t\t  *\t\t*\n");

	return 0;
}
```

## Questão 20:

Escreva um programa que receba um numero inteiro e entao determine e imprima se ele e par ou ımpar. _Não utilizar estrutura de decisao if_

```c
#include <stdio.h>

int main() {
	int num = 0;

	printf("Entre um número inteiro: ");
	scanf("%i", &num);

	!(num % 2)
	?
	printf("O número que você entrou é par\n")
	:
	printf("O número que você entrou é impar\n");

	return 0;
}
```

## Questão 21:

Escreva um programa que leia dois inteiros e entao determine e imprima se o primeiro é múltiplo do segundo. _Não utilizar estrutura de decisao if_

```c
#include <stdio.h>

int main() {
	int num0 = 0, num1 = 0;

	printf("Entre dois números inteiros de forma espaçada: ");
	scanf("%i %i", &num0, &num1);

	!(num0 % num1)
	?
	printf("O primeiro número é multiplo do segundo\n")
	:
	printf("O primeiro número não é multiplo do segundo\n");

	return 0;
}
```

## Questão 22:

Escreva um programa em C que imprima os inteiros equivalentes a algumas letras maiusculas, letras minusculas e sımbolos especiais. No minimo, determine os numeros inteiros equivalentes ao conjunto seguinte: A B C a b c 0 12 $ \* + / e o caractere espaço em branco.

```c
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
```

## Questão 23:

Escreva um programa que receba a entrada de um numero de três digitos, separe o número em seus digitos componentes e reconstrua um numero com os componentes na ordem inversa.

- Exemplo: para entrada de 123, a resposta do programa seria 321.

```c
#include <stdio.h>

int main() {
	int num = 0;
	char numStr[4], invNumStr[4];


	printf("Entre um número de 3 digitos: ");
	scanf("%i", &num);

	sprintf(numStr, "%i", num);
	sprintf(invNumStr, "%c%c%c", numStr[2], numStr[1], numStr[0]);

	printf("O valor %s ao ser invertido fica igual a: %s\n", numStr, invNumStr);

	return 0;
}
```

## Questão 24:

Escreva um programa que calcule o produto entre um valor dado x por 2 elevado a um valor dado n. _Utilize operadores biarios_

```c
#include <stdio.h>

int main() {
	int x = 0, n = 0, result = 0;

	printf("Entre os dois valores x e n, respectivamente, espaçadamente: ");
	scanf("%i %i", &x, &n);

	result = x << n;

	printf("Sendo x = %i e n = %i temos que x * 2^n = %i", x, n, result);

	return 0;
}
```

## Questão 25:

Escreva um programa que leia um tempo em segundos e imprima quantas horas, minutos e segundos ha neste tempo.

```c
#include <stdio.h>

int main() {
	int segundos, horas, minutos, segundos_restantes;

	printf("Digite o tempo em segundos: ");
	scanf("%d", &segundos);

	segundos_restantes = segundos % 60;
	minutos = (segundos / 60) % 60;
	horas = segundos / 3600;

	printf("%d segundos equivalem a %d horas, %d minutos e %d segundos\n", segundos, horas, minutos, segundos_restantes);

	return 0;
}
```

## Questão 26:

Fazer um programa para ler as coordenadas x e y de dois pontos e calcular a distancia entre os doispontos no plano.

```c
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
```

## Questão 27:

Escreva um programa que solicite 3 numeros em ponto flutuante e imprima a média aritmetica e geometrica.

```c
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
```
