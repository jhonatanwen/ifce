contas = []

for i in range(5):
    numconta = input(f'\nQual o número da conta do cliente {i+1}: ')
    nome = input(f'Digite o nome do cliente: ')
    saldo = float(input('Digite o saldo na conta do cliente: '))
    op = input('Informe a operação que o cliente fará ["C" ou "D"]: '.upper())
    saldo_atualizado = None
    match op:
        case 'C':
            credito = float(input('Quanto você quer creditar?\n->'))
            saldo_atualizado = saldo + credito
        case 'D':
            debito = float(input('Quanto você quer debitar?\n->'))
            saldo_atualizado = saldo - debito
        case _:
            print('Operação não reconhecida, nenhum alteração será executada.')
    cliente = [numconta, nome, saldo, op, saldo_atualizado]

    contas.append(cliente)

print(contas)