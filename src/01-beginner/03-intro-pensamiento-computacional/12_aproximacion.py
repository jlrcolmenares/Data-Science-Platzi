objetivo = int(input('Escoge un número: '))
epsilon = 0.01 #que tan cerca queremos llegar de la respuesta
paso = epsilon**2 #cada cuanto me quiero acercar
respuesta = 0.0
#nuestra respuesta comiensa
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')