from math import inf

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