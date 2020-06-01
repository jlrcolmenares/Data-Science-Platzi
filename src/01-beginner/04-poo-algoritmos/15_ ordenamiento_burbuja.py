import random 

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):   # vas a iterar por sobre todo la lista
        for j in range(0, n - 1 - i):  # la recorres n veces, luego n-1, luego n-2, y así
            #print(i,j)
            if lista[j] > lista[j+1]:
                # print(lista[j],lista[j+1])
                lista[j],lista[j+1]= lista[j+1] , lista[j]
                # notacion swaping. Se intercambian valores

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)