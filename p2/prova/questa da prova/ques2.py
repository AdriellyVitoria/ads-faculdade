from re import I


contador = soma = 0
nota = 'M'
aluno = input ('')
while nota == 'M':
  nota = float (input ('adiciomar nota [N] ou [M] para calcular a média')).strip().upper()
  soma += nota
  contador += 1
  if nota != 'M':
    print ('Erro tente novamente. ')
    nota = float (input ('adiciomar nota ou [M] para calcular a média')).strip().upper()
  if nota == 'N':
    print (f'O aluno {aluno}, ficou com a média {soma / contador}')
