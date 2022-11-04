primos = []

for i in range(10):
    num = int(input('Digite um número inteiro: '))
    serprimo = True
    
    for j in range(2, num):
        if(num % j == 0):
            serprimo = False

    if((serprimo == True) and (num not in primos)):
        primos.append(num)

print(f'Entre os números digitados temos {len(primos)} primo(s), sendo ele(s) o(s) seguinte(s) número(s):\n{primos}')