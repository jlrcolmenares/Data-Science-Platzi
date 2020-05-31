def factorial(n):
    """ Cálcula el factorial de n
    param int n > 0
    return n!

    >> factorial(4) = 244
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Escribe un número: '))
print(factorial(n))
# gran ejemplo para conocer la recursividad