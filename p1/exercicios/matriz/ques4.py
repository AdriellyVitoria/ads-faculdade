#Desenvolva uma função gerar_intervalo_paginas(inicio, final) que, dado um intervalo de páginas, retorne dois vetores com os números das páginas que devem ser encaminhados para a impressora. Por exemplo: [97, 98, 101, 102, 105, 106, 109, 110, 113, 114, 117, 118, 121, 122, 125, 126, 129, 130, 133, 134] e [99, 100, 103, 104, 107, 108, 111, 112, 115, 116, 119, 120, 123, 124, 127, 128, 131, 132, 135, 136]



#quero q pegue dois numero em uma lista dps pegue mais dois numeor para a proxima lista

intervalo = []
outro = []
inicial, final = map (int, input ().split ())

while inicial <= final:
    intervalo.append(inicial)
    if inicial <= final:
        inicial += 1
        intervalo.append(inicial)

    inicial += 1
    outro.append(inicial)
    if inicial <= final:
        inicial += 1
        outro.append(inicial)
        inicial += 1

print (f'{intervalo} e {outro}')
