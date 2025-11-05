PRECIO_GASOLINA = 5.50
PRECIO_DIESEL = 4.80
PRECIO_ELECTRICIDAD = 0.80

class Vehiculo:
    def __init__(self, marca, modelo, consumo, nro_placa, color, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo
        self.nro_placa = nro_placa
        self.color = color
        self.tipo_combustible = tipo_combustible
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.nro_placa}")
        print(f"Color: {self.color}")
        print(f"Combustible: {self.tipo_combustible}")
    def costo_por_km(self):
        pass

class Coche(Vehiculo):

    def costo_por_km(self):
        return self.consumo * PRECIO_GASOLINA
    
class Camion(Vehiculo):

    def __init__(self, marca, modelo, consumo, nro_placa, color, tipo_combustible, capacidad_carga):
        super().__init__(marca, modelo, consumo, nro_placa, color, tipo_combustible)
        self.capacidad_carga = capacidad_carga

    def costo_por_km(self):
        """Usa el precio del diésel."""
        return self.consumo * PRECIO_DIESEL
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de Carga: {self.capacidad_carga}")

class CocheElectrico(Coche):
    def costo_por_km(self):
        return self.consumo * PRECIO_ELECTRICIDAD
    
def calcular_costes(vehiculos, kms):
    costes_finales = []
    for vehiculo in vehiculos:
        costo_total_viaje = vehiculo.costo_por_km() * kms
        costes_finales.append(costo_total_viaje)
    return costes_finales

coche1 = Coche("Toyota", "Yaris", 0.07, "ABC-123", "Rojo", "Gasolina")
camion1 = Camion("Volvo", "FH", 0.3, "DEF-456", "Blanco", "Diésel", "20 toneladas")
electrico1 = CocheElectrico("Tesla", "Model 3", 0.15, "GHI-789", "Negro", "Electricidad")

lista = [coche1, camion1, electrico1]


distancia_viaje = 200 


lista_de_costos = calcular_costes(lista, distancia_viaje)


print(f" Resultados para un viaje de {distancia_viaje} km\n")
print("---------------------------")

for i in range(len(lista)):
    vehiculo_actual = lista[i]
    costo_actual = lista_de_costos[i]
    vehiculo_actual.mostrar_informacion()
    print(f"Costo Total del Viaje: S/ {costo_actual:.2f}")
    print("---------------------------")



