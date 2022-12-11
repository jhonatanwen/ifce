from math import inf

matriz_requisitada = []

def maiorColunaMenorLinha(matriz):
    maior_coluna_lista = None
    menor_linha_lista = None
    soma_das_colunas = []
    soma_das_linhas = []
    maior_coluna = -inf
    menor_linha = inf

    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma = soma + matriz[i][j]
        
        soma_das_linhas.append([i+1, soma])
    
    for j in range(len(matriz)):
        soma = 0
        for i in range(len(matriz)):
           soma = soma + matriz[i][j]
        
        soma_das_colunas.append([j+1, soma])

    for soma in soma_das_colunas:
        if(soma[1] > maior_coluna):
            maior_coluna = soma[1]
            maior_coluna_lista = soma

    for soma in soma_das_linhas:
        if(soma[1] < menor_linha):
            menor_linha = soma[1]
            menor_linha_lista = soma
    
    return [maior_coluna_lista, menor_linha_lista]

for i in range(3):
    linha = []
    
    print(f'\nDigite os valores da linha {i+1} de forma espaçada abaixo.')
    
    if i == 0:
        print('(Ex:-> 3 9 2)')
    
    valslinha = input('-> ').split(' ')
    
    for j in valslinha:
        linha.append(int(j))
    
    matriz_requisitada.append(linha)

maior_coluna = maiorColunaMenorLinha(matriz_requisitada)[0]
menor_linha = maiorColunaMenorLinha(matriz_requisitada)[1]

print(f'Maior coluna......: {maior_coluna[0]}')
print(f'Soma da coluna....: {maior_coluna[1]}')
print(f'Menor linha.......: {menor_linha[0]}')
print(f'Soma da linha.....: {menor_linha[1]}')