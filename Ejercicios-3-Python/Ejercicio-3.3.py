
numeros = [101, 50, 32, 16]

def calcularMayor(numeros):
    if len(numeros) == 0:
        return "No se ingresaron numeros"
    mayor = max(numeros)
    return f"El número mayor es {mayor}"

print(calcularMayor(numeros))
