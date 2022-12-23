from random import randint

vetor = []
usado = []
i = 0

while i < 10:
    num = randint(1, 20)

    if num not in usado:
        vetor.append(num)
        usado.append(num)
        i = i + 1

print(vetor)