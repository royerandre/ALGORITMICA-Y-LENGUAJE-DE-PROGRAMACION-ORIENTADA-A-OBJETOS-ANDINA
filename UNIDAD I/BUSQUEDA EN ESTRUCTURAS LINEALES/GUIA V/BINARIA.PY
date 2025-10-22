import random

def ordenar_lista_insercion(lista_original):

    lista_a_ordenar = []
    for numero in lista_original:
        lista_a_ordenar.append(numero)

    for i in range(1, len(lista_a_ordenar)):
        j = i
        while j > 0 and lista_a_ordenar[j] < lista_a_ordenar[j-1]:
            lista_a_ordenar[j], lista_a_ordenar[j-1] = lista_a_ordenar[j-1], lista_a_ordenar[j]
            j = j - 1
            
    return lista_a_ordenar


def la_lista_esta_ordenada(lista):

    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False    
    return True

def busqueda_binaria(lista, numero_a_buscar):

    posicion_izquierda = 0
    posicion_derecha = len(lista) - 1
    iteraciones = 0 


    while posicion_izquierda <= posicion_derecha:
        iteraciones = iteraciones + 1
        

        posicion_del_medio = (posicion_izquierda + posicion_derecha) // 2
        

        if lista[posicion_del_medio] == numero_a_buscar:
            return posicion_del_medio, iteraciones 
        
        elif numero_a_buscar > lista[posicion_del_medio]:

            posicion_izquierda = posicion_del_medio + 1
        else:

            posicion_derecha = posicion_del_medio - 1
            

    return -1, iteraciones


print("--- Resultado---")
numeros_aleatorios = []
for i in range(100):
    numero = random.randint(1, 1000)
    numeros_aleatorios.append(numero)
print(" Se ha generado una lista de 100 números.")


if la_lista_esta_ordenada(numeros_aleatorios) == False:
    print("-> La lista estaba desordenada. Se ordenará ahora.")
    lista_final = ordenar_lista_insercion(numeros_aleatorios)
else:
    print("-> La lista ya estaba ordenada.")
    lista_final = numeros_aleatorios

print("\n--- 🚀 Realizando Búsquedas de Prueba una por una ---")




numero_buscado = lista_final[10] 
posicion, iteraciones = busqueda_binaria(lista_final, numero_buscado)
print(f"\nBuscando el número: {numero_buscado}")
print(f"  -> Resultado: Encontrado en la posición {posicion}.")
print(f"  -> Iteraciones con Búsqueda Binaria: {iteraciones}")
print(f"  -> Comparaciones con Búsqueda Secuencial (estimado): {posicion + 1}")


numero_buscado = lista_final[50] 
posicion, iteraciones = busqueda_binaria(lista_final, numero_buscado)
print(f"\nBuscando el número: {numero_buscado}")
print(f"  -> Resultado: Encontrado en la posición {posicion}.")
print(f"  -> Iteraciones con Búsqueda Binaria: {iteraciones}")
print(f"  -> Comparaciones con Búsqueda Secuencial (estimado): {posicion + 1}")

numero_buscado = lista_final[99] 
posicion, iteraciones = busqueda_binaria(lista_final, numero_buscado)
print(f"\nBuscando el número: {numero_buscado}")
print(f"  -> Resultado: Encontrado en la posición {posicion}.")
print(f"  -> Iteraciones con Búsqueda Binaria: {iteraciones}")
print(f"  -> Comparaciones con Búsqueda Secuencial (estimado): {posicion + 1}")


numero_buscado = 2000 
posicion, iteraciones = busqueda_binaria(lista_final, numero_buscado)
print(f"\nBuscando el número: {numero_buscado}")
print(f"  -> Resultado: No se encontró el elemento ({posicion}).")
print(f"  -> Iteraciones con Búsqueda Binaria: {iteraciones}")
print(f"  -> Comparaciones con Búsqueda Secuencial (estimado): {len(lista_final)}")
