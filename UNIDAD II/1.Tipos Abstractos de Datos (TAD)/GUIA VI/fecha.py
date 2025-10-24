
from datetime import date, timedelta

class Fecha:

    def __init__(self, dia=1, mes=1, anio=2000):

        try:
            self._fecha = date(anio, mes, dia)
        except ValueError:
            print(" La fecha ingresada no es válida. Se usará la fecha por defecto.")
            self._fecha = date(2000, 1, 1)

    def mostrar(self):
        """
        Muestra la fecha en formato DD/MM/AAAA.
        """
        print(f" Fecha: {self._fecha.strftime('%d/%m/%Y')}")

    def incrementar(self, numeroDias):
        """
        Incrementa la fecha actual por un número determinado de días.
        """
        if numeroDias >= 0:
            self._fecha += timedelta(days=numeroDias)
            print(f"{numeroDias} día(s) añadidos.")
        else:
            print(" Error: El número de días a incrementar debe ser positivo.")

    def distancia(self, dia, mes, anio):

        try:
            otra_fecha = date(anio, mes, dia)
            diferencia = self._fecha - otra_fecha
            
            print(f"  La distancia es de {abs(diferencia.days)} días.")
            return abs(diferencia.days)
        except ValueError:
            print(" La fecha para calcular la distancia no es válida.")
            return None


print("\n--- Probando  ---")


fecha_evento = Fecha(22, 10, 2025)
fecha_evento.mostrar()

fecha_evento.incrementar(10)
fecha_evento.mostrar()


fecha_evento.distancia(31, 12, 2025)


fecha_default = Fecha()
fecha_default.mostrar()