class movimientos:
    def __init__(self, nombre):
        self.saldo = 0
        self.propietario = nombre
        print(f'Tu saldo actual es {self.saldo}')

    def deposito(self, cantidad):
        self.saldo += cantidad
        print(f'Tu saldo actual es {self.saldo}')
        return self.saldo
        
    def retiro(self, cantidad):
        if cantidad > self.saldo:
            return ('fondos insuficiente')
        self.saldo -= cantidad
        return (self.saldo)


if __name__ == "__main__":
        
    cc = movimientos (str(input('Escribe tu nombre: ')))
    
    cc.deposito(int(input('Escribe el valor a depositar: ')))

    cc.retiro(int(input('Escribe el valor a retirar: ')))

    if cc.saldo <= 0:
        print ('Fondos insuficientes')
    else:
        print (f'{cc.propietario} Tu saldo actual disponible es: {cc.saldo}')
        
