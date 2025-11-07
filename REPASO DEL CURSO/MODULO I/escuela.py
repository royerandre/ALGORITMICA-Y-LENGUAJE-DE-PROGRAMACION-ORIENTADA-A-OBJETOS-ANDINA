class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def grado_actual(self):
        return f"{self.nombre} está en el grado {self.grado}."

estudiante1 = Estudiante("Ana", 20, "Segundo") 
print(estudiante1.saludar())  