#criar a função soma, ser o resultando for maior q mil deve dá o erro overfliwError

def soma(a, b):
    try:
        if a < 1000 and b < 1000:
            soma = a + b
        print(soma)
    except OverflowError:
        print('numero elevando demais para realizar a soma')
    except UnboundLocalError:
        print('erro')
            
numero = int (input())
num = int (input ())
soma(numero, num)