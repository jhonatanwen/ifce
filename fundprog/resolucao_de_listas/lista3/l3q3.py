fibo = [1, 1]

for i in range(1,11):
    soma = fibo[i] + fibo[i-1]
    fibo.append(soma)

print(fibo)