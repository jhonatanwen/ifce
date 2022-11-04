habitante = []
menor_sal = 0
soma0 = 0
soma1 = 0

for i in range(5):
    salario = int(input('\nDigite o salário do habitante: '))
    filhos = int(input("Digite quantos filhos o habitante tem: "))
    if(salario < 1000):
        menor_sal += 1
    habitante.append([salario, filhos])

for i in habitante:
    soma0 += i[0]
    soma1 += i[1]

media_salarial = soma0 / len(habitante)
media_filhos = soma1 / len(habitante)
percentual = menor_sal / len(habitante) * 100

print('\nNessa cidade temos três dados quanto aos habitantes:')
print(f'>>>>> Média Salárial..............: {"R${0:.2f}".format(media_salarial).replace(".",",")}')
print(f'>>>>> Média de filhos.............: {media_filhos}')
print(f'>>>>> Percentual de Salário Baixo.: {percentual}%')
    