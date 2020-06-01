# 1) Tenemos una clase que se llama coordenada
class Coordenada:
        
        # 2) La clase tiene sus variables
        def __init__(self, x, y):
            self.x = x
            self.y = y

        #3) También tiene sus métodos
        def distancia(self, otra_coordenada):

            #teorema de pitagoras
            x_diff = (self.x - otra_coordenada.x)**2 
            y_diff = (self.y - otra_coordenada.y)**2 

            return (x_diff + y_diff)**0.5 

# 6) Inicializar nuestro programa. Si el archivo se ejecuta directamente desde la terminal nosotros lo podemos correr
if __name__ == '__main__':

    # 4) Esto nos permite definir varias instancias
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    # 5) Accediendo a sus métodos también
    #print(coord_2.distancia(coord_1))
    print (isinstance(coord_2, Coordenada))

