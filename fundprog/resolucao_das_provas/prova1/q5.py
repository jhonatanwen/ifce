def Consumo(percuso):
    return percuso / 12

percurso1 = int(input('Digite a quantidade de km do primeiro percurso: '))
percurso2 = int(input('Digite a quantidade de km do segundo percurso: '))

if(percurso1 < percurso2):
    consumo = f'{Consumo(percurso1):.2f}'
    print(f'O primeiro percuso vai ter menor consumo sendo ele igual a {consumo}l')
elif(percurso2 < percurso1):
    consumo = f'{Consumo(percurso2):.2f}'
    print(f'O segundo percuso vai ter menor consumo sendo ele igual a {consumo}l')
else:
    consumo = f'{Consumo(percurso1):.2f}'
    print(f'Os dois percusos são iguais, logo o consumo será igualmente de {consumo}l')
