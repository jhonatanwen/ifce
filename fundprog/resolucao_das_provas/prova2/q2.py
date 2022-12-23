def somatorioPares(inicio):
    if inicio == 20:
        return 20

    if inicio % 2 == 0:
        return inicio + somatorioPares(inicio + 1)
    else:
        return 0 + somatorioPares(inicio + 1)

print(somatorioPares(1))