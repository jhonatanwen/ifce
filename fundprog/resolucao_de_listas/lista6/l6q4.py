tabela_brasileirao = []
campeao = ""
libertadores = ""
copa_sulamericana = ""
rebaixados = ""

for i in range(12):
    timeX = []
    
    print(f'\nDigite os dados do time na posição {i+1} de forma separada por vírgulas abaixo.')
    
    if i == 0:
        print('(Ex:-> L, Time, P, J, V, E, D)')

    dadosTime = input('-> ').split(', ')
    
    for j in dadosTime:
        if j.isnumeric():
            timeX.append(int(j))
        else:
            timeX.append(j)
    
    tabela_brasileirao.append(timeX)

for dados_do_time in tabela_brasileirao:
    if dados_do_time[0] == 1:
        campeao = campeao + dados_do_time[1]
    
    if dados_do_time[0] in [1, 2, 3, 4, 5]:
        if dados_do_time[0] in [1, 2, 3]:
           libertadores = libertadores + f"{dados_do_time[1]}, "
        elif dados_do_time[0] == 4:
           libertadores = libertadores + f"{dados_do_time[1]} e "
        else:
           libertadores = libertadores + dados_do_time[1]
    
    if dados_do_time[0] in [6, 7, 8, 9, 10]:
        if dados_do_time[0] in [6, 7, 8]:
            copa_sulamericana = copa_sulamericana + f"{dados_do_time[1]}, "
        elif dados_do_time[0] == 9:
            copa_sulamericana = copa_sulamericana + f"{dados_do_time[1]} e "
        else:
            copa_sulamericana = copa_sulamericana + dados_do_time[1]

    if dados_do_time[0] in [11, 12]:
        if dados_do_time[0] == 11:
            rebaixados = rebaixados + f"{dados_do_time[1]} e "
        else:
            rebaixados = rebaixados + dados_do_time[1]

print(f"O CAMPEÃO BRASILEIRO é o time do {campeao.upper()}")
print(f"\nOs times convocados para a LIBERTADORES DA AMERICA são os time do {libertadores.upper()}.")
print(f"\nOs times convocados para a COPA SUL AMERICANA são os time do {copa_sulamericana.upper()}.")
print(f"\nOs times que foram REBAIXADOS são os time do {rebaixados.upper()}.")