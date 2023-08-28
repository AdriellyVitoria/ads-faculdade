#Imagine uma lista de clientes para atuar como uma fila. Em uma fila, o primeiro a chegar deve ser o primeiro a ser atendido. Considerando uma fila com 10 clientes. Caso um novo cliente chegue, ele deve ser inserido no final da fila com um append. Para realizar o atendimento retirando o cliente da fila e obtendo o valor retirado, é preciso usar o pop . Faça um programa para gerenciar uma fila e crie um "menu" com as seguintes opções: A - Atendimento F - Final S - Sair


cliente = []
cont = 0
while True:

  print ('=-' * 30)
  print ('\nMENU\nA - Atendimento\nF - Final\nS - Sair\n')
  print ('=-' * 30)
  opcao = input ('Digite a sua opção: ').upper()

  if opcao == 'F':
    nome = input ('Digite o nome do cliente: ')
    cliente.append(nome)
    print (f'Sua posicao é {len(cliente)}')
      
  elif opcao == 'A':
    if cliente == []:
      print ('Não tem ninguem na fila')
    else:
      print ('*' * 30)  
      primeiro = cliente.pop(0)
      print (f'o {primeiro} foi por atendimento')
      cont += 1

  elif opcao == 'S':
    break

  else:
    print ('ERRO, TENTE NOVAMENTE!!')

print (f'foi atendidas {cont} pessoas.')