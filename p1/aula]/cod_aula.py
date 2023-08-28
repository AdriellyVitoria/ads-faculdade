# w - escrita
# r - leitura
# a - escritas (preserva o conteúdo)

#CRIAR ARQUIVOS#
# arquivo = open('linhas1.txt', 'w')
# arquivo.write('Analise e dese de sistemas') #parar escrever

#tratamento de exceções

#      * TRY *

# A palavra try (“tentar”, em inglês) é usada pra criar um bloco de código que talvez dê errado. Essa palavra chave é a alma do tratamento de exceções. Só da pra gente tratar exceções que estão dentro do bloco try.

# ** EXCEPT **

#Esse código só é executado quando o código no bloco try der treta e não funcionar. Se a gente colocar o except, igual na imagem acima, QUALQUER erro que der no código do try vai simplesmente chamar o bloco except. No entanto, a gente também consegue especificar o erro que a gente quer tratar! 

# #for linha in range(1, 11):
#     #arquivo.write(f'{linha}\n')

# arquivo.close() #parar fechar 
# print (arquivo)

#LEITURA #
# arquivo = open('linhas1.txt', 'r')
# arquivo.write('Analise e dese de sistemas') #parar escrever
# for linha in arquivo.readlines():   
#     print (linha)

#arquivo.close() #parar fechar 

# arquivo = open('linhas1.txt', 'a')

# for linha in arquivo.readable():
#     if linha[-1] == '\n':
#         palavra = input()
#         arquivo.write(palavra)
#     #arquivo.write(f'{linha}\n') #parar escrever

# arquivo.close()

# from math import sqrt as raizquadrada

# with open('numero.txt', 'r') as arquivos:
#     for linha in arquivos.readlines():
#         print(linha)

#tratamento de Exceções

# num = [1, 2, 3]

# for i in range(len(num)):

#     try:
#         numero = int (input('Digite um valor: '))
#         print(num[numero])

#     except IndexError:
#         print('Informe um número existente na lista')
#     else:
#         print('Nenhuma exceção para essa entrada')
#     finally: #vai entra sempre
#         print(f'Tentativa {i + 1}')

    # except ValueError:
    #     print('vc imformou uma letra, por favor, informe um numero: ')

lista = ['Bety', 'Arthun', 'Lucas', 'Adrielly', 'Kayo', 'Kelvin ', 'Mateus']

for i in  range (len(lista)):
    nome = input('Nome para pesquisa: ')

    if nome == lista[i]:
        print(nome)
    else:
        x = nome[0].upper()
        for i in lista:
            if i[0] == x:
                print(i)