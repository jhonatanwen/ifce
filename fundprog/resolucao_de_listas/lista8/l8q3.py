from math import inf

print(f'\nDigite os valores do vetor de forma espaçada abaixo.')
    
vetor_requisitado = input('-> ').split(' ')

for i in range(len(vetor_requisitado)):
    vetor_requisitado[i] = int(vetor_requisitado[i])

def maiorValorVetor(vetor, i = 0, maior = -inf):
    if i >= len(vetor):
        return maior
    if vetor[i] > maior:
        maior = vetor[i]

    return maiorValorVetor(vetor, i + 1, maior)


print(f'Maior valor do vetor requisitado: {maiorValorVetor(vetor_requisitado)}')
