![](https://joseluisramoncolmenares.files.wordpress.com/2020/05/joseluisramon-diploma-python-cs.png)

# Introducción al Pensamiento Computacional con Python

**Prof. David Aroesti**

## Unidad 2. Introducción a Python

### Elementos de un lenguaje

Todo lenguaje está compuesto por ==**literales, operadores y enunciados (statements).**==

```python
# <literales> = 1, 'abc'
# <operadores> = + / ** ==
# SINTAXIS
# <literal> <operador> <literal>


1 + 2 # expresión correcta
1 3.0 # error sintáctico (no cumple sintaxis)
5 / 'platzi' # error semántico estático, cumple con sintaxis pero no tiene sentido
5 * 'Platzi' # expresión correcta
```

## Unidad 3. Programas Numéricos

### Búsqueda Binaria

Uno de los algoritmos más importante y eficientes de computer science es este. Se basa en:

* Uno de los requisitos es que el conjunto de búsqueda esté ordenado. (numero reales y enteros.
* Es altamente eficientes, pues corta el espacio de búsqueda en dos por cada iteración

**Ejemplo**

Encontrar raíz cuadrada

```python
objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2 #en cada iteración estamos dividiendo entre 2 nuestro espacio de búsqueda
    

print(f'La raiz cuadrada del {objetivo} es {respuesta}')
```

No siempre es posible hacer esto, es obligatorio que sea un conjunto ordenado, sin embargo, siempre que se pueda, es maravillosa herramienta

## Unidad 4. Funciones, alcance y abstracción

Los lenguajes de programación modernos nos dan abstracciones que nos permiten modularizar el código, que nos permiten modularizar secciones.

#### Abstracciones

Una abstracción significa que tu no necesitas entender la forma en que algo opera internamente para poderla utilizarlo. Ej. No necesitas saber como está escrito el electrónica interna de una calculadora para poder utilizarla ==necesitas saber como operarla==. Pasa con los coches también, por ejemplo. 

Una de las habilidades más importantes de los ingenerio del software es utilizar esta abstracciones. Recuerda que vas a utilizar librería de otras personas y tienes que saber como utilizarlo. Ej. No te interesa saber como está construido Apache, te interesa saber como utilizarl

#### Decomposición

* Nos permite dividir el código en unidades lógicas, en compoentes que colaboran con un fin en común
* Se puede pensar como mini programas de un programa mayor. 

## Unidad 5. Tipos estructurados, mutabilidad y funciones de alto nivel

Una de las características más poderosas de Python es que todo es un objeto, incluyendo las funciones. Las funciones en python son “ciudadanos de primera
 clase.”

Esto, en sentido amplio, significa que en Python las funciones:

- Tienen un tipo
- Se pueden pasar como argumentos de otras funciones
- Se pueden utilizar en expresiones
- Se pueden incluir en varias estructuras de datos (como listas, tuplas, diccionarios, etc.)

### Funciones como argumentos

Un ejemplo bien ilustrativo es

```python
def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

>>> nums = [1, 2, 3]
>>> aplicar_operacion(multiplicar_por_dos, nums)
[2, 4, 6]

>>> aplicar_operacion(sumar_dos, nums)
[3, 4, 5]
```

En este ejemplo la función `aplicar_operación` recibe una función como argumentos (f) y un número. La función, como se observa en el primer cado es `multiplicar_por_dos`. Multiplicar por dos necesita un N como un argumento para funcionar. Entonces, el ciclo for llama a cada uno de los iterables dentro de la lista `nums`. (declarada dentro de la función como `numeros` ) y les aplica la función y hace append en el arreglo `resultado`

### Funciones en expresiones

una forma de definir una función en una expresión es utilizando el keyword `lambda`. ==`lambda` tiene la siguiente sintaxis: `lambda : <vars>: <expresion> `.==

```python
#declaración
sumar = lambda x, y: x + y

>>> sumar(2, 3)
5
```

### Listas y Mutabilidad

Las listas es el primer objeto propio de Python que goza de mutabilidad. Las listas

* Son secuencias de objetos, pero a diferencia de las tuplas, si son mutables. Esto a nivel memoria significa que puede ir creciendo.
* Cuando modificar una lista, pueden existir efectos secundarios (*side effects*). Uno de los riesgos de mutar un elementos es que puede tener problemas con la memoria 
* Es posible iterar con ellas. Para ellos podemos utilizar un *for loop*

* Para modificar una lista podemos
  * Modificar un elementos
  * Utilizar los [métodos](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

EJEMPLOS

```python
>>> my_list= [1,2,3] #DECLARACIÓN DE UNA LISTA
>>> type([1,2,3])
<type 'list'>
#funciones para la modificación
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> my_list[0] = 'a'
>>> my_list
['a', 2, 3, 4]
>>> my_list.pop()
4
>>> my_list
['a', 2, 3]
```

## Unidad 6. Pruebas y Debugging

Algo con la que vas a toparte y te vas a seguir topando son bugs. Voy a darte herramientas para que puedas aprender a hacer pruebas del código y para aprender técnicas para encontrar de manera eficiente y sistemática los errores dentro del código

### Pruebas de caja negra

* Se basan en la especificación de la función o el programa. Es decir, que no conocemos el valor
* Prueba inputs y valida output. De nuevo, no conocemos el código
* Estos tiene que ver con dos palabras claves en la industria de la computación. Los unit testing o integration testing.

### Pruebas de caja de cristal

* Estas pruebas se basan en el flujo del programa. Aquí parten de que tu conoces el funcionamiento internos, la implementación de la función.
* Prueban todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursiones, etc
* Son muy buenas para hacer *Regression testing* o *mocks*. Es decir, cuando descubrimos un bug una vez el programa ya salió a la luz.

### Debugging

> El origen de la palabra 'bug'  fue un caso real de un bicho que se metió en la computadora que utilizaba Grace Hooper causando errores

**Reglas Generales**

* No te molestes con el debugger. Aprende a utilizar el print statement, ya que nos da una mirada a lo que está sucediendo dentro del programa. 
* Estudia los datos disponibles (obtenidos por medio del print)
* Utiliza los datos para crear hipótesis y experimentos. *Método científico*
* Ten una mente abierta. No te preguntes porqué un programa está fallando, más bien pregúntate porque la computadora está computando de esa manera. **Si entendiera el programa, probablemente no habría bugs**
* Lleva un registro de lo que has tratado, preferentemente en forma de test, para que nunca vuelva a surgir.

## Unidad 7. Excepciones y Afirmaciones

### Excepciones

Una excepción es cuando sucede un error en el código

* Son muy comunes en programación. No tienen nada de excepcional :)
* Las excepciones de Python normalmente se relacionan con errores de semántica. Excepciones de tipo, de división, operaciones no compatibles, etc. 
* Se pueden crear excepciones propias
* Cuando una excepción no se maneja (unhandled exception). El programa termina en errores 

Un concepto muy atado a la excepciones es el *Defensive Programming* 

* Las excepciones se manejan con los keywords: **try**, **except** y **finally**. 

###  Afirmaciones

Las afirmaciones es un mecanismo para determinar si una condición se cumple o no, lo que nos permite decidir si continuar adelante con nuestro programa

* Es un método de programación defensiva (*Defensive Programming*). Nos estamos asegurando que los usuarios no vayan a cometer un error que puede ser fatal para la ejecución de nuestro programa.
* Puede utilizarse para verificar que los tipos de una función sean correctos. Ej. Que pasa si tienes un programa para sumar enteros y le pasas un float
* Son un gran método de debuggear. Hay veces que solamente quiere aventar resultados y dejarlo así, o dentro de loop