lista1 = []
lista2 = []
for i in range(10):
    elemento = int(input('Digite um número: '))
    lista1.append(elemento)
    lista2.append(elemento)

lista1.sort()
lista2.sort(reverse = True)
print(lista1, lista2)