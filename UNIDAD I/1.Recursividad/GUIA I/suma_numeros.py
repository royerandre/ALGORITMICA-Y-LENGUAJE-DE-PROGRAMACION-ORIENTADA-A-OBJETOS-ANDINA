"""Crear una función recursiva que permita sumar los números naturales hasta N.
Nro = {0,1,2,3,4…..N}"""

def sumnatural(n):
    if n==0:
        return 0
    else:
        return n + sumnatural(n-1)
nro = int(input("ingrese su numero: "))
print(f"La suma de numeros naturales hasta {nro} es:{sumnatural(nro)}")
