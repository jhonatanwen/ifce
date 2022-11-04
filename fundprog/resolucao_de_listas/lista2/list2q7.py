print('Saiba qual mês é pelo número')

mes = input('Digite o número do mês: ')
meses = {'1': 'Janeiro', 
        '2': 'Fevereiro', 
        '3': 'Março', 
        '4': 'Abril', 
        '5': 'Maio', 
        '6': 'Junho', 
        '7': 'Julho', 
        '8': 'Agosto', 
        '9': 'Setembro', 
        '10': 'Outubro', 
        '11': 'Novembro', 
        '12': 'Dezembro'}

if mes in meses:
    print(meses[mes])
else:
    print('Número/Mensagem corresponde a um Mês Inválido')