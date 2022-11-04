from random import randint

vetor = []
repetidos = []
repeticoes = 0

for i in range(10):
    vetor.append(randint(-100, 100))

for i in range(len(vetor)):    
    for j in range(i+1, len(vetor)):    
        if(vetor[i] == vetor[j]):
            if(not(vetor[i] in repetidos)):  
                repetidos.append(vetor[j])
            repeticoes = repeticoes + 1
            break

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)
print('Valores repetidos ->', repetidos)
print('Número de repetições ->', repeticoes)
print('-'*50)