class Fecha:
    def __init__(self,dia="01",mes="01",ano="2000"):
        self.dia=dia
        self.mes=mes
        self.ano = ano
    def mostrar(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
    def incrementar(self,numeroDias):
        for _ in range(numeroDias):
            













fecha1 = Fecha("15","09","2002")
fecha1.mostrar()
