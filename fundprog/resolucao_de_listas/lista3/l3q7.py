for i in range(10):
    pessoa = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa: '))
    altura = float(input('Digite a altura da pessoa: '))
    imc = peso / altura**2
    imc = float(f'{imc:.1f}')

    if(imc >= 40):
        print(f'{pessoa} está com Obesidade Grau III ou Mórbida')
    elif((imc >= 35) and (imc <= 39,9)):
        print(f'{pessoa} está com Obesidade Grau II')
    elif((imc >= 30) and (imc <= 34,9)):
        print(f'{pessoa} está com Obesidade Grau I')
    elif((imc >= 25) and (imc <= 29,9)):
        print(f'{pessoa} está com Sobrepeso')
    elif((imc >= 18,5) and (imc <= 24,9)):
        print(f'{pessoa} está com Peso Normal')
    elif(imc < 19,5):
        print(f'{pessoa} está Abaixo do Peso')
