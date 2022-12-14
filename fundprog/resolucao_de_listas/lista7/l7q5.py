def fazerImc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        print(f'Imc............: {imc}')
        print('Classificação..:Magreza')
        print('Obesidade(Grau): 0')
        return
    if imc >= 18.5 and imc < 25:
        print(f'Imc............: {imc}')
        print('Classificação..:Normal')
        print('Obesidade(Grau): 0')
        return
    if imc >= 25 and imc < 30:
        print(f'Imc............: {imc}')
        print('Classificação..:Sobrepeso')
        print('Obesidade(Grau): I')
        return
    if imc >= 30 and imc < 40:
        print(f'Imc............: {imc}')
        print('Classificação..:Obesidade')
        print('Obesidade(Grau): II')
        return
    if imc >= 40:
        print(f'Imc............: {imc}')
        print('Classificação..:Obesidade Grave')
        print('Obesidade(Grau): III')
        return

fazerImc(float(input('Qual seu peso em kg?\n->')), float(input('Qual sua altura, em m?\n->')))