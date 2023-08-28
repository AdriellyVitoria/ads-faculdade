numero = int ( input ('valor: '))

while numero > 0:
    valor = numero % 10
    numero //= 10
    valor2 = numero % 10
    if valor == valor2:
        print("igual")
        