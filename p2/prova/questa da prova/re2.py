a, b, c = map (int, input ().split ()) #entra dos numeros int
if (a < (b + c) and b < (a + c) and c < (a + b)): #verificar se é triangulo
  print ('Parabens, os numeros formam um triangulo!') #imprimir saida
  print ('-=' * 25) #só para separar
  #definir o tipo de triangulo
  if a != b != c: 
    print ('Triângulo Escaleno')
  elif (a == b != c or c == b != a or c == a!= b):  
    print ('Triângulo Isósceles') 
  elif a == b == c:
      print ('Triângulo Equilátero')
else: #apresentar saida se não formar triangulo
  print ('Os valores não formam um triângulo') 