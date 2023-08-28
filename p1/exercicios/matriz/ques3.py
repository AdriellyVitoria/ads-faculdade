#Adapte a função gerar_matriz da questão 1 para que ela leia os valores informados pelo usuário. Em seguida, crie uma segunda função que recebe a matriz gerada e retorne o número de linhas e colunas que tem apenas zeros.

def gerar_matriz(m, n, x):
    agru = []
    for i in range (m):
        lista = []
        for j in range (n):
            lista.append(x)
        agru.append(lista)  

    matriz (m, n, 0)

def matriz (m, n, x):
    agru = []
    for i in range (m):
        lista = []
        for j in range (n):
            lista.append(x)
        agru.append(lista)  

    return agru

linha, coluna, valor = map (int, input ().split ())
chamar = gerar_matriz (linha, coluna, valor)
print (chamar)

