def criar_conta(numero, titulo, saldo, limite):
    conta = {"numero ": numero, "titulo ": titulo, "Saldo ": saldo, "limite ": limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor
    
def sacar(conta, valor):
    conta['saldo'] -= valor