class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo' #variable privada
        self._motor = Motor(cilindros = 4)
        self._frenos = Frenos(2,2,'nula')

    	
    #cosas que se pueden hacer con el automovil    
    def acelerar(self, tipo= 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'desplazandose'

    def velocidad(self ,kmph = 0):
        if acelerar('despacio') == True:
            self.kmph = 10
        else: #acelerar._tipo == 'rapida'
            self.kmph = 20

    def frenar(self, presion = 'nula'):
        if presion == 'suave':
            self._motor.inyecta_gasolina(1)
            velocidad.kmph -= 5
        elif presion == 'fuerte':
            self._motor.inyecta_gasolina(0)
            velocidad.kmph -= 12
        else:
            pass

class Motor:
    
    def __init__(self, cilindros, tipo = 'gasolina'): # parámetro por defecto 'tipo'
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass


class Frenos:

    def __init__(self, discos = 2, tambores = 2, presion = 'nula'):
        self.discos = discos
        self.tambores = tambores
        self.presion = presion

    def activar_frenos():
        self.discos._activar = True
        self.tambores._activar = True
    


