class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")


estudiante = str(input("Ingrese el nombre del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
grado = str(input("Ingrese el grado del estudiante: "))
estudiante1 = Estudiante(estudiante, edad, grado)
estudiante1.estudiar()



