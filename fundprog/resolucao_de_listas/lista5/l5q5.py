vetor = []
temp = None

for i in range(10, 21):
    vetor.append(i)

for i in range(int(len(vetor) / 2)):
    if(vetor[i] % 2 == 0):
        temp = vetor[i]
        vetor[i] = vetor[len(vetor) - i - 1]
        vetor[len(vetor) - i - 1] = temp

print('-'*50)
print('', vetor, '')
print('-'*50)