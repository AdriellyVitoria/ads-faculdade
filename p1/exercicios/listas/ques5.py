#Agora imagine uma pilha de pratos. Os pratos lavados são retirados do topo da pilha e os pratos sujos são colocados no topo da pilha. A diferença entre pilhas e filas é de onde o elemento é retirado: na fila é o primeiro, enquanto que na pilha é o último. Implemente um programa semelhante ao anterior (fila de banco) usando como "menu" as seguintes opções: E - Empilhar D - Desempilhar S - Sair

lista = []
conta = 0
while True:
    print ('=-' * 30)
    print ('\nMENU\nE - Empilhar\nD - Desempilhar\nS - Sair:')
    print ('=-' * 30)
    opção = input ('Escolhe opcão: ').upper()
     
    if opção == 'E':
        conta += 1
        lista.append(conta)
        print (f'tem {len(lista)} pratos na pilha')
    
    elif opção == 'D':
        if lista == []:
            print ('Não tem nenhum prato')
        else:
            lista.pop()
            print (f'Agora tem {len(lista)} na pilha')
        
    elif opção == 'S':
      break

    else:
        print ('ERRO, TENTE NOVAMENTE')

