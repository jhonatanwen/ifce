import random

for i in range(5):
    debito = random.randint(50, 5000)
    credito = random.randint(50, 5000)
    
    print(f'\nSeu crédito é de {"R${0:.2f}".format(credito).replace(".",",")} e seu débito é de {"R${0:.2f}".format(debito).replace(".",",")}')
    saldo_atual = credito - debito
    
    print(f'Seu saldo atual é de {"R${0:.2f}".format(saldo_atual).replace(".",",")}')
    
    saque = float(input("Insira o quanto você deseja sacar: R$"))
    
    if((saldo_atual >= saque) and (saldo_atual > 0)):
        saldo_atual -= saque
        print(f'\nSaque aprovado, agora seu saldo é de {"R${0:.2f}".format(saldo_atual).replace(".",",")}')
    else:
        print("Saque inválido.\n")