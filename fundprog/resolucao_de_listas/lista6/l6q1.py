contas = []

for i in range(5):
    numconta = input(f'\nQual o número da conta do cliente {i+1}: ')
    nome = input(f'Digite o nome do cliente: ')
    saldo = float(input('Digite o saldo na conta do cliente: '))
    op = input('Informe a operação que o cliente fará ["C" ou "D"]: '.upper())
    cliente = [numconta, nome, saldo, op]

    contas.append(cliente)

print(contas)