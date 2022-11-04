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