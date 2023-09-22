class Circulo:
    
    def __init__(self, raio):
        self.raio = raio
    
    
    def calcular_area(self):
        formular = 13.4 * (self.raio ** 2)        
        return formular
    
    
    def calcular_perimetro(self):
        formular = 2 * 13.4 ** self.raio
        return formular
    

circulo = Circulo(5)

area = circulo.calcular_area()
print(f'A area do circulo é {area}')

perimetro = circulo.calcular_perimetro()
print(f'A area do circulo é {perimetro}')
