total = 0
quant = int(input('Quantas maçãs foram compradas? '))

if(quant >= 12):
    preco_maca = 1
else:
    preco_maca = 1.3

for i in range(quant):
    total += preco_maca

print(f'\nO preço total da compra será de {total}')