print('Descubra a diferença entre dois números ')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if(n1 > n2):
    print(f'A diferença é {(n1 - n2):.2f}.')
elif(n2 > n1):
    print(f'A diferença é {(n2 - n1):.2f}.')
else:
    print('A diferença é 0.')