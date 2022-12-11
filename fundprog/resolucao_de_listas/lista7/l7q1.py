#1. Faça uma função em python para ler uma data válida (P.ex.: 12 de junho de 2010) e informar quantos dias já se passaram desta data, considerando o ano com 365 dias e o mês com 30 dias.
from datetime import date

hoje = date.today()
hoje_list = str(hoje).split('-')

for i in range(len(hoje_list)):
    hoje_list[i] = int(hoje_list[i])

hoje_em_dias = (hoje_list[0] - 1) * 365 + (hoje_list[1] - 1) * 30 + hoje_list[2]
data_requisitada = input('Digite a data ao qual você quer saber quantos dias se passaram desde esse dia até hoje: ')

def quantosDias(data):
    data_em_dias = None
    data_list = None

    if '-' in data:
        data_list = str(data).split('-')
    elif '/' in data:
        data_list = str(data).split('/')
    elif '.' in data:
        data_list = str(data).split('.')
    else:
        data_list = str(data).split(' de ')
        data_list[1] = data_list[1].lower()

        match data_list[1]:
            case 'janeiro':
                data_list[1] = 1
            case 'fevereiro':
                data_list[1] = 2
            case 'março':
                data_list[1] = 3
            case 'abril':
                data_list[1] = 4
            case 'maio':
                data_list[1] = 5
            case 'junho':
                data_list[1] = 6
            case 'julho':
                data_list[1] = 7
            case 'agosto':
                data_list[1] = 8
            case 'setembro':
                data_list[1] = 9
            case 'outubro':
                data_list[1] = 10
            case 'novembro':
                data_list[1] = 11
            case 'dezembro':
                data_list[1] = 12
        
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    
    data_em_dias = data_list[0] + (data_list[1] - 1) * 30 + (data_list[2] - 1) * 365

    return hoje_em_dias - data_em_dias


print(f'Já se passaram {quantosDias(data_requisitada)} dias dessa data.')

        

