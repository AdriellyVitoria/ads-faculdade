estoque = {}

class Loja:
    def __init__ (self, produto, preco, quantidade):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
    
    def adicionar_produto(self):
        if self.produto in estoque:
            estoque[self.produto]["quantidade"] += self.quantidade
        else:
            estoque[self.produto] = {"quantidade": self.quantidade, "preco": self.preco}
            
            
teste = Loja("not", 100, 2)
teste.adicionar_produto()

teste2 = Loja("not", 100, 2)
teste2.adicionar_produto()
print(estoque)        