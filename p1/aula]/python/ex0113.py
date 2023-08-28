def leia_int (msg):
    while True:
        try:
            n = int ( input (msg))
        except:
            print('Valor inválido!')
        else:
            return n


n = leia_int('Digite um numero ')
print(f'Vc digitou {n}')