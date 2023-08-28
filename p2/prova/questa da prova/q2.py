#deve se escolher a opção de par ou impar: tem q colocar se é de 1 a 10 ?
opcao, numero1, numero2 = str (input ()).split()
print (f"{opcao}, {numero1}, {numero2}")
numero1 = int (numero1)
numero2 = int (numero2)

#soma os dois numeros se a soma vou dividido por 2 é par. 
soma = numero1 + numero2

#imprimir o resultando falando qual foi o jogando que ganhou.
if opcao == 'par' and soma % 2 == 0:
    print ('jogador 1 venceu!')
else:
    print ('Jogador 2 venceu!')

#questão 2, Aluna: Adrielly Vitoria