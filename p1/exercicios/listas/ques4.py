#Imagine uma lista de clientes para atuar como uma fila. Em uma fila, o primeiro a chegar deve ser o primeiro a ser atendido. Considerando uma fila com 10 clientes. Caso um novo cliente chegue, ele deve ser inserido no final da fila com um append. Para realizar o atendimento retirando o cliente da fila e obtendo o valor retirado, é preciso usar o pop . Faça um programa para gerenciar uma fila e crie um "menu" com as seguintes opções: A - Atendimento F - Final S - Sair

cliente = []
giros = posicao = posicao_geral = 0
# quantas pessoas foram antedinda no dia? eu add na lista

while True:
    print ('  #MENU#\n[1] Atendimento\n[2] Final\n[3] Sair')
    resposta = int (input ('Digite a opção '))

    while resposta > 3 or resposta <= 0:
      print ('ERRO, TENTE NOVAMENTE')
      print ('  #MENU#\n[1] Atendimento\n[2] Final\n[3] Sair')
      resposta = int (input ('Digite a sua opção '))

    if resposta == 1:
      print (f' a pessoa que está na posicao {posicao_geral} foi para o atendimento')
      cliente.pop(1)
      
    elif resposta == 2:
      print (f'vc foi add, com sucesso sua posicao é {posicao_geral}')
      giros += 1
      cliente.append(giros)

    elif resposta == 3:
      break

for numero in cliente:
  soma = numero

print (f'''Foram antendidas {soma} pessoas no dia''')
