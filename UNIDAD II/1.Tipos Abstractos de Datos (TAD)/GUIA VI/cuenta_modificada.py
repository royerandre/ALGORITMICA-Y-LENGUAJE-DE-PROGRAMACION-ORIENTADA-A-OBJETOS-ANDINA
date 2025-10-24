class CuentaMejorada:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar debe ser positivo.")
        elif monto > 10000:
            print("No se puede depositar más de S/ 10,000 a la vez.")
        else:
            self.cantidad += monto
            print(f"Depósito exitoso. Saldo actual: S/ {self.cantidad:.2f}")

    def retirar(self, monto):

        if monto <= 0:
            print(" El monto a retirar debe ser positivo.")
        elif monto > self.cantidad:
            print(f" Saldo insuficiente. No puede retirar S/ {monto:.2f}.")
        else:
            self.cantidad -= monto
            print(f" Retiro exitoso. Saldo actual: S/ {self.cantidad:.2f}")

    def mostrar(self):

        print(f"Titular: {self.titular}, Saldo: S/ {self.cantidad:.2f}")


print("\n--- Probando  ---")
cuenta_pro = CuentaMejorada("Ana", 500)
cuenta_pro.mostrar()


cuenta_pro.depositar(15000) 
cuenta_pro.depositar(-100)  
cuenta_pro.depositar(200)   

cuenta_pro.retirar(800)     
cuenta_pro.retirar(-50)     
cuenta_pro.retirar(150)     


cuenta_pro.mostrar()