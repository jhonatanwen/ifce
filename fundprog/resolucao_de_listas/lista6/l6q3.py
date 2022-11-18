def printMatriz(matriz):
    for linha in matriz:
        print('| ', end='')
        for val in linha:
            print(val, end=' ')
        print('|')
    print()


matriz = []

print('Vamos verificar se uma matriz quadrada é um quadrado mágico!')
print('\nDigite abaixo o tamanho da matriz quadrada que você quer verificar.')

tamanho = int(input('-> '))

for i in range(tamanho):
    linha = []
    
    print(f'\nDigite os valores da linha {i+1} de forma espaçada abaixo.')
    if i == 0:
        print('(Ex:-> 3 9 2)')
    
    valslinha = input('-> ').split(' ')
    
    for j in valslinha:
        linha.append(int(j))    
    
    matriz.append(linha)

diagonais = 0
colunas = 0
linhas = 0
sdp = 0
sdc = 0
sl = 0
sl_temp = 0
sc = 0
sc_temp = 0

for i in range(tamanho):
    sdp = sdp + matriz[i][i]
    sdc = sdc + matriz[i][tamanho-i-1]
    
    for j in range(tamanho):
        sl_temp = sl_temp + matriz[i][j]
        sc_temp = sc_temp + matriz[j][i]
    
    if i == 0:
        sl = sl_temp
        sc = sc_temp
    else:
        if sl == sl_temp:
            linhas = sl
        else:
            linhas = -1
            break
        if sc == sc_temp:
            colunas = sc
        else:
            colunas = -2
            break

    sl_temp = 0
    sc_temp = 0

if sdp == sdc:
    diagonais = sdp

print('\nMatriz inserida:')
printMatriz(matriz)

if(diagonais == colunas) and (diagonais == linhas):
    print('É uma matriz QUADRADO MÁGICO')
else:
    print('NÃO é uma matriz QUADRADO MÁGICO')