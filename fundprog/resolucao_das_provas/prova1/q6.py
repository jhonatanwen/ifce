from math import inf

def fgts(salario, t):
    return salario * (8.5 / 100) * t

def toBrl(valor):
    return f'R${f"{valor:.2f}".replace(".",",")}'

func_fgts = []
max_sal = -inf
index_max = 0
min_sal = inf
index_min = 0

for i in range(5):
    sal = int(input(f'\nDigite o salário do funcionário {i+1}: '))
    
    func_fgts.append([sal, fgts(sal, 1)])
    
    print(f'\nO valor do fgts do funcionário {i+1} é de {toBrl(fgts(sal,1))}')

for i in range(len(func_fgts)):
    if(func_fgts[i][0] > max_sal):
        max_sal = func_fgts[i][0]
        index_max = i
    if(func_fgts[i][0] < min_sal):
        min_sal = func_fgts[i][0]
        index_min = i
    
print(f'\nO menor valor do fgts dos funcionários é o do funcionário {index_min+1} com o valor de de {toBrl(func_fgts[index_min][1])};')
print(f'O maior valor do fgts dos funcionários é o do funcionário {index_max+1} com o valor de de {toBrl(func_fgts[index_max][1])};')
print(f'\nA diferença de valor do maior valor de fgts e o menor em um intervalo de 1 ano é de {toBrl(fgts(func_fgts[index_max][0], 12)-fgts(func_fgts[index_min][1], 12))}, sendo {toBrl(fgts(func_fgts[index_max][0], 12))} o fgts de maior valor e {toBrl(fgts(func_fgts[index_min][0], 12))} o de menor valor')