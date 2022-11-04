from random import randint

vetor = []
valor = int(input('Digite um número e veja se ele está dentro do vetor randomico: '))

for i in range(10):
    vetor.append(randint(-100, 100))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

if(valor in vetor):
    print(f'O número {valor} está presente no vetor e tem posição inicial igual a: {vetor.index(valor)}')
else:
    print(f'O número {valor} não está presente no vetor')

print('-'*50)