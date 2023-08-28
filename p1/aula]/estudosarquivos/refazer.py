#criar um menu de criar arquivos, ler arquivos, buscar arquivos e o nome do arquivo, sair... cada entro de uma função

from os import system

def criar_arquivo(nome):
    arquivos = open(nome, 'w')
    linha = int (input('quantas linhas deseja escreve? '))
    system('clear')
    for num in range(linha):
        print(num+1, end='')
        arquivos.write(f'{input()}\n')
    arquivos.close()


def ler_arquivo(arquivo):
    arquivo = open(arquivo, 'r')
    for item in arquivo:
        print(item.upper())

def buscar_arquivos(nome):
    arquivo = open(nome, 'r')

    for item in arquivo:
        if item == nome.upper():
            return True
        else:
            return False


while True:
    try:
        print('1 - Criar arquivo\n2 - Ler arquivo\n3 - Buscar arquivo\n4 - Sair')
        opcao = int (input ('> '))

        if opcao == 1:
            arquivos = input('Informe o nome do arquivo: ')
            criar_arquivo(arquivos)
        elif opcao == 2:
            ler = input('Qual o nome do arquivo q vc deseja ler: ')
            ler_arquivo(ler)
        elif opcao == 3:
            buscar = input('O que vc deseja buscar? ')
            buscar_arquivos(buscar)
        elif opcao == 4:
            print('fim do programar')
            system('clear')
            break
        
    except ValueError:
        print("ERRO, tente novamente")
