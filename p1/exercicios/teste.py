# Escreva um programa que solicite ao usuário o nome e a idade de várias pessoas. Armazene essas informações em um dicionário, onde o nome é a chave e a idade é o valor. O programa deve permitir ao usuário adicionar novas pessoas, consultar a idade de uma pessoa existente e listar todas as pessoas e suas respectivas idades.

# pessoas = {}
# while True:
#     print('''\n=== Menu ===\n
#     1. Adicinar pessoas
#     2. Consultar idade
#     3. Listar pessoas
#     4. Sair''')
#     opcao = int(input("Digite o número da opção desejada: "))

#     if opcao == 1:
#         nome = input("Dige o nome: ")
#         idade = int (input("Digite a idade: "))
#         pessoas[nome] = idade
#         print("Pessoas add com sucesso")

#     elif opcao == 2:
#         nome = input("Digite o nome da pessoas: ")
#         if nome in pessoas:
#             idade = pessoas[nome]
#             print(f"A idade de {nome} e {idade}")
#         else :
#             print("pessoa não encontrada!!")

#     elif opcao == 3:
#         print("Lista de Pessoas ")
#         for nome, idade in pessoas.items():
#             print(nome, "-" , idade, "anos")

#     elif opcao == 4:
#         print ("Saindo do programa")
#         break     
#     else:
#         print("opção de invalida")



alunos = {}

while True:
    print("""
    ----Menu de opções----
    
    Adiconar aluno
    Visualizar alunos
    Sair
    """)

    opcao = int(input("Digite o numero da opcao que voce deseja: "))

    if opcao == 1:
        nome = input("nome: ")
        idade = int(input("idade: "))
        curso = input("curso: ")
        aluno = {'nome': nome, 'idade': idade, 'curso': curso}
        alunos[nome] = aluno


    elif opcao == 2:
        for nome, aluno in alunos.items():
            print("Nome:", nome)
            print("Idade:", aluno['idade'])
            print("Curso:", aluno['curso'])
            print("------------------")

    elif opcao == 3:
        print("saindo do programa")
        break

      