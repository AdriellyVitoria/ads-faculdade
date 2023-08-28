#Adrielly 
a, b, c = map (float, input ().split()) 
perimetro = a + b + c
area = ((a + b) * c) / 2
if (a < b + c and b < a + c and c < a + b):
  print (f'Perimetro = {perimetro:.0f}')
else:
  print (f'Area = {area:.0f}')


#letra a- Se os valores formarem um perimetro, vai mostra o resultando, caso o perimetro seja falso, vai imforma a area.

#letra b- vai print o perimetro = 18

#letra c- variaveis com letras maiuculas, falta de comentarios, mascara antiga, codigo poluido demais. 