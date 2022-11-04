vetorfibo = [1, 1]

for i in range(1,21-len(vetorfibo)):
    soma = vetorfibo[i] + vetorfibo[i-1]
    vetorfibo.append(soma)

print('-'*50*2)
print('', vetorfibo, '')
print('-'*50*2)