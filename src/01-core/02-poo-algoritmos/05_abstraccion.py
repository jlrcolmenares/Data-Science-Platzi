class Lavadora:
    """ Clase de atributos relacionados con una lavadora
    >> lavadora = Lavadora() 

    """
    def __init__(self):
        pass

    def lavar(self, temperatura = 40):
    #tenemos que empezar que es lo que significa el ciclo de lavado
    #al usuario le interesa darle click a lavar luego de elegir la temperatura
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._enjuagar_lavar()
        self._centrifugar()
        #del mismo modo así se programan la lavadoras reales. Descomponiendo en etapas y luego programando cada etapa

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua a {temperatura} C')

    def _anadir_jabon(self):
        print(f'Anadiendo jabon')
    
    def _enjuagar_lavar(self):
        print(f'Enjuagando la ropa')
    
    def _centrifugar(self):
        print(f'centrifugando')

#Si un archivo se ejecuta desde aquí es que vamos a comenzar
if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar(60)
    help(Lavadora)
        