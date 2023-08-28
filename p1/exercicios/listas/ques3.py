#Escreva um programa que leia duas listas de mesmo tamanho, com números inteiros, e gere uma terceira lista sem números repetidos

#listas vazias
lista1 = []
lista2 = []

for i in range (3): #vai até 3
  valor1 = int (input ()) #entrada do numero
  if valor1 not in lista1: #verificar se não tem na lista
    lista1.append(valor1) #entrda dos valores da lista

for j in range (3): #vai até 3
  valor = int (input ()) #entrada dos valores da lista
  if valor not in lista1: #verificar se não tem na lista
     lista2.append(valor) #entrada dos valores da lista
  
lista3 = lista1 + lista2 #junta as listas
lista3.sort() #colocando em ordem
  
print (lista3) #saida e junta as 2 listas
