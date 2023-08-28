#ler o valor inteiro do dinheiro com dupla precisão
valor = round (float (input()), 2)

#separar as notas de 100 até  os centavos.
#começar separando as notas de 100:
cem = int (valor / 100)

#para prosseguir vc pegar o valor completo, e diminuir pela as notas de 100 separanda. assim:
sobrou = valor - (cem * 100) 

#separa as notas de 50:
cinquenta = int (sobrou / 50) 

#pegar o valor q sobrou e diminuir pela a nota q saiu:
sobrou1 = sobrou - (cinquenta * 50)

#separa as de 20:
vinte = int (sobrou1 / 20)

#diminuir os vinte q saiu:
sobrou2 = sobrou1 - (vinte * 20)

#separa as notas de 10:
dez = int (sobrou2 / 10)

#diminiur as notas que sairam:
sobrou3 = sobrou2 - (dez * 10)

#separa as notas de 5:
cinco = int (sobrou3 / 5)

#diminuir as notas que sairam:
sobrou4 = sobrou3 - (cinco * 5)

#separa as notas de 2:
dois = int (sobrou4 / 2)

#diminuir as notas que sairam:
sobrou5 = sobrou4 - (dois * 2)

#PARA MOEDAS AGORA:

#separa as moedas de 1 real:
real = int (sobrou5 / 1)

#diminuir todo o dinheiro q saiu:
sobrou6 = sobrou5 - real

#como fazer para os centavos ficarem maiores para o programar n dá erros.
#faça com o oposto de %, multiplique por 100 para tem um valor maio.

#centavos mutiplicando por cem:
centavos = sobrou6 * 100
#colocar round para eliminar as virgulas
centavos = round (centavos, 0)

#separar as moedas de 50 centavos:
centavos_50 = int (centavos // 50)

#diminuir oq foi separando:
centavos -= centavos_50 * 50

#separar as moedas de 25 centavos:
centavos_25 = int (centavos // 25)

#diminuir oq foi tirando:
centavos -= centavos_25 * 25

#separar as moedas de 10 centavos:
centavos_10 = int (centavos // 10)

#diminuir oq foi tirando:
centavos -= centavos_10 * 10

#separa as moedas de 5 centavos:
centavos_5 = int (centavos // 5)

#diminuir as moedas que foi tirando:
centavos -= centavos_5 * 5

#separar as moedas de 1 centavos:
centavos_1 = int (centavos // 1)

#saida do resultando EM NOTAS:
print ('NOTAS:')
print (f'{cem} nota(s) de R$ 100.00')
print (f'{cinquenta} nota(s) de R$ 50.00')
print (f'{vinte} nota(s) de R$ 20.00')
print (f'{dez} nota(s) de R$ 10.00')
print (f'{cinco} nota(s) de R$ 5.00')
print (f'{dois} nota(s) de R$ 2.00')

#saida do resultando EM MOEDAS:
print ('MOEDAS:')
print (f'{real} moeda(s) de R$ 1.00')
print (f'{centavos_50} moeda(s) de R$ 0.50')
print (f'{centavos_25} moeda(s) de R$ 0.25')
print (f'{centavos_10} moeda(s) de R$ 0.10')
print (f'{centavos_5} moeda(s) de R$ 0.05')
print (f'{centavos_1} moeda(s) de R$ 0.01')


centavos = valor % 100 % 50 % 20 % 10 % 5 % 2 % 1
centavos = round (centavos * 100, 0)
moeda050 = centavos // 50
moeda025 = centavos % 50 // 25
moeda010 = centavos % 50 % 25 // 10
moeda005 = centavos % 50 % 25 % 10 // 5
moeda01 = centavos % 50 % 25 % 10 % 5