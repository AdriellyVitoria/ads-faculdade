def leia_int(msg):
    ok = False
 
    while True:
        try:
            n = int(input (msg))
        except:
            print('ERRO')
        else:
            return n
        

def leia_float(msg):
    while True:
        try:
            x = int(input(msg))
        except:
            print('ERRO')
        else:
            return x

n = leia_int('Digite um numero ')
print(f'vc digitou o numero {n}')

x = leia_float('Digite um numero: ')
print(f'vc digitou o numero {x}')