valor = float(input())

valor100 = valor // 100
resto100 = valor % 100
valor50 = resto100 // 50
resto50 = resto100 % 50
valor20 = resto50 // 20
resto20 = resto50 % 20
valor10 = resto20 // 10
resto10 = resto20 % 10
valor5 = resto10 // 5
resto5 = resto10 % 5
valor2 = resto5 // 2
resto2 = resto5 % 2
#moedas

valor1 = resto2 // 1
resto1 = resto2 % 1
valor050 = resto1 // 0.5
resto050 = resto1 % 0.5
valor025 = resto050 // 0.25
resto025 = resto050 % 0.25
valor010 = resto025 // 0.1
resto010 = resto025 % 0.1
valor005 = resto010 // 0.05
resto005 = resto010 % 0.05
valor001 = resto005 / 0.01


print('NOTAS:')
print(f'{valor100:.0f} nota(s) de R$ 100.00')
print(f'{valor50:.0f} nota(s) de R$ 50.00')
print(f'{valor20:.0f} nota(s) de R$ 20.00')
print(f'{valor10:.0f} nota(s) de R$ 10.00')
print(f'{valor5:.0f} nota(s) de R$ 5.00')
print(f'{valor2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{valor1:.0f} moeda(s) de R$ 1.00')
print(f'{valor050:.0f} moeda(s) de R$ 0.50')
print(f'{valor025:.0f} moeda(s) de R$ 0.25')
print(f'{valor010:.0f} moeda(s) de R$ 0.10')
print(f'{valor005:.0f} moeda(s) de R$ 0.05')
print(f'{valor001:.0f} moeda(s) de R$ 0.01')