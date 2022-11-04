reg_funcionarios = {}
maior_hora_key = None
maior_hora = 0
hrs_mensais = 40 * 4
salario_mensal = int(input('Digite o salário dos funcionários: '))

for i in range(10):
    funcionario = input('\nDigite o nome do funcionário: ')
    hrs_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
    valor_hr = salario_mensal / hrs_mensais
    salario = salario_mensal

    if(hrs_trabalhadas > hrs_mensais):
        salario += (hrs_trabalhadas - hrs_mensais) * valor_hr * 1.5
    elif(hrs_trabalhadas < hrs_mensais):
        salario = valor_hr * hrs_trabalhadas
        
    
    salario = f'{salario:.2f}'.replace('.',',')
    
    print(f'\n{funcionario} receberá R${salario} esse mês.')

    reg_funcionarios[funcionario] = hrs_trabalhadas

for key, i in reg_funcionarios.items():
    if(int(i) > maior_hora):
        maior_hora = i
        maior_hora_key = key

print(f'{maior_hora_key} foi o funcionário com maior quantidade de horas trabalhadas com {maior_hora}hrs.')

