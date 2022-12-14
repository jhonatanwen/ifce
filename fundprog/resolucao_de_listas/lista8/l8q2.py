def somaDiagonalMatriz(matriz):
    soma_diagonal = 0
    
    for i in range(len(matriz)):
        soma_diagonal = soma_diagonal + matriz[i][i]
    
    return soma_diagonal

matriz_requisitada = []

for i in range(3):
    linha = []
    
    print(f'\nDigite os valores da linha {i+1} de forma espaçada abaixo.')
    
    if i == 0:
        print('(Ex:-> 3 9 2)')
    
    valslinha = input('-> ').split(' ')
    
    for j in valslinha:
        linha.append(int(j))
    
    matriz_requisitada.append(linha)

print(f'A soma da diagonal da matriz requisitada é {somaDiagonalMatriz(matriz_requisitada)}')