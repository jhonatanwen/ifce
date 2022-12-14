cedulas = [2, 5, 10, 20, 50, 100, 200]

def quantasCedulas(saque):
    if not saque.isdigit():
        print('Você só pode sacar dinheiro a partir de 4 reais e de valor cheio')
        return
    if int(saque) < 4:
        print('Você só pode sacar dinheiro a partir de 4 reais e de valor cheio')
        return
    
    cedulas.reverse()
    distribuicao = []
    cedulas_string = ''
    quantidade_de_cedulas = 0
    saque_requisitado = int(saque)
    parcial = 0
    cedulas_novo = [cedula for cedula in cedulas if cedula < saque_requisitado ]

    while True:
        if saque_requisitado - cedulas_novo[0] != 1 and saque_requisitado - cedulas_novo[0] != 3:  
            if saque_requisitado % cedulas_novo[0] == 0:
                distribuicao.append([cedulas_novo[0], int(saque_requisitado / cedulas_novo[0])])
            else:
                i = 0
                j = 1
                parcial = cedulas_novo[0]
                distribuicao.append([cedulas_novo[0], 1])

                while i < len(cedulas_novo):
                    parcial = parcial + cedulas_novo[i]

                    if saque_requisitado - parcial == 1 or saque_requisitado - parcial == 3 or parcial > saque_requisitado:
                        parcial = parcial - cedulas_novo[i]
                        i = i + 1
                        j = 0
                    else:
                        if j == 0:
                            distribuicao.append([cedulas_novo[i], j])
                        
                        j = j + 1
                        distribuicao[distribuicao.index([cedulas_novo[i], j - 1])] = [cedulas_novo[i], j]
               
            break
        else:
            cedulas_novo.pop(0)

    for item in distribuicao:
        cedulas_string = cedulas_string + f'-> {item[1]} cedulas de {item[0]}\n'
        quantidade_de_cedulas = quantidade_de_cedulas + item[1]
    
    print(f'Se a pessoa for sacar {saque} reais, deverá obter {quantidade_de_cedulas} cédulas, sendo:\n{cedulas_string}')

pergunta_saque = input('Quanto você quer sacar?\nR$')

quantasCedulas(pergunta_saque)
