#coloque para receber dois numeros. para dividir... e faça o tratamento do erro
x = True


def verificar():
    try:
        a = int (input ())
        b = int (input ())
        dividir = a / b
        print(dividir)
        x = input('add mais numero: ').upper()
        if x == 'S':
            verificar()
        else:
            x = False
    except ZeroDivisionError:
        print('não pode dividir por zero')
    except ValueError:
        print('o usuario não digitou um numero')
    finally:
        print('fim')


verificar()