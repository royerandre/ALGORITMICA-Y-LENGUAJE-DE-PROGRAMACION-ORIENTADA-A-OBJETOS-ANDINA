"""Un grupo de números quiere llegar ordenado a la meta. Crea una función
burbuja_numeros(lista) que ordene la siguiente lista usando el método de burbuja.
Lista: [5, 3, 8, 4, 2]
Resultado esperado: [2, 3, 4, 5, 8]
Muestra paso a paso cómo los números “intercambian posiciones”."""

def burbuja_numeros(lista):
    n = len (lista)
    print ("lista inicial:",lista)
    for i in range(n-1):
        for j in range (n-i-1):
            if lista[j]>lista[j-1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                print(f"intercambio{lista}")
    return lista
numeros = [5, 3, 8, 4, 2]
resultado = burbuja_numeros(numeros)
print("resultado final: ",resultado) 