class CasillaVotacion:
    
    def __init__(self, indentificador,pais):
        self._identificador = indentificador
        self._pais = pais
        self._region = None
    @property #getter
    def region(self):
        return self._region
    @region.setter
    def region(self,reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self._pais}')
    #defino un método
    
    def cambiar_identificador(self):
        nuevo = int(input(f'introducir nuevo identificador: '))
        self._identificador = nuevo
        return self._identificador

if __name__ == "__main__":

    casilla = CasillaVotacion(123,['Bogota','Medellin'])
    print(casilla.region)
    casilla.region = 'Bogota'
    print(casilla.region)
    #No entiendo porqué el profesor dice que a las propiedades se accede sólo con el dot notation cuando los métodos son iguales
    casilla.cambiar_identificador()
    print(casilla._identificador)