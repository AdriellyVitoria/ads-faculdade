fila = []

class Fila:
    def __init__ (self, pedido):
        self.pedido = pedido
    
    def adicionar_pedido(self):
        fila.append(self.pedido)
    
    def tamanho_da_lista(self):
        tamanho = len(fila)
        return tamanho
        
    def remover(self):
        if self.pedido in fila:
            fila.remove(self.pedido)    
    
    def verificar(self):
        if fila == {}:
            print(True)
        else:
            print(False) 
            
            
            
fila = Fila("Hamburguer")

# fila.adicionar_pedido()
# fila.adicionar_pedido("Pizza")
# fila.adicionar_pedido("Sorvete")
print(fila.adicionar_pedido())

print(fila.tamanho_da_lista())  # Deve imprimir 3

print(fila.remover())  # Deve imprimir "Hamburguer"

print(fila.verificar())  # Deve imprimir False            