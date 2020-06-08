import random

# Calcular promedio
def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)
    sumatoria = 0
    for x in X:  # notacion matemática
        sumatoria += (x - mu)** 2
    
    return sumatoria / len(X)

def desviacion_estandar(X):
    return (varianza(X))**0.5 

if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print('Arreglo:', X)
    print('Media: ', mu)
    print('Varianza: ', Var)
    print('Desv Estandar: ', sigma)
