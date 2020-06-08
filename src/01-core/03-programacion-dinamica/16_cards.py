import random
import collections # una parte de la librería estándar

# Se declaran las contantes en mayúsculas,
# por convención las constantes se escriben en mayúsuculas

PALOS = ['Corazones', 'Picas', 'Treboles', 'Diamantes']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    # funcion para crear baraja con todas sus opciones disponibles
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    # funcion que toma un set de 52 cartes y extrae N cartas de forma aleatoria
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    # con esta función podemos generar varias manos    
    mazo = crear_baraja()
    #print(mazo)

    manos = []
    for _ in range(intentos):  # ejecutar esto N veces
        mano = obtener_mano(mazo, tamano_mano) # toma el mazo creado anteriormente
        manos.append(mano)

    # si tenemos 5 cartas cual es la probabilidad de que nos salda un par
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])  # tenemos tuplas (palo, valor), el valor es el indice 1
        
        # dentro de collection tenenmos un clase muy específica llamada counter
        counter = dict(collections.Counter(valores))
        # print(counter) #revisamos que funcione antes de continuar
        for val in counter.values():  # como ahora es un diccionario podemos acceder a los valores
            if val == 2:
                pares += 1
                break  # solo queremos calcular la probilidades de obtener 1 par
            
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de  {tamano_mano} cartas es {probabilidad_par}')
        

if __name__ == "__main__":
    tamano_mano = int(input('De cuantas cartas será la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))
    # ley de la multiplicacion de las probabilidades,
    # intentos independientes consecutivos hacen que la probabilidad sea cada vez más pequeña
    # mano = obtener_mano(mazo, 3) # funcion inicial
    main( tamano_mano, intentos)