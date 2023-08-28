#Escreva uma função gerar_matriz(m, n, x) em que os parâmetros m, n são as dimensões da matriz e x é o valor que irá preencher os índices automaticamente. A função deve retornar a matriz preenchida [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# def gerar_matriz(m, n, x):
#     agru = []
#     m, n, x = map (int, input ().split ())
#     for i in range (m):
#     # agru = lista
#         lista = []
#         for j in range (n):
#         lista.append(x)
#         agru.append(lista)  #não está dentro da lista maior
    
#     print (agru, end=',')

     
def gerar_matriz(m, n, x):
    agru = []
    for i in range (m):
        lista = []
        for j in range (n):
            lista.append(x)
        agru.append(lista)  

    return agru


linha, coluna, valor = map (int, input ().split ())
x = gerar_matriz (linha, coluna, valor)
print (x)

