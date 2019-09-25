fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')


def Deposit(dictBank, listOperation):
    name = listOperation[0]
    inCount = int(listOperation[1])
    if name not in dictBank:
        dictBank[name] = 0
    dictBank[name] += inCount


def Withdraw(dictBank, listOperation):
    name = listOperation[0]
    sum = int(listOperation[1])
    if name not in dictBank:
        dictBank[name] = 0
    dictBank[name] -= sum


def Balance(dictBank, listOperation):
    name = listOperation[0]
    if name not in dictBank:
        print('ERROR', file=fout)
    else:
        print(dictBank[name], file=fout)


def Transfer(dictBank, listOperation):
    name1 = listOperation[0]
    name2 = listOperation[1]
    sum = int(listOperation[2])
    if name1 not in dictBank:
        dictBank[name1] = 0
    dictBank[name1] -= sum
    if name2 not in dictBank:
        dictBank[name2] = 0
    dictBank[name2] += sum


def Income(dictBank, listOperation):
    interest = int(listOperation[0])
    for name in dictBank:
        if dictBank[name] > 0:
            dictBank[name] += int(dictBank[name] * interest / 100)


baseBank = {}
for line in fin:
    command, *other = line.strip().split()
    if command == 'DEPOSIT':
        Deposit(baseBank, other)
    elif command == 'WITHDRAW':
        Withdraw(baseBank, other)
    elif command == 'BALANCE':
        Balance(baseBank, other)
    elif command == 'TRANSFER':
        Transfer(baseBank, other)
    elif command == 'INCOME':
        Income(baseBank, other)
    else:
        print(command, ' - ', other)

fin.close()
fout.close()
