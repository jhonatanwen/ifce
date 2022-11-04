from math import inf, pi
from datetime import date
from random import randint

print('Tabuada de 1, 2 e 3')

for i in range(1,4):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}')

R = float(input('Digite o raio da esfera para calcular o volume: '))
V = (4 * pi * R ** 3) / 3

print(f'O volume da esfera é {V:.2f} u.v.')

value = int(input('Digite um número inteiro para verificar se é par ou impar: '))

if(value % 2 == 0):
    print(f'O número {value} é par.')
else:
    print(f'O número {value} é impar.')

print('Descubra qual número é o maior entre três.')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
nums = [n1, n2, n3]
maxn = -inf

for n in nums:
    if(n > maxn):
        maxn = n

print(f'O maior número é {maxn}')

print('Descubra a diferença entre dois números ')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if(n1 > n2):
    print(f'A diferença é {(n1 - n2):.2f}.')
elif(n2 > n1):
    print(f'A diferença é {(n2 - n1):.2f}.')
else:
    print('A diferença é 0.')

print('Soma do quadrado de uma número mais outros dois')

n1 = int(input('Digite o número que será elevado ao quadrado: '))
n2 = int(input('Digite o primeiro número para ser somado: '))
n3 = int(input('Digite o segundo número para ser somado: '))
res = n1 ** 2 + n2 + n3

print(f'O resultado é {res}')

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

print('Saiba em que conceito sua nota está posicionada')

nota = float(input('Digite sua nota: '))
nota = f'{nota:.1f}'
nota = float(nota)

if((nota >= 9) and (nota <= 10)):
    print('Sua nota está no conceito A')
elif((nota >= 7) and (nota <= 8,9)):
    print('Sua nota está no conceito B')
elif((nota >= 5) and (nota <= 6,9)):
    print('Sua nota está no conceito C')
elif((nota >= 0) and (nota <= 4,9)):
    print('Sua nota está no conceito D')

print('Cálculadora')
print('Qual operação você deseja usar?\n')

c = input('Escolha entre as operações "+", "-", "/" e "*": ')

print('AVISO: os números devem ser INTEIROS!')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if(c == '+'):
    print(f'{n1 + n2}')
elif(c == '-'):
    print(f'{n1 - n2}')
elif(c == '/'):
    print(f'{n1 / n2}')
elif(c == '*'):
    print(f'{n1 * n2}')
else:
    print('Operação Inválida')

print('Descubra o maior número entre 10')

maxn = -inf
nums = []

for i in range(10):
    n = float(input('Digite um número:'))
    nums.append(n)

for i in nums:
    if(i > maxn):
        maxn = i

print(f'O maior número é {maxn}')

num = int(input('Digite um número natural ao qual você deseja fazer o fatorial: '))
n = num

if(num <= 0):
    print('\nERRO: NÚMERO NEGATIVO')
    exit()

for i in range(num):
    if(num == 1):
        break
    
    if(n > 1):
        n -= 1
        num = num * n

print('\n' + str(num))

fibo = [1, 1]

for i in range(1,11):
    soma = fibo[i] + fibo[i-1]
    fibo.append(soma)

print(fibo)

primos = []

for i in range(10):
    num = int(input('Digite um número inteiro: '))
    serprimo = True
    
    for j in range(2, num):
        if(num % j == 0):
            serprimo = False

    if((serprimo == True) and (num not in primos)):
        primos.append(num)

print(f'Entre os números digitados temos {len(primos)} primo(s), sendo ele(s) o(s) seguinte(s) número(s):\n{primos}')


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

reg_media_alunos = []
soma = 0

for i in range(10):
    aluno = input('Digite o nome do aluno: ')
    av1 = float(input('Qual foi sua nota na primeira avaliação? '))
    av2 = float(input('Qual foi sua nota na segunda avaliação? '))
    av3 = float(input('Qual foi sua nota na terceira avaliação? '))
    media = (av1 + av2 + av3) / 3
    media = float(f'{media:.1f}')

    if(media >= 7):
        print(f'{aluno} tirou {media} e está aprovado')
    elif((media >= 4) and (media <= 6,9)):
        print(f'{aluno} tirou {media} e está de AF')
    elif(media < 4):
        print(f'{aluno} tirou {media} e está reprovado')

    reg_media_alunos.append(media)

for i in reg_media_alunos:
    soma += i

media_geral = soma / len(reg_media_alunos)

print(f'A média geral dos alunos é {media_geral:.1f}')

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

salarios = {}
soma = 0
menor_salario = inf
maior_salario = -inf
menor_salario_key = None
maior_salario_key = None

def imposto(porcentagem):
    return salario_bruto * (porcentagem/100)

for i in range(10):
    funcionario = input('Digite o nome do funcionário: ')
    salario_bruto = int(input('Digite o salário do funcionário: '))

    print('\nQuanto ao imposto de renda:')
    
    if(salario_bruto > 2000):
        print(f'    O imposto de renda de {funcionario} será de R${imposto(15):.2f}'.replace('.',','))
        
        salario_liquido = salario_bruto - float(f'{imposto(15):.2f}')
    elif((salario_bruto > 1500) and (salario_bruto <= 2000)):
        print(f'    O seu imposto de renda de {funcionario} será de R${imposto(10):.2f}'.replace('.',','))
        
        salario_liquido = salario_bruto - float(f'{imposto(10):.2f}')
    elif(salario_bruto <= 1500):
        print(f'    {funcionario} está isento de imposto de renda')
        
        salario_liquido = salario_bruto

    print(f'\nQuanto ao salário líquido:\n    O salário líquido de {funcionario} é R${salario_liquido:.2f}\n'.replace('.',','))

    salarios[funcionario] = salario_bruto
    
for key, i in salarios.items():
    if(int(i) > maior_salario):
        maior_salario = i
        maior_salario_key = key

for key, i in salarios.items():
    if(int(i) < menor_salario):
        menor_salario = i
        menor_salario_key = key

for key, i in salarios.items():
    soma += int(i)

media_salarial = soma / len(salarios)
media_salarial = f'{media_salarial:.2f}'.replace('.', ',')

print(f'Com as informações coletadas dos funcionários temos que a média salarial é de R${media_salarial} onde temos que:\n    {maior_salario_key} recebe o maior salário, sendo esse igual a R${maior_salario},00\n    {menor_salario_key} recebe o menor salário, sendo esse igual a R${menor_salario},00')

total = 0
quant = int(input('Quantas maçãs foram compradas? '))

if(quant >= 12):
    preco_maca = 1
else:
    preco_maca = 1.3

for i in range(quant):
    total += preco_maca

print(f'\nO preço total da compra será de {total}')

reg_funcionarios = {}
maior_hora_key = None
maior_hora = 0
hrs_mensais = 40 * 4
salario_mensal = int(input('Digite o salário dos funcionários: '))

for i in range(10):
    funcionario = input('\nDigite o nome do funcionário: ')
    hrs_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
    valor_hr = salario_mensal / hrs_mensais
    salario = salario_mensal

    if(hrs_trabalhadas > hrs_mensais):
        salario += (hrs_trabalhadas - hrs_mensais) * valor_hr * 1.5
    elif(hrs_trabalhadas < hrs_mensais):
        salario = valor_hr * hrs_trabalhadas
        
    
    salario = f'{salario:.2f}'.replace('.',',')
    
    print(f'\n{funcionario} receberá R${salario} esse mês.')

    reg_funcionarios[funcionario] = hrs_trabalhadas

for key, i in reg_funcionarios.items():
    if(int(i) > maior_hora):
        maior_hora = i
        maior_hora_key = key

print(f'{maior_hora_key} foi o funcionário com maior quantidade de horas trabalhadas com {maior_hora}hrs.')

for i in range(5):
    debito = randint(50, 5000)
    credito = randint(50, 5000)
    
    print(f'\nSeu crédito é de {"R${0:.2f}".format(credito).replace(".",",")} e seu débito é de {"R${0:.2f}".format(debito).replace(".",",")}')
    saldo_atual = credito - debito
    
    print(f'Seu saldo atual é de {"R${0:.2f}".format(saldo_atual).replace(".",",")}')
    
    saque = float(input("Insira o quanto você deseja sacar: R$"))
    
    if((saldo_atual >= saque) and (saldo_atual > 0)):
        saldo_atual -= saque
        print(f'\nSaque aprovado, agora seu saldo é de {"R${0:.2f}".format(saldo_atual).replace(".",",")}')
    else:
        print("Saque inválido.\n")

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

numeros = ''

for i in range(10):
    numeros += f'{i+1} '

print(numeros)

numeros = ''

for i in range(10):
    numeros += f'{10-i} '

print(numeros)

habitante = []
menor_sal = 0
soma0 = 0
soma1 = 0

for i in range(5):
    salario = int(input('\nDigite o salário do habitante: '))
    filhos = int(input("Digite quantos filhos o habitante tem: "))
    if(salario < 1000):
        menor_sal += 1
    habitante.append([salario, filhos])

for i in habitante:
    soma0 += i[0]
    soma1 += i[1]

media_salarial = soma0 / len(habitante)
media_filhos = soma1 / len(habitante)
percentual = menor_sal / len(habitante) * 100

print('\nNessa cidade temos três dados quanto aos habitantes:')
print(f'>>>>> Média Salárial..............: {"R${0:.2f}".format(media_salarial).replace(".",",")}')
print(f'>>>>> Média de filhos.............: {media_filhos}')
print(f'>>>>> Percentual de Salário Baixo.: {percentual}%')

vetor = []

for i in range(10):
    vetor.append(randint(-100, 100))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

vetor.sort()

print('Vetor ordenado de forma crescente ->', vetor)

vetor.sort(reverse=True)

print('Vetor ordenado de forma decrescente ->', vetor)
print('-'*50)

vetor0 = []
vetor1 = []
vetorsoma = []

for i in range(2,21):
    if(i % 2 == 0):
        vetor0.append(i**2)
   
    if(i in range(10,20)):
        vetor1.append(i)

j = 0

while j < len(vetor0):
    vetorsoma.append(vetor0[j] + vetor1[j])
    
    j = j + 1

print('-'*50)
print('', vetorsoma, '')
print('-'*50)

vetor = []
primos = []

for i in range(10):
    vetor.append(randint(1, 200))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

for i in vetor:
    if(i != 1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            primos.append(i)

print('Primos no vetor ->', primos)
print('-'*50)

vetorfibo = [1, 1]

for i in range(1,21-len(vetorfibo)):
    soma = vetorfibo[i] + vetorfibo[i-1]
    vetorfibo.append(soma)

print('-'*50*2)
print('', vetorfibo, '')
print('-'*50*2)

vetor = []
temp = None

for i in range(10, 21):
    vetor.append(i)

for i in range(int(len(vetor) / 2)):
    if(vetor[i] % 2 == 0):
        temp = vetor[i]
        vetor[i] = vetor[len(vetor) - i - 1]
        vetor[len(vetor) - i - 1] = temp

print('-'*50)
print('', vetor, '')
print('-'*50)

vetor = []
valor = int(input('Digite um número e veja se ele está dentro do vetor randomico: '))

for i in range(10):
    vetor.append(randint(-100, 100))

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)

if(valor in vetor):
    print(f'O número {valor} está presente no vetor e tem posição inicial igual a: {vetor.index(valor)}')
else:
    print(f'O número {valor} não está presente no vetor')

print('-'*50)

vetor = []
par = 0
impar = 0

for i in range(10):
    vetor.append(randint(-100, 100))

for i in vetor:
    if(i % 2 == 0):
        par = par + 1
    else:
        impar = impar + 1

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)
print('Número de valores pares ->', par)
print('Número de valores impares ->', impar)
print('-'*50)

vetor = []
repetidos = []
repeticoes = 0

for i in range(10):
    vetor.append(randint(-100, 100))

for i in range(len(vetor)):    
    for j in range(i+1, len(vetor)):    
        if(vetor[i] == vetor[j]):
            if(not(vetor[i] in repetidos)):  
                repetidos.append(vetor[j])
            repeticoes = repeticoes + 1
            break

print('-'*50)
print('Vetor randomicamente gerado ->', vetor)
print('Valores repetidos ->', repetidos)
print('Número de repetições ->', repeticoes)
print('-'*50)