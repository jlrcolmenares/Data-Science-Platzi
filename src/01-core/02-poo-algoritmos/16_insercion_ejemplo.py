import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]    # se guarda el valor en una variable que no se toca
        posicion_actual = indice        # se guarda la posición
        print("Valor actual {:3d} ***** Posicion actual {:3d}".format(valor_actual,posicion_actual))

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1] # se intercambian los valores dentro de la lista
            posicion_actual -= 1    # se compara con la siguiente posición
            print('Posicion actual-1 (while): ',posicion_actual)

        lista[posicion_actual] = valor_actual   # cuando la posición actual-1 es menor que el valor actual, se le asigna el valor apartado

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    #lista = [7,3,2,9,8]
    print(lista)

    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)