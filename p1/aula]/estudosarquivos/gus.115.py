#criar um menu(ver pessoas cadadrata, cadrata pessoas e sair do sistemas) para cadrastra pessoas 
lista = []

while True:
    print('-' * 30)
    print('      MENU PRINCIPAL    \n1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoas\n3 - Sair do sistema')
    print('-' * 30)

    opcao = int (input ('Sua opção: '))

    if opcao == 1:
        if len(lista) == 0:
            print('Zero pessoas foram cadastrada')
        else:
          arquivos= open('cadastra', 'r')

    elif opcao == 2:
        quantidade = int (input ('Quantas pessoas vc deseja cadastra: '))

        for i in range(quantidade):
            arquivos = open('cadastra.txt','w')
            arquivos.white(f'{input ('Nome da pessoas para o cadastrame')})
    
            idade = int (input('idade da pessoa para o cadastramento: '))
        arquivos.clase()
    else:
        print('Sair do programa... volte sempre!!')
        break