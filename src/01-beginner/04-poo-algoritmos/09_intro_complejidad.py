import time
import sys 
sys.setrecursionlimit(10002)

# Factorial normal. Con operaciones algorítmica
def factorial(n):
    respuesta = 1
    
    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

# Factorial recursivo. 
def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)

if __name__ == "__main__":
    
    n = 10000
    
    print(sys.getrecursionlimit())

    comienzo = time.time() #mides el tiempo antes de ejecutar la función 
    factorial(n)
    final = time.time() #mides el tiempo después ejecutar
    print(final - comienzo) #restas y obtienes tiempo total

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
    