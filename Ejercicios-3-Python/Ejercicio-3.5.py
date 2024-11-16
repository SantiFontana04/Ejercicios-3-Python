
numero = int(input("Ingrese un número entero positivo: "))

def calcularFactorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

print(f"El factorial de {numero} es {calcularFactorial(numero)}")
