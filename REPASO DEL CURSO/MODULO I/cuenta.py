class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def mostrar(self):
        print(f"\n--- Datos de la Cuenta ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo: S/ {self.saldo}")   
        print("--------------------------")

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a ingresar debe ser mayor que cero.")
        else:
            self.saldo += cantidad
            print(f"Se han ingresado S/ {cantidad}. Nuevo saldo: S/ {self.saldo}")
