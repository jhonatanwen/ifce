print('Vamos achar o MDC de dois inteiros!\n')

nums = []
primos = [2]
i = 0
mdc = 1
num0 = int(input('Digite o primeiro número.: '))
num1 = int(input('Digite o segundo número..: '))
maior = num0

if(num1 > num0):
    maior = num1

for j in range(2, maior+1): 
    if(j>1): 
        for k in range(2,i): 
            if(j % k==0): 
                break
        else: 
            primos.append(j) 

nums.append(num0)
nums.append(num1)

while (nums[0] != 1 and nums[1] != 1):
    if(nums[0] % primos[i] == 0 and nums[1] % primos[i] == 0):
        mdc = mdc * primos[i]
        nums[0] = nums[0] / primos[i]
        nums[1] = nums[1] / primos[i]
    elif(nums[0] % primos[i] == 0 and nums[1] % primos[i] != 0):
        nums[0] = nums[0] / primos[i]
    elif(nums[0] % primos[i] != 0 and nums[1] % primos[i] == 0):
        nums[1] = nums[1] / primos[i]
    elif(nums[0] % primos[i] != 0 and nums[1] % primos[i] != 0):
        i = i + 1

print(f'O mdc de {num0} e {num1} é {mdc}')

