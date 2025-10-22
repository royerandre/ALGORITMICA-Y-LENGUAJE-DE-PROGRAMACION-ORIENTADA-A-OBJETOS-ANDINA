""" El Desafío del Botín (Insertion Sort)
Un aventurero encontró una bolsa con monedas de oro de diferentes tamaños y necesita
ordenarlas de menor a mayor para que entren en un compartimento secreto.
Crea una función ordenar_monedas(monedas) que implemente el método de inserción
para ordenar la lista.
Lista: [10, 5, 25, 1, 8]
"""

# EJERCICIO 4.1: El Desafío del Botín (Insertion Sort)

def ordenar_monedas(monedas):
    n = len(monedas)
    for i in range(1, n):
        j = i
        while j > 0 and monedas[j] < monedas[j-1]:
            monedas[j], monedas[j-1] = monedas[j-1], monedas[j]
            j = j - 1
            
    return monedas


lista_monedas = [10, 5, 25, 1, 8]

monedas_ordenadas = ordenar_monedas(lista_monedas)

print("--- Resultado ---")
print("Lista de monedas original:", [10, 5, 25, 1, 8])
print("Lista de monedas ordenada:", monedas_ordenadas)