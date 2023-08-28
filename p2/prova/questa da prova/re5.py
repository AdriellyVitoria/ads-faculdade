# velocidade, espaço = map (float, input ().split()) #velocidade do corredor e o espaço q correu
# media = velocidade // espaço #calcular a media
# if media < 10: #abaixo de 10km/h amador
#   print (f'{media:.1f} km/h - Amador')
# elif media <= 10 or media <= 15: #entre 10 e 15km/h aspirante
#   print (f'{media:.1f} km/h - Aspirante')
# elif media > 15: #acima de 15km/h profissional
#   print (f'{media:.1f} km/h - Profissional')


def combinacoes(lista, num):
  if num <= 0 or len(lista) < num:
      return []

  result = []
  combinacao_atual = []

  def backtrack(start):
      if len(combinacao_atual) == num:
          result.append(tuple(combinacao_atual))
          return

      for i in range(start, len(lista)):
          combinacao_atual.append(lista[i])
          backtrack(i + 1)
          combinacao_atual.pop()

  backtrack(0)
  return result

lista = [1, 2, 3]
numero = 2

resultado = combinacoes(lista, numero)
print(resultado)