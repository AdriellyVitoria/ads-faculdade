valor = float(input())

valor100 = valor // 100
resto100 = int (valor % 100)
valor50 = resto100 // 50
resto50 = int (resto100 % 50)
valor20 = resto50 // 20
resto20 = int (resto50 % 20)
valor10 = resto20 // 10
resto10 = int (resto20 % 10)
valor5 = resto10 // 5
resto5 = int (resto10 % 5)
valor2 = resto5 // 2
resto2 = int (resto5 % 2)

#moedas

valor1 = resto2 // 1
resto1 = int (resto2 % 1)

centavos = round (resto1 * 100, 0)

valor050 = centavos // 50
resto050 = int (resto1 % 50)
valor025 = resto050 // 25
resto025 = int (resto050 % 25)
valor010 = resto025 // 1
resto010 = int (resto025 % 10)
valor005 = resto010 // 5
resto005 = int (resto010 % 5)
valor001 = resto005 / 1

print('NOTAS:')
print(f'{valor100:.0f} nota(s) de R$ 100.00')
print(f'{valor50:.0f} nota(s) de R$ 50.00')
print(f'{valor20:.0f} nota(s) de R$ 20.00')
print(f'{valor10:.0f} nota(s) de R$ 1..00')
print(f'{valor5:.0f} nota(s) de R$ 5.00')
print(f'{valor2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{valor1:.0f} moeda(s) de R$ 1.00')
print(f'{valor050:.0f} moeda(s) de R$ 0.50')
print(f'{valor025:.0f} moeda(s) de R$ 0.25')
print(f'{valor010:.0f} moeda(s) de R$ 0.10')
print(f'{valor005:.0f} moeda(s) de R$ 0.05')
print(f'{valor001:.0f} moeda(s) de R$ 0.01')

# 576.73
# NOTAS:
# 5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01