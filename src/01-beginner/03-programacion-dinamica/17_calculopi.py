import random
import math
from estadistica import media, varianza, desviacion_estandar
# es el archivo en el cual guardamos nuestro algoritmo de media, de varianza, etc

def lanzar_agujas(numero_de_agujas):
    dentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        # generamos las coordenadas entre 0 y 1
        x = random.random()  #esto nos regresa un valor entre 0 y 1 
        y = random.random()
        distancia_desde_centro = math.sqrt(x ** 2 + y ** 2)
        #print(x,y, distancia_desde_centro)
        if distancia_desde_centro <= 1:
            dentro_del_circulo += 1
    
    return (4 * dentro_del_circulo) / numero_de_agujas
    
def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = lanzar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
        # aqui lo que estamos calculando pi muchas veces para poder estimar la media

    media_estimados = media(estimados)
    sigma_estimados = desviacion_estandar(estimados)
    
    #print(media_estimados, varianza_estimados,sigma_estimados)

    print(f'Estimacion PI: {round(media_estimados, 5)}, sigma: { round(sigma_estimados, 5)}, agujas: {numero_de_agujas}')
    # en este punto vamos a usar la regla empirica para determinar ue tenemos un 95% por ciento de confianza
    # ese valor lo encontramos a 1.96 desviaciones estandar
    return (media_estimados,sigma_estimados)

def estimar_pi(precision, numero_de_agujas, numero_de_intentos):
    sigma = precision
    # condicion para cumplir el 95% de confiabilidad
    while sigma >= (precision / 1.96):
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        print(f'sigma: {sigma}. confiabilidad: {precision/1.96}')
        # con cada iteración vamos a multiplicar el número de agujas para ver si nos acercamos más
        numero_de_agujas *= 2

    return media

if __name__ == "__main__":
    print(estimar_pi(0.025, 3000, 1000))
    # impirme el promedio del cálculo