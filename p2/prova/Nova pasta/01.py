#ler tres valores 
# x vai ser o multiplos
#a, b vai ser conferindo se é multiplos de x (inclusive eles)
multiplos = 0
x, a, b = map (int, input ().split ())
if a > b: #fazer a trocar 
 a = b
for i in range (a, b + 1): 
  if i % x == 0: #ver se é multiplos de x
    print (i, end=' ') #saida
    multiplos += 1
 
if multiplos == 0: #verificar se não é multiplos
  print (f'Não há múltiplos de {x} no intervalo [{a},{b}].') #saida