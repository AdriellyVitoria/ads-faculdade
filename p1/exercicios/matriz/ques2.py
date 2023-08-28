#Crie uma função que imprima a seguinte matriz de inteiros [[0, 0, 0], [1, 1, 1], [2, 2, 2]].

def matriz ():
    agru = []
    x = 0

    while x <= 2:
        giros = 0

        lista = []
        while giros < 3:
            lista.append(x)       
            giros += 1
        agru.append(lista)  
        x += 1    
    return agru

y = matriz ()
print  (y)
