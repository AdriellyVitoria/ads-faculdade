from os import system


def escrever_no_arquivo(file):
    # Criar o arquivo e fechar ao final da execução
    arquivo = open(file, 'w')
    # Qual a quantidade de endereços IP que serão lidos
    qtda = int(input('Informe a quatidade de linhas para a entrada: '))
    system('clear')
    # Loop para fazer a leitura dos IPs
    for num in range(qtda):
        # Lendo um IP por linha
        print(num+1, end=" ")
        arquivo.write(f'{input()}\n')
    # Fechando o arquivo
    arquivo.close()

def ler_no_arquivo(file):
    # Abrindo o arquivo para leitura
    arquivo = open(file, 'r')
    # Percorrendo a lista para avaliar cada IP
    for item in arquivo:
        print(item.upper())

    # Fechando o arquivo
    arquivo.close()


def buscar(file, nome):
    arquivo = open(file, 'r')

    for item in arquivo:
        if item == nome.upper():
            return True
        else:
            return False


while True:
    try:
        # Listar opções para o usuário decidir
        print('1 - Criar e Escrever\n2 - Ler Arquivo\n3 - Buscar\n4 - Sair')
        opcao = int(input('> '))

        # Tratar as opções
        if opcao == 1:
            # Pedir o nome do arquivo
            arquivo = input('Informe o nome do arquivo: ')
            system('clear')
            # Invocando a função de escrita no arquivo
            escrever_no_arquivo(arquivo)

        elif opcao == 2:
            # Pedir o nome do arquivo
            arquivo = input('Informe o nome do arquivo: ')
            system('clear')
            # INvocando a função de leiura do arquivo
            ler_no_arquivo(arquivo)
            input('Pressione qualquer tecla para continuar...')
            system('clear')

        elif opcao == 3:

            arquivo = input('Informe o nome do arquivo: ')
            nome = input('Informe o nome para a busca: ')

            if buscar(arquivo, nome):
                print(nome)
            else:
                print('Nome não encontrado!')

        elif opcao == 4:
            # Finalizando o loop
            system('clear')
            break

    except ValueError:
        print('ERRO!! tente novamente')