def exponencial2(n = int(input('Qual o valor do expoente da exponenciação?\n->'))):
    if n == 0:
        return 1

    return 2 * exponencial2(n - 1)

print(f'Valor da exponenciação: {exponencial2()}')