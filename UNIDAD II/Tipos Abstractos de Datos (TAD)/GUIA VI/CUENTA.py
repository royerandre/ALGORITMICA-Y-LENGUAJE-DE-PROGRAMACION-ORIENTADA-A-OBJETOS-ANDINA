
class Cuenta:

    def __init__(self, titular, cantidad=0.0):

        self.titular = titular
        self.cantidad = cantidad


    def depositar(self, monto):

        self.cantidad = self.cantidad + monto

    def retirar(self, monto):

        self.cantidad = self.cantidad - monto

    def mostrar(self):

        print(f"Titular: {self.titular}, Cantidad: S/ {self.cantidad:.2f}")



print("--- Probando Ejercicio 5.1 ---")

cuenta1 = Cuenta("Luis") 
cuenta2 = Cuenta("Carlos", 100) 

cuenta1.depositar(1000)
cuenta2.retirar(50)


cuenta1.mostrar()
cuenta2.mostrar()