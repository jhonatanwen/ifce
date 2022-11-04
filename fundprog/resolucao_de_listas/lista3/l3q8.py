from math import inf

salarios = {}
soma = 0
menor_salario = inf
maior_salario = -inf
menor_salario_key = None
maior_salario_key = None

def imposto(porcentagem):
    return salario_bruto * (porcentagem/100)

for i in range(10):
    funcionario = input('Digite o nome do funcionário: ')
    salario_bruto = int(input('Digite o salário do funcionário: '))

    print('\nQuanto ao imposto de renda:')
    
    if(salario_bruto > 2000):
        print(f'    O imposto de renda de {funcionario} será de R${imposto(15):.2f}'.replace('.',','))
        
        salario_liquido = salario_bruto - float(f'{imposto(15):.2f}')
    elif((salario_bruto > 1500) and (salario_bruto <= 2000)):
        print(f'    O seu imposto de renda de {funcionario} será de R${imposto(10):.2f}'.replace('.',','))
        
        salario_liquido = salario_bruto - float(f'{imposto(10):.2f}')
    elif(salario_bruto <= 1500):
        print(f'    {funcionario} está isento de imposto de renda')
        
        salario_liquido = salario_bruto

    print(f'\nQuanto ao salário líquido:\n    O salário líquido de {funcionario} é R${salario_liquido:.2f}\n'.replace('.',','))

    salarios[funcionario] = salario_bruto
    
for key, i in salarios.items():
    if(int(i) > maior_salario):
        maior_salario = i
        maior_salario_key = key
    if(int(i) < menor_salario):
        menor_salario = i
        menor_salario_key = key
    
    soma += int(i)

media_salarial = soma / len(salarios)
media_salarial = f'{media_salarial:.2f}'.replace('.', ',')

print(f'Com as informações coletadas dos funcionários temos que a média salarial é de R${media_salarial} onde temos que:\n    {maior_salario_key} recebe o maior salário, sendo esse igual a R${maior_salario},00\n    {menor_salario_key} recebe o menor salário, sendo esse igual a R${menor_salario},00')