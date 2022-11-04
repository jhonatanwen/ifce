from random import randint

vetor = []
par = 0
impar = 0

for i in range(10):
    vetor.append(randint(-100, 100))

for i in vetor:
    if(i % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)
print('Número de valores pares ->', par)
print('Número de valores impares ->', impar)
print('-'*50)