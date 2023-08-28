#Imagine uma lista de clientes para atuar como uma fila. Em uma fila, o primeiro a chegar deve ser o primeiro a ser atendido. Considerando uma fila com 10 clientes. Caso um novo cliente chegue, ele deve ser inserido no final da fila com um append. Para realizar o atendimento retirando o cliente da fila e obtendo o valor retirado, é preciso usar o pop . Faça um programa para gerenciar uma fila e crie um "menu" com as seguintes opções: A - Atendimento F - Final S - Sair


cliente = []

posicao = 0

while True:
   
    print ('-=' * 30)
    print ('  #MENU#\n[1] Atendimento\n[2] Final\n[3] Sair')
    print ('-=' * 30)
    encaminhamento = int (input ('Digite a opção '))
    posicao += 1

    if encaminhamento == 1:
        cliente.pop(0)
        posicao -= 1

    elif encaminhamento == 2:
        print (f'add com sucesso')
        cliente.append(1)

    elif encaminhamento == 3:
        break

print (f'No final do dia tivemos {len(cliente) } atendimento')
