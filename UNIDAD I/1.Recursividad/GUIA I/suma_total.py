"""Dada una lista de números, escribe una función recursiva que calcule la suma de todos los
elementos en la lista.
Lista = [10,9,8,7,6,5,4,3,2,1]
Lista = 55
"""

def sum_lista(lista):
    if len(lista) == 0 :
        return 0 
    else :
        return lista [0] + sum_lista(lista[1:0])

lista = [10,9,8,7,6,5,4,3,2,1]

print("La suma  de la lista es : ",sum_lista(lista))
