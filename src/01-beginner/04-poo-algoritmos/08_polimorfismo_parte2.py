class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base*2 + self.altura*2

class Cuadrado(Rectangulo): 
    def  __init__(self,lado):
        super().__init__(lado, lado) #se llama al constructor de la superclase

class Romboide(Rectangulo):
    def __init__(self, base, altura):   # esta clase, tienen dos atributos de entrada
        super().__init__(base, altura)  # se corresponden a los lados de la superclase
    
    def perimetro(self): # esta función ya existía en la superclase pero la podemos definir nuevamente cambiado su definición
        print('calculado perimetro...')
        return (self.base*2 + self.altura*2)


if __name__ == "__main__":
    rectangulo = Rectangulo( base = 3, altura = 4)
    print('area: ', rectangulo.area())
    print('perimetros: ', rectangulo.perimetro())

    cuadrado = Cuadrado(lado = 5)
    print('area cuadrado: ',cuadrado.area()) #lo interesante ocurre aqui
    # esto funciona porque estamos heredando el método area() del rectángulo
    # no hizo falta definir este método dentro de la clase Cuadrado

    romboide = Romboide( base = 6, altura = 4)
    print('area romboide: ', romboide.area()) 
    print(romboide.perimetro())