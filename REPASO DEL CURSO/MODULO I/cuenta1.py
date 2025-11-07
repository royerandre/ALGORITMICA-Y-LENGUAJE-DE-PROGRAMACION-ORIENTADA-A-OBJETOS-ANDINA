class Cuenta:
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,anadido):
        if 0<anadido<=10000:
            self.saldo += anadido
        elif anadido + self.saldo > 10000:
                print("Depósito excede el límite permitido de 10,000.")
        else:
                print("El monto a depositar debe ser positivo.")
    def retirar(self,retirado):
        if 0<retirado<=self.saldo:
            self.saldo -= retirado
        elif retirado>self.saldo:
            print("Fondos insuficientes para retirar la cantidad solicitada.")
        else:
            print("El monto a retirar debe ser positivo.")
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")

cliente1 = Cuenta("Juan", 1000)
cliente1.retirar(-200)
cliente1.mostrar()


