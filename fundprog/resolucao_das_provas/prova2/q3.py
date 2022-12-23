def multiplosDeTres(inicio = 2, vetor = []):
    if inicio % 3 == 0:
        vetor.append(inicio)
    
    if inicio == 30:
        return vetor
        
    return multiplosDeTres(inicio + 1, vetor)

print(multiplosDeTres())