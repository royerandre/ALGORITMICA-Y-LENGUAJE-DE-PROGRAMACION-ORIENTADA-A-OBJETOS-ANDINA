"""Los estudiantes se están formando para un desfile. Ordena sus nombres alfabéticamente
usando Bubble Sort.
Lista: ["Carlos", "Ana", "Pedro", "Lucía", "Diego"]
Resultado esperado: ["Ana", "Carlos", "Diego", "Lucía", "Pedro"]"""

def burbuja_nombres(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range (n-i-1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
nombres = ["Carlos", "Ana", "Pedro", "Lucía", "Diego"]
resultado = burbuja_nombres(nombres)
print("resultado final:",resultado)