import math

print('Descubra qual número é o maior entre três.')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
nums = [n1, n2, n3]
maxn = -math.inf

for n in nums:
    if(n > maxn):
        maxn = n

print(f'O maior número é {maxn}')