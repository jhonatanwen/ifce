ano = int(input('Digite um ano: '))
bissexto = False

if(ano % 400 == 0):
    bissexto = True
elif(ano % 100 == 0):
    bissexto = False
elif(ano % 4 == 0):
    bissexto = True
else:
    bissexto = False

if(bissexto):
    print(f'O ano {ano} é bissexto')
else:
    print(f'{ano} não é bissexto')