#Desenvolva um programa que leia duas listas de mesmo tamanho, com números inteiros, e gere uma terceira lista com os elementos das duas primeiras.

# '''LISTAS JÁ PREENCHIDAS'''
# lista1 = [1, 2, 3, 4, 5] #lista uma
# lista2 = [6, 7, 8, 9, 10] #lista 3

# print (lista1 + lista2) #saida juntado as duas listas


'''LISTAS COM O USUARIO FORNECENDO OS VALORES'''
#lista vazias
lista1 = []
lista2 = []

for i in range (3): #vai até 3
  lista1.append(int (input ())) #entrda dos valores da lista

for j in range (3): #vai até 3
  lista2.append(int (input ())) #entrda dos valores da lsita

print (lista1 + lista2) #saida junta as 2 listas
