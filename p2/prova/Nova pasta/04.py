# Questão 4- Inteiros adjacentes iguais

num =  int (input ()) #entrada do numero

adjacentes_iguais = False #para ficar claro o entendimento 

while num > 0 and not adjacentes_iguais: #duas avaliações q sejam vdd, 
  atual = num % 10 #pegar o ultimo numero 
  adjacentes = num // 10 % 10 #recebe o pernultimo numero


  if atual == adjacentes: #verificar se tem numero iguais 
    adjacentes_iguais = True
    print ('sim')
  num //= 10

else: # um else para o while, caso seja falso 
  if not adjacentes_iguais:
    print ('não')
    