media_solicitada = float(input('Qual a media do aluno? '))

def conceito(media):
    if media >= 0 and media < 4.9:
        return 'D'
    if media >= 5 and media < 6.9:
        return 'C'
    if media >= 7 and media < 8.9:
        return 'B'
    if media >= 9 and media <= 10:
        return 'A'

print(f'O aluno terminou com o conceito {conceito(media_solicitada)}')