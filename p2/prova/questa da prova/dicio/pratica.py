from os import system
system('clear')

# tabelas = {
#     'hamburguer': 15.99, 'batatinha': 7.98, 'refrigerante': 5.00
# }

# print (tabelas) #saida da tabela completa, um ao lado do outro
# #tabelas[suco]

# for produto in tabelas:
#     #print(tabelas[produto]) #pegar os preços
#     #print (produto) #pegar só os produtos
#     #print (tabelas['hamburguer']) #chamar só o preço do hamburguer

#uma dici e dentro uma lista

# locadora = {
#     'acao': ['007', 'MIB', 'JW', 'kingsman'],
#     'infantil': ['Carros', 'Madagas', 'Turbo']
# }

# genero = input ('Qual o genero vc quer? ')
# #for genero in locadora:
#     #print (locadora[genero])
# print (locadora[genero])

produtos = {
    'alface': 0.45,
    'batata':1.20,
    'cenoura': 4.23,
    'cebola': 3.00
}

# for chave in produtos.keys():
#     print ()
    # print (produtos.keys()) #mostras os nomes
    # print (produtos.values()) #mostra os valores

# produtos.pop('alface') #retirar
# print (produtos.keys())

# del produtos['batata'] #retira
# print (produtos.keys()) 

# produtos['farinha'] = 1.00 #add
# print (produtos.keys())

#\t = para dá quantidade de espaços
for chave in produtos:
    print(f'{produtos[chave]:.2f} \t {chave}') #inverter os valores do dicionario

#