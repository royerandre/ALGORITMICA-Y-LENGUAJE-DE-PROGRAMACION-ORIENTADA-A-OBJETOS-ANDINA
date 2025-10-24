class Persona:

    institucion ="UAC"
    
    def __init__(self,_Dni,_Nombre):
        self.__Dni=_Dni
        self.nombre=_Nombre
    
    def mostrar(self):
        print(f"la institucion es : {self.institucion} el dni es: {self.__Dni} y el nombre {self.nombre}")
    
    @property
    def Dni(self):
        return self.__Dni
    
    @Dni.setter
    def Dni(self,_updateDni):
        if len(_updateDni)==8:
            self.__Dni=_updateDni
        else:
            print("error de longitud")
            
if __name__=="__main__":
    personal=Persona("1111111111","JUAN Gabriel")
    personal.mostrar()