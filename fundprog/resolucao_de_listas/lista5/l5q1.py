from random import randint

vetor = []

for i in range(10):
    vetor.append(randint(-100, 100))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

vetor.sort()

print('Vetor ordenado de forma crescente ->', vetor)

vetor.sort(reverse=True)

print('Vetor ordenado de forma decrescente ->', vetor)
print('-'*50)