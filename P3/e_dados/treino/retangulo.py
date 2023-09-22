class Retangulo:
    
    def __init__ (self,largula, altura):
        self.largula = largula
        self.altura = altura
     
    def calcular_area(self):
        Resultando = self.largula * self.altura
        return Resultando
    
    def calcular_perimetro(self):
        resultando = 2 * (self.largula + self.altura)
        return resultando
    
teste = Retangulo(4, 5) #Criou o objeto em py

#ordem objeto e atributo
print(f'resultando {teste.calcular_area()}')  
       