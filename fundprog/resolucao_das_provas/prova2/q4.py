def emBinario(num, binario = []):
    if num == 1 or num == 0:
        if num == 1:
            binario.append('1')
        
        binario.reverse()
        str = ''.join(binario)
        return str

    if num % 2 == 0:
        binario.append('0')
    else:
        binario.append('1')
    
    return emBinario(num // 2, binario)

binario_requisitado = int(input("Digite um número inteiro ao qual você queira traduzir para binário:\n->"))

print("Resultado:")
print(emBinario(binario_requisitado))