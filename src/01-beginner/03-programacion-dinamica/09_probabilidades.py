import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        # tenemos un dado que tiene 6 caras. Elegimos un numero aleatorio entre 1 y 6
        tiro = random.choice([1, 2, 3, 4, 5, 6]) # randInt(1,7) es otra opción par implementaro        secuencia_de_tiros.append(tiro)
        # una vez tenemos un tiro se lo añadimos a la secuencia
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        # generamos un loop que corra la simulación la cantidad de veces que nosotros definamos
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        # si tiramos el dado 1 vez tendremos un valor, si lo tiramos 10 veces tendrá 10 valores
        tiros.append(secuencia_de_tiros)

    # en este caso vamos a calcular la probabilidad de que un tiro del dado NO SEA 1
    tiros_con_1 = 0
    for tiro in tiros:
        # Aquí está la condición para probar los tiros de los dados. 
        if 1 not in tiro:  # la condicion de obtener un 1 sería 'if 1 in tiro'
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    # numero de caso afirmativos / numero total de casos
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)