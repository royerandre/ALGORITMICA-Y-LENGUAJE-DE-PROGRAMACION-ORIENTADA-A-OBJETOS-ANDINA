from clase1 import Persona

class Docente(Persona):
    def __init__(self, _Dni, _Nombre,_especialidad):
        super().__init__(_Dni, _Nombre)
        self.especialidad=_especialidad
    def mostrarDocente(self):
        print(f"EL ni del doncente es :{self.Dni} y el nombre {self.nombre} y la especialidad {self.especialidad}")

docente1=Docente("24941234","Redy Delgado","IS")
docente1.mostrarDocente()
