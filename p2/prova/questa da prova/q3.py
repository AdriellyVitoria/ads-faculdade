hora_i, min_i = map (int, (input ()).split(':')) #entrada de horas e minutos inicial
hora_f, min_f = map (int, (input ()).split(':')) #entrada de horas e minutos finais

tempo_h = hora_f - hora_i #calculando a hora
tempo_m = min_f - min_i #calculando o min


if tempo_h == 0 and tempo_m <= 15: #se ficar só 15 min
    print (f'Estacionamento Gratis')

elif tempo_h == 0 and tempo_m > 15: #se ficar acima de 15 min
    print (f'Valor à Pagar: R$ 2.00')

elif tempo_h <= 1 and tempo_m <= 60: #se for acima de 1 hora
    print (f'Valor à Pagar: R$ 3.00')

elif tempo_h <= 2 and tempo_m <= 60: #se for acima de 2 horas
    print (f'Valor à Pagar: R$ 4.00')

elif tempo_h >= 3 : #se for acima de 3 horas
    print (f'Valor à Pagar: R$ 5.00')



#aluna: Adrielly Vitoria questão 3