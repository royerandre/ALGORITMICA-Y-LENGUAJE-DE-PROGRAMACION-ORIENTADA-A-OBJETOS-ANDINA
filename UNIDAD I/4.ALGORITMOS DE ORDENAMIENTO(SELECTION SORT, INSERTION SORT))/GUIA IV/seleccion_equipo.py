"""El Desafío del Botín (Insertion Sort)
Un aventurero encontró una bolsa con monedas de oro de diferentes tamaños y necesita
ordenarlas de menor a mayor para que entren en un compartimento secreto.
Crea una función ordenar_monedas(monedas) que implemente el método de inserción
para ordenar la lista.
Lista: [10, 5, 25, 1, 8]
"""


def ordenar_equipo(fuerzas):

    n = len(fuerzas)

    for i in range(n - 1):
        
        indice_minimo = i
        
        for j in range(i + 1, n):
            if fuerzas[j] < fuerzas[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            fuerzas[i], fuerzas[indice_minimo] = fuerzas[indice_minimo], fuerzas[i]
            
    return fuerzas

lista_fuerzas = [40, 30, 90, 20, 10]


equipo_ordenado = ordenar_equipo(lista_fuerzas)


print("--- Resultado---")
print("Lista de fuerzas original:", [40, 30, 90, 20, 10])
print("Equipo ordenado por fuerza:", equipo_ordenado)