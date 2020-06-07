![](https://joseluisramoncolmenares.files.wordpress.com/2020/06/joseluiramon-diploma-poo-python.png)

# Programación Orientada a Objetos y Algoritmos en Python

**Prof. David Aroesti**

## Unidad 1. Programación Orientada a Objetos

Uno de los objetos más importante de los lenguajes de programación es la utilización de clases para organizar programas en módulos y abstracciones de datos. 

La clave para entender la programación orientada a objetos es pensar en objetos como agrupaciones de datos y los métodos que operan en dichos datos.

Por ejemplo, podemos representar a una persona con propiedades como nombre, edad, género, etc. y los comportamientos de dicha persona como caminar, cantar, comer, etc.

Puesto de otra manera, la programación orientada a objetos nos permite modelar cosas reales y concretas del mundo y sus relaciones con otros objetos.

> “Los objetos son las principales cosas que un programa de Python manipula. Cada objeto tiene un tipo que define qué cosas puede realizar un programa con dicho objeto.”

### Clases en Python

Las clases nos permiten crear nuevos tipos que contiene información arbitraria sobre un objeto. En el caso del hotel, podríamos crear dos clases `Hotel()` y `Cuarto()` que nos permitiera dar seguimiento a las propiedades como número de cuartos, ocupación, aseo, tipo de habitación, etc.

Las clases sólo proveen estructura. Son un molde con el cual podemos construir objetos específicos. La clase señala las propiedades que los hoteles que modelemos tendrán, pero no es ningún hotel específico. Para eso necesitamos las instancias.

#### Instancias

Mientras que las clases proveen la estructura, ==las instancias son los objetos reales que creamos en nuestro programa:== un hotel llamado PlatziHotel o Hilton. Otra forma de pensarlo es que **las clases son como un formulario**. Cada copia del formulario que es rellenada es una instancia, que como se pque pertenecen a dicha clase. Cada copia del "formulario" puede tener datos distintos, al igual que cada instancia es distinta de las demás (aunque todas pertenecen a una misma clase o "formulario").

Para definir una clase, simplemente utilizamos el *keyword* `class`. Por ejemplo:

```Python
class Hotel:
    pass
```

Una vez que tenemos una clase llamada `Hotel` podemos generar una instancia llamando al constructor de la clase.

```Python
hotel = Hotel()
```

#### Atributos (de instancia)

Todas las clases crean objetos y todos los objetos tienen atributos. ==Utilizamos el método especial `__init__` para definir el estado inicial de nuestra instancia.== Recibe como primer parámetro obligatorio `self` (que es simplemente una
 referencia a la instancia).

```Python
class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        
        # inicializar variables de instancia
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
```

#### Métodos (de instancia)

Mientras que los atributos de la instancia describen lo que representa el objeto, ==los métodos de instancia nos indican qué podemos hacer con las instancias de dicha clase== y normalmente operan en los mencionados atributos. Los métodos son equivalentes a funciones dentro de la definición de la clase, pero todos reciben `self` como primer argumento.

```Python
class Hotel:

    ...

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2
```

### Tipos de datos abstractos y clases. Instancias

* En Python todo es un objeto y todo tiene un tipo. Ej. `list` , `range` , `str` , etc
  * **Todo es un objeto: **Todo lo que nosotros hacemos dentro de nuestro programa tienen un representación en memoria.
  * **Todo tiene un tipo:** Podemos encapsular los datos y el comportamiento adentro de un sólo objeto.
  * Los objetos se usan para la representación de datos y hay diversas formar de interactuar con ellos. 

> **En la programación conocemos estos tipos de datos que tu creas como =="tipos de datos abstractos"==.**

#### Ejemplo

Pongamos como ejemplo la creación de un *restaurante*

* Existen diversas formas de interactuar con un objetos
  * **Crearlos.** Ej. Una vez has creado el método puedes crear cuando restaurantes quieras.
  * **Manipularlos.** Ej. Por medio de la manipulación de sus atributos puedes crear restaurantes de comida italiana, mexicana, china, etc
  * **Destruirlos.** Ej. Un restaurante X puede cerrar y se deja de utilizar. En Python cuando un objeto pierde todas sus referencia es eliminado por el *garbage collector*

* Cuando tenemos objetos tenemos varias ventajas
  * **Podemos Decomponerlos**. Ej. Silla, mesas platos, mesoneros, cocineros
  * **Usar sus Abstracciones.** Ej. Si alguien quiere ordena una hamburguesa no es necesario explicar de donde viene la hamburgues ni como se prepara. Por medio de un método puedes crearla y listo
  * **Encapsular**. Esconder datos que no son importantes para las personas que utilizan nuestros objetos

### Creación de Datos Abstractos

```python
# Definición de clase

class <nombre_de_la_clase>(<super_clase>):
    def __init__(self, <params>): #es una buena práctica tener el self cuando describas una clase.
        <expression>
    def <nombre_del_método>(self, <params>):
        <expression> #que hace este método cuando se ejecuta
```

### Instancias

* ==Mientras que la clase es un molde, a los objetos creados se les conoce como **instancias**.==. Ejemplo. La clase es el molde de la botella, y la instancia es cada botella que produces. Puedes tener botella rojas, azules, pero el molde es el mismo. La clase es la forma en la que se generan las instancias
* ==Cuando se crea una instancia, se ejecuta el **constructor**== o el método `__init__` (se lee como *"dunder init"* =  *double underscore - init*)
* Todos los métodos de una clase reciben implícitamente como primer parámetro `self`
* Se accede a los atributos por la notación de punto. Los atributos de clase nos permiten: 
  * Representar datos. Ejemplo. Variables de instancia: `self.<nombre_de_variable>`
  * Procedimientos para interactuar con los mismo (métodos). Ej.  `def nombre_metodo(self, atributuro):`  
  * Mecanismos para esconder la representación interna. Lo cuales se conocen como **variables privadas**. Para tener atributos privados. Por convención comienza con `_`.

Por medio del método`isintance()` se puede comprobar su un objeto es una instancia de una clase dada. Por ejemplo .  `  print(isinstance(coord_2, Coordenada)) ` .

### Descomposición

* Partir un problema en problemas más pequeño
* Las clases permiten crear mayores abstracciones en forma de componentes, nos permiten generar componente más pequeños.
* Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener. Nos ayuda a mantener el software de manera más sencilla

==Crear clases muy extensas es una mala práctica==

> Las clases permiten agarrar un problema muy grande y generar clases más pequeñas que es un conjunto nos permiten resolver problemas

La descomposición nos ayudar a mantener el código. Las clases muy grande son muy pesadas de entender y mantener

Dentro del 

### Abstracción

Lo que estamos tratando de lograr con estas clases es **dotarte de herramientas conceptuales** para que tu puedas traducir la forma en que tu modelas el mundo a código

La abstracción es

* Enfocarnos en la información relevante. 
* Separa la información central (relevante) de los detalles secundarios. 
* Podemos utilizar variables y métodos (privados o públicos)

Nosotros nos estamos preocupando como funcionan internamente las neuronas de las personas cuando nos comunicamos.

**Para traducir estas cosas a una abstracción es por medio de una interfaz.** A nosotros nos interesa saber como interactuamos con los servidores, librerías y demás algoritmos para analizar datos. S tuviéramos que saber a detalle cómo funcionan todas las disciplinas y algoritmos que tenemos nos sería imposible poder hacerlo.  

Por eso vamos a ver como generar un clase que nos permita hacer ciertas abstracciones y que tenga una interfaz que nos permita modificarlas

```python
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = 'caliente'):
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
        
```

Contantemente tenemos que pensar qué interfaz le entregamos al usuario

* Si estamos definiendo movimientos, nos basta buscar relaciones del tipo `Fuerza = masa*aceleración`

Comienza a descomponer al mundo de esta manera. Ve analizando los sistemas que están a tu alrededor. 