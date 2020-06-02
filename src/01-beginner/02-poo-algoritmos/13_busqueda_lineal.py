import random

def busqueda_lineal(lista, objetivo):
    match = False
    
    for elemento in lista: # complejidad O(n)
        
        if elemento == objetivo:
            print('match! match! match!')
            match == True
            break     # si pensamos en el peor caso este break no sirve de nada

    return match

if __name__ == "__main__":
    tamaño_lista = int(input('Indica tamaño de lista: '))
    objetivo = int(input('Qué número quieres encontrar? '))
    
    #librería random nos permite hallar valores aleatorios
    lista = [random.randint(0,100) for item in range(tamaño_lista)] #list comprohension

    encontrado = busqueda_lineal(lista,objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
    # ^ operador ternario python dentro de las llaves