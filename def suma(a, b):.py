def suma(a, b):
    """Función para sumar dos números."""
    return a + b

def resta(a, b):
    """Función para restar dos números."""
    return a - b

# Ejemplos de uso
if __name__ == "__main__":
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    
    resultado_suma = suma(num1, num2)
    resultado_resta = resta(num1, num2)
    
    print(f"La suma es: {resultado_suma}")
    print(f"La resta es: {resultado_resta}")
