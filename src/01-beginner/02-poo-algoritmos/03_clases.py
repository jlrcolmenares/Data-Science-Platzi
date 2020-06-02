class Supermercado():
    '''
        Instancia de supermercados, tienen las funciones básicas de todo supermercado
        
        >>> mercado 1 = Supermercado(productos=dict(), empleados=list(), compradores=list())
    ''' 
    def __init__(self, productos, empleados, compradores):
        self.productos = productos
        self.empleados = empleados
        self.compradores = compradores
        self.abierto = True # indica si está abierto o cerrado
        self._saldo_cuenta = 300    #atributo protegido
        self.__propietario = 'Jose Colmenares'

    def cargar_productos(self,productos_precios):
        # pruebo el funcionamiento de las excepciones
        try:
            # actualizo los productos
            return self.productos.update(productos_precios) 
        except ValueError as problem:    # se imprimer la excepción si se introduce un valor inválido
            print('Entrada no válida')
            print(problem)
            return self.productos

    def subir_nomina(self,lista_empleados):
        # pruebo el funcionamiento de las afirmaciones
        assert type(lista_empleados) == list, 'Tiene que ser una lista'
        self.empleados = lista_empleados 
        return self.empleados


if __name__ == "__main__":
    
    # se crea una instancia de supermercado de nombre 'mercadonut'
    mercadonut = Supermercado(productos=dict(), empleados=list(), compradores=[])

    # lista de empleados
    nomina = ['Ana Maria Guerrero','Vicente Almeida','Juan Alberto Donoso']
    # cargar empleados (sin diferenciación de cargos)
    print(mercadonut.subir_nomina(nomina))
    
    # lista de productos iniciales con su precio
    productos1= {'leche':20,
                 'chocolate':30,
                 'harina':60,
                 'huevos':40}
    # función para cargar los productos
    mercadonut.cargar_productos(productos1)
    print('Productos existentes: \n', mercadonut.productos)

    productos2 = {'yogurt':100}
    # probamos el funcionamiento de la función update(dict)
    mercadonut.cargar_productos(productos2)
    print('Productos existentes: \n', mercadonut.productos)
    
    print('*' * 30) # separador de secciones
    
    print('mercadonut es instancia de Supermercado? ',isinstance(mercadonut,Supermercado))
    
    # help(Supermercado) # nos muestra la documentación que hemos creado

    #probamos condiciones atributos proteegidos y privados
    #print(mercadonut.empleados, mercadonut._saldo_cuenta, mercadonut.__propietario)  #el atributo propietario no puede ser accesado
    # forma de acceder a un atriibuto privado, que NO ES CORRECTA pero se puede
    mercadonut._Supermercado__propietario = 'Vicente Herrera'
    print(mercadonut._Supermercado__propietario)


