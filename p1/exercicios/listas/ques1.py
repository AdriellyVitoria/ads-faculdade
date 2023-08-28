#Faça um programa que leia 5 notas de um aluno e calcule a média imprimindo o resultado com uma casa decimal.

# numeros = [] #lista vazia
# soma = 0 #acumulador

# for i in range (5): # vai até 5
#   numeros.append(float (input ())) #entrada

# for numero in numeros: #vai pegar um numero da lista numeros
#   soma += numero #soma todos os numeros da lista 
  
# print (f'{soma//5:.1f}') #saida com o calculo 


numeros = []
soma = posicao = 0
while True:
  notas = float (input ('Digite as notas, para parar digiter [999] '))
  if notas == 999:
    for i, j in enumerate(numeros):
      print (f'nota {i}: {j}')
    print (f'Media final: {soma / posicao:.1f}')
    break
  soma += notas
  numeros.append(notas)
  posicao += 1
  

soma += numeros.append(notas)
