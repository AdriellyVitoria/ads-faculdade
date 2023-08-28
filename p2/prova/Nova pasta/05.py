#questão 5 - Letras adjacentes iguais

frase = input ().split() #entrada 

contador = 0

#verificação para pegar letras repetidas para contar
for palavra in frase: #as palavras ficam separadas por espaços 
  for letra in range(len(palavra)-1):
    if palavra [letra] == palavra [letra + 1]:
      contador += 1

if contador:
  print (f'Na frase há {contador} palavra(s) com letras repetidas.') #saida se tive palavra repetida
else:
  print ('Não há palavras com letras repetidas na frase.') #saida se não tiver
