contador = soma = 0 #contadores
deseja = 'S' #interrupção
aluno = input ('Qual o nome do aluno: ') #entrada do nome do aluno
while deseja == 'S': #laço de repetição
  nota = float (input ('Nota do aluno: ')) #entrada das notas
  #somatorios dos contadores
  soma += nota 
  contador += 1
  deseja = input ('Quer colocar mais notas[S/N]? ').strip().upper() #submissão para parar
  if deseja != 'S' and deseja != 'N': #em caso de resposta errada
    print ('Erro tente novamente. ') #saida 
    deseja = input ('Quer colocar mais notas[S/N]? ').strip().upper() 
  if deseja == 'N': #para calcular a media
    print (f'O aluno {aluno}, ficou com a média {soma / contador:.1f}')#saida
