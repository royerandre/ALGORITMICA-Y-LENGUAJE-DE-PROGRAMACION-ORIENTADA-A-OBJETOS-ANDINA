"""¿Qué pasaría si quisiéramos que nuestra función 
sumar solo sumara los números si ambos son positivos? Si uno de ellos es negativo, la función no debería hacer nada. 
¿Cómo le daríamos a la máquina una instrucción para que pueda tomar una decisión?
"""
def sumar(num1, num2):
    if num1 < 0 or num2 < 0:
        return "Error: ambos números deben ser positivos."
    else:
        return num1 + num2

print(sumar(5, 10))  # Salida: 15
print(sumar(-5, 10)) # Salida: Error: ambos números deben ser positivos.        
    
    