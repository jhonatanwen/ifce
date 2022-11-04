from datetime import date
from math import inf

idades = {}
menor_idade = inf
maior_idade = -inf
menor_idade_key = None
maior_idade_key = None
ano_atual = date.today().year
     
def idade(aniver):
    if(aniver):
        return ano_atual - ano_nasc
    else:
        return ano_atual - ano_nasc - 1

for i in range(10):
    nome = input('Digite o nome e sobrenome da pessoa: ')
    ano_nasc = int(input('Em que ano a pessoa nasceu? '))
    niver = input('A pessoa já fez aniversário? Responda com "S" ou "N" ')
    
    if(niver == 'S'):
        fez_niver = True
    elif(niver == 'N'):
        fez_niver = False
    else:
        print('!!!!ERRO!!!!')
        
        exit()
    
    idades[nome] = idade(fez_niver)

    print(f'{nome} tem {idades[nome]}')

for key, i in idades.items():
    if(int(i) > maior_idade):
        maior_idade = i
        maior_idade_key = key

for key, i in idades.items():
    if(int(i) < menor_idade):
        menor_idade = i
        menor_idade_key = key

print(f'Dessas pessoas, {maior_idade_key} tem a maior idade com seus {maior_idade} anos e {menor_idade_key} tem a menor idade com seus {menor_idade} aninhos.')