#24/02/2021 invalida
# dia, mes, ano = map (int, input ().split ('/'))
# if dia <= 31 and mes <= 12 and ano <= 9999:
#   print ('Data válida!')
# elif ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
#   print ('Data inválida!')

dia, mes, ano = map (int, input ().split('/')) #entrada 
meses_31 = ('01', '02', '03', '05', '07', '08', '10', '12') #verificar quem tem 31 dias
meses_30 = ('04', '06', '09', '11')
mes_02 = 28
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
  ano = 'bissexto'
  mes_02 += 1
  print ('Data valida')

else:
  print ('Data invalida')


  