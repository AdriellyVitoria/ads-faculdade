#um funcao "soma_digitos"
#entra de numero (inteiro)
#eu quero fatiar o numero e pegar um digito por vez 

def soma_digito(numero):
  soma = 0
  while numero > 0:
    soma += numero % 10
    numero //= 10
  return soma


valor = int (input ())
print (soma_digito (valor))
#   #retone a soma os digitos da entrada
