class Animal:
    def comer(self):
        return "El animal está comiendo."
class Mamifero(Animal):
    def amamantar(self):
        return "El mamífero está amamantando."
class Ave(Animal):
    def volar(self):
        return "El ave está volando."
class Murcielago(Mamifero, Ave):
    pass
    
murcielago1 = Murcielago()
print(murcielago1.comer())
print(murcielago1.amamantar())
print(murcielago1.volar())