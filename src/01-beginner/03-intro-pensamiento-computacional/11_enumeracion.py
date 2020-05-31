objetivo = int(input('Escoge un entero: ')) #entrada
respuesta = 0 #valor inicial

while respuesta**2 < objetivo:
    print(respuesta)
    respuesta += 1 #

if respuesta**2 == objetivo:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'El objetivo no tiene raiz cuadrar exacta')    