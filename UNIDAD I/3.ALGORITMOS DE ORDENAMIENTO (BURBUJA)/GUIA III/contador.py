"""Modifica la función anterior para contar:
4.2.a. Cuántas comparaciones se realizan,
4.2.b. Cuántos intercambios hubo.
4.2.c. Al final, muestra ambos conteos e imprime la lista ordenada.
"""
def burbuja_numeros(lista):
    n= len (lista)
    comparaciones=0
    intercambios=0
    print("lista inicial:",lista)
    for i in range(n-1):
        for j in range (n-i-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                intercambios += 1
    print(f"Lista ordenada ",lista)
    print("numero de comparaciones:",comparaciones)
    print("numero de intercambios: ",intercambios)
    return lista

numeros = [5, 3, 8, 4, 2]
resultado = burbuja_numeros(numeros)