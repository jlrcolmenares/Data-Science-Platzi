def morral(tamano_morral,pesos,valores,n):
    # en este caso se va a recorre la lista desde
    # el final, por eso n = len(valores)

    # caso 0:
    # si ya revisamos todo el morral (n ==0)
    # o si ya llenamos el morral con cosas
    if n == 0 or tamano_morral == 0:
        return 0
    # caso 1:
    # si el peso del elemento n supera el 
    # tamaño del morral, regresa el morral
    # con lo que ya tiene dentro
    # pero con n-1 para que revise el siguiente objeto
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral,pesos,valores, n-1) 
    # caso 2: puedo tomar un elemento o no tomarlo
    # si decido tomarlos, viene con un valor.
    # si lo tomara cual valor tendría.
    # y tomar el valor
    return max( valores[n - 1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1), morral(tamano_morral,pesos,valores, n-1) )

if __name__ == "__main__":
    
    valores = [60,100,120]  # lista[0] = valor[0] 
    pesos = [10,20,30]      # lista con pesos de las cosas
    tamano = 5     #constraint: capacidad del morral del ladros
    n = len(valores)     # indice de las objetos que se lleva el ladrón

    resultado = morral(tamano,pesos,valores,n) # esto significa que estamos empezando al final
    print(resultado)
    # cambiando el tamaño puedes ver cuales objetos te puede llevar
