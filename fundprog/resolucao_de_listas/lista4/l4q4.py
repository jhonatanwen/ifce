for i in range(6):
    aposentadoria = False
    nome = input('\nDigite o nome do trabalhador: ')
    idade = int(input('Digite a idade do trabalhador: '))
    t_trab = int(input('Digite a quantos anos o trabalhador trabalha: '))
    sexo = input('Digite o sexo do trabalhador: ["m"]Masculino | ["f"]Feminino\n>>>> ')

    match sexo:
        case 'm':
            if((idade >= 65) and (t_trab >= 35)):
                aposentadoria = True
            
            sexo = 'masculino'
        case 'M':
            if((idade >= 65) and (t_trab >= 35)):
                aposentadoria = True
            
            sexo = 'masculino'
        case 'f':
            if((idade >= 60) and (t_trab >= 30)):
                aposentadoria = True
            
            sexo = 'feminino'
        case 'F':
            if((idade >= 60) and (t_trab >= 30)):
                aposentadoria = True
            
            sexo = 'feminino'
        case _:
            print('ERRO: @@@Sexo inválido@@@ !!!O Programa será encerrado!!!')
            exit()

    if(aposentadoria == True):
        print(f'{nome} por ser do sexo {sexo}, ter {idade} anos de idade e ter trabalhado {t_trab} anos está apto(a) para a aposentadoria.')
    else:
        print(f'{nome} por ser do sexo {sexo}, ter {idade} anos de idade e ter trabalhado {t_trab} anos não está apto(a) para a aposentadoria.')
            


