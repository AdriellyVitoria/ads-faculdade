lista = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
giros = 0
for i in range (len(lista)):
    for j in range (len(lista)):
        i = str (i)
        j = str (j)
        print (f'{i}{j}', end=' ')
        giros += 1
        if giros == 3:
            print ( )
            giros = 0
   #quero q pegue 3 em 3 