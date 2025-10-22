import random
import time


def insercion_con_metricas(lista_original):
    lista = []
    for elemento in lista_original:
        lista.append(elemento)
        
    comparaciones = 0
    tiempo_inicio = time.time()
    n = len(lista)

    for i in range(1, n):
        j = i
        while j > 0:
            comparaciones += 1
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                j -= 1
            else:
                break
    
    tiempo_total = time.time() - tiempo_inicio
    return comparaciones, tiempo_total

def seleccion_con_metricas(lista_original):
    lista = []
    for elemento in lista_original:
        lista.append(elemento)

    n = len(lista)
    comparaciones = 0
    tiempo_inicio = time.time()

    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            comparaciones += 1
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
            
    tiempo_total = time.time() - tiempo_inicio
    return comparaciones, tiempo_total


def menu_principal():
    lista_generada = []

    while True:
        print("\n--- MENÚ DE OPERACIÓN ---")
        print("1. Generar lista de 100 números aleatorios")
        print("2. Ordenar lista y analizar eficiencia")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            lista_generada = [random.randint(1, 1000) for _ in range(100)]
            print("\n ¡Lista de 100 números generada con éxito!")
            print("   Primeros 10 números:", lista_generada[:10])

        elif opcion == '2':
            # Verificamos si la lista está vacía. Si lo está, mostramos un error.
            if not lista_generada:
                print("\n Primero debes generar la lista con la opción 1.")
            else:
                print("\n Ordenando la lista con ambos métodos...")
                
                comps_ins, tiempo_ins = insercion_con_metricas(lista_generada)
                comps_sel, tiempo_sel = seleccion_con_metricas(lista_generada)
                
                print("\n--- Resultados del Análisis ---")
                
                print("\n>> Método de Inserción:")
                print(f"   - Comparaciones realizadas: {comps_ins}")
                print(f"   - Tiempo de ejecución: {tiempo_ins:.6f} segundos")

                print("\n>> Método de Selección:")
                print(f"   - Comparaciones realizadas: {comps_sel}")
                print(f"   - Tiempo de ejecución: {tiempo_sel:.6f} segundos")

        elif opcion == '3':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("\nOpción no válida. Por favor, elige 1, 2 o 3.")

menu_principal()

"""Aunque ambos comparten la misma complejidad teórica en el peor caso,
para una lista aleatoria como esta, Insertion Sort 
es más eficiente porque  le permite ahorrar una cantidad significativa de comparaciones."""