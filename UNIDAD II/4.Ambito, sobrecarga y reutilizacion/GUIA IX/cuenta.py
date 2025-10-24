class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad

    def get_titular(self):
        return self._titular

    def get_cantidad(self):
        return self._cantidad

    def set_titular(self, titular):
        self._titular = titular

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def mostrar(self):
        print(f"\n--- Datos de la Cuenta ---")
        print(f"El titular de la cuenta es: {self._titular}")
        print(f"Saldo actual: S/ {self._cantidad}")
        print("--------------------------")

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print(" No se puede ingresar una cantidad negativa o cero.")
        elif cantidad > 1000:
            print("No se puede ingresar más de S/ 1000 por depósito.")
        else:
            self._cantidad += cantidad
            print(f" Se ha ingresado S/ {cantidad}. Nuevo saldo: S/ {self._cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print(" No se puede retirar una cantidad negativa o cero.")
        elif cantidad > 1000:
            print(" No se puede retirar más de S/ 1000 por transacción.")
        elif cantidad > self._cantidad:
            print(" No tienes saldo suficiente para este retiro.")
        else:
            self._cantidad -= cantidad
            print(f" Se ha retirado S/ {cantidad}. Nuevo saldo: S/ {self._cantidad}")

def programa_principal():
    print("🏦 ¡Bienvenido al Sistema Bancario!")
    nombre_titular = input("Para comenzar, ingrese el nombre del titular de la cuenta: ")
    mi_cuenta = Cuenta(nombre_titular) 

    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Mostrar datos de la cuenta")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mi_cuenta.mostrar()

        elif opcion == '2':
            monto_ingresar = float(input("¿Cuánto dinero quieres meter?: S/ "))
            mi_cuenta.ingresar(monto_ingresar)

        elif opcion == '3':
            monto_retirar = float(input("¿Cuánto dinero quieres sacar?: S/ "))
            mi_cuenta.retirar(monto_retirar)

        elif opcion == '4':
            print("\n¡Gracias por usar el banco! ¡Adiós! ")
            break

        else:
            print(" ¡Opción no válida! Por favor, escribe solo un número del 1 al 4.")
            
if __name__ == "__main__":
    programa_principal()
