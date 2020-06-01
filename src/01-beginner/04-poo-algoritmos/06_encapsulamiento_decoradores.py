class Perros(object): #Declaramos la clase principal Perros
    def __init__(self, nombre, peso): #Definimos los parámetros 
        self.__nombre = nombre #Declaramos los atributos (privados ocultos)
        self.__peso = peso
    
    @property
    def nombre(self): #Definimos el método para obtener el nombre
        "Documentación del método nombre bla bla " # Doc del método
        return self.__nombre #Aquí simplemente estamos retornando el atributo privado oculto
 
    #Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
    #Ahora vamos a utilizar setter y deleter para modificarlos
 
    @nombre.setter #Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por ",self.__nombre) #Aquí vuelvo a pedir que retorne el atributo para confirmar
    
    @nombre.deleter #Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
 
    #Hasta aquí property#
 
    def peso(self): #Definimos el método para obtener el peso
        return self.__peso #Aquí simplemente estamos retornando el atributo privado


if __name__ == "__main__":
    #Instanciamos
    Tomas = Perros('Tom', 27)
    print (Tomas.nombre) #Imprimimos el nombre de Tomas. Se hace a través de getter
    #Que en este caso como esta luego de property lo toma como el primer método..
 
    Tomas.nombre = 'Tomasito' #Cambiamos el atributo nombre que se hace a través de setter
    del Tomas.nombre #Borramos el nombre utilizando deleter    
    
    # Esto debería dar error, por ser atributo privado y no existe metodo para acceder a el
    print(Tomas.peso)
    #print(Tomas.__peso) # DA ERROR
    print(Tomas._Perros__peso) # Se accede pero NO es la forma correcta


