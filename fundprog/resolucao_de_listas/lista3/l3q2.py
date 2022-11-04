num = int(input('Digite um número natural ao qual você deseja fazer o fatorial: '))
n = num

if(num <= 0):
    print('\nERRO: NÚMERO NEGATIVO')
    exit()

for i in range(num):
    if(num == 1):
        break
    
    if(n > 1):
        n -= 1
        num = num * n

print('\n' + str(num))