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