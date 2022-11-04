from random import randint

vetor = []
primos = []

for i in range(10):
    vetor.append(randint(1, 200))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

for i in vetor:
    if(i != 1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            primos.append(i)

print('Primos no vetor ->', primos)
print('-'*50)
