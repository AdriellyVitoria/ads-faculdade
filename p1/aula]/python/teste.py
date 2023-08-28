try:
    a = int (input())
    b = int (input ())
    r = a / b

except (ValueError, TypeError):
      print('Tivemos um problema com os tipos de dados que vc digitou ')
except ZeroDivisionError:
    print('Zero')
except KeyboardInterrupt:
    print('O usuario preferiu não imformar um numero')
except SyntaxError:
    print ('erro de sitaxe')
except Exception as erro:
    print (f"infelimente tivemos um problema {erro.__class__}")
else:
    print(f'{r:.1f}')
finally:
    print ('volte sempre')


