class Pessoa:
    def __init__ (self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profisao = profissao
        
    def apresentar(self):
        resultando = print(f'Olá meu nome é: {self.nome}, Tenho {self.idade}, hoje trabalho com {self.profisao}')
        
        return resultando
    
pessoa1 = Pessoa("Adrielly", 21, "Programação")
teste1 = pessoa1.apresentar()

pessoa2 = Pessoa("Castiel", 4, "Ser lindo")
teste2 = pessoa2.apresentar()