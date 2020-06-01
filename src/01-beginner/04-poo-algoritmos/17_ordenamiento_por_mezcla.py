import random

def ord_por_mezcla(lista):
    #caso base
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva
        derecha = ord_por_mezcla(derecha)
        print('length der: ',len(derecha))
        izquierda = ord_por_mezcla(izquierda)
        print('length izq: ',len(izquierda))

        #iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i< len(izquierda) and j < len(derecha): #mientras podamos seguir comparando
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k+= 1
        #copiar los pedazos de las listas que quedaron
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda  {izquierda}. derecha  {derecha}')
        print('lista:',lista,'[ k:',k,'j:',j,'i:',i,']')
        print('--' * 20)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ord_por_mezcla(lista)
    print(lista_ordenada)