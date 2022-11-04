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