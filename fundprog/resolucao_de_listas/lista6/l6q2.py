from math import inf

funcionarios = []
min_sal = inf
min_sal_func = None
max_sal = -inf
max_sal_func = None

def toBrl(valor):
    return f'R${f"{valor:.2f}".replace(".",",")}'

for i in range(4):
    matricula = input(f'\nDigite o número de matrícula do funcionário {i+1}: ')
    nome = input('Digite o nome do funcionário: ')
    funcao = input('Digite a função exercida pelo funcionário: ')
    salario = input('Digite o salario do funcionário: ')
    reg_func = [matricula, nome, funcao, salario]

    funcionarios.append(reg_func)

for i in funcionarios:
    sal = int(i[3])
    if(sal > max_sal):
        max_sal = sal
        max_sal_func = i[1]

    if(sal < min_sal):
        min_sal = sal
        min_sal_func = i[1]

print()
print('-'*50)
print('Emissão da folha de pagamento: ')
print()

for linha in funcionarios:
    for val in linha:
        print(val, end=' | ')
    print()

print()
print('Maior salário:')
print(f'Funcionário -> {max_sal_func}')
print(f'Valor -> {toBrl(max_sal)}')
print()
print('Menor salário:')
print(f'Funcionário -> {min_sal_func}')
print(f'Valor -> {toBrl(min_sal)}')