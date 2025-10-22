#Crear una función recursiva que muestre los N-ésimos términos de la Serie de Fibonacci 

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nro =int(input("Ingrese el numero de terminos de la serie :  "))
print(fibonacci(nro))