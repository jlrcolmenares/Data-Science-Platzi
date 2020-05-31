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