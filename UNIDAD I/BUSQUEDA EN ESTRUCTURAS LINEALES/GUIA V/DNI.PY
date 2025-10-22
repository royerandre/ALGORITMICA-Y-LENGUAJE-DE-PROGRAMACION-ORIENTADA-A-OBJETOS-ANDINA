import random

def generar_dnis(cantidad):
    """
    Genera una lista de DNIs aleatorios usando un bucle básico.
    """
    lista_vacia = []
    
    for i in range(cantidad):
        dni_nuevo = random.randint(10000000, 99999999)
        lista_vacia.append(dni_nuevo)
        
    return lista_vacia

def busqueda_secuencial_simple(lista, objetivo):
    """
    Busca un elemento en una lista revisando uno por uno.
    
    Retorna solo la posición (índice) si lo encuentra.
    Si no encuentra el elemento, retorna -1.
    """
    # Se recorre la lista desde el índice 0 hasta el final.
    for i in range(len(lista)):
        if lista[i] == objetivo:
            # Si se encuentra, retorna la posición inmediatamente.
            return i
    
    # Si el bucle termina, el DNI no se encontró y retorna -1.
    return -1

# --- Ejecución del Ejercicio ---

# 1) Genera una lista de N=60 DNIs aleatorios.
N = 60
lista_de_dnis = generar_dnis(N)

dni_a_buscar = int(input("Por favor, ingresa el DNI de 8 dígitos que quieres encontrar: "))

print(f"\n Buscando el DNI {dni_a_buscar}...")
posicion_encontrada = busqueda_secuencial_simple(lista_de_dnis, dni_a_buscar)

if posicion_encontrada != -1:
    print(f"  -> ¡Éxito! El DNI fue encontrado en la posición: {posicion_encontrada}")
else:
    print(f"  -> Lo sentimos, el DNI {dni_a_buscar} no se encuentra en la lista  .")