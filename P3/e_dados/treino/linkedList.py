lista = []

class Lista:
    def __init__ (self, nome):
        self.nome = nome
        
    def add_nomes(self):
        lista.append(self.nome)
            
nome = Lista("Adrielly")
nome.add_nomes()

nome2 = Lista("Mateus")
nome2.add_nomes()

print(lista)         