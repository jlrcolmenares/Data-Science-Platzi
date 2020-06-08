import sys

def fibonacci_recursivo(n):
    # definición clásica
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n] # si tenemos el key en el diccionario lo regresamos
    except KeyError: #si el key no existe lo generamos en el diccionario memo. 
        # hacemos el resultado de la recursividad. 
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        print(memo)
        return resultado

if __name__ == '__main__':
    
    #fibonacci_recursivo(50) tarda más de 10 minutos en implementarse y regresar un valor
    
    sys.setrecursionlimit(10002) #extendemos el límite de recursividad, en principo es 1000
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)