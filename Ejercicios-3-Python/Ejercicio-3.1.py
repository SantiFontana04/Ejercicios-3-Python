
notas = [8, 3, 7, 9]

def calcularPromedio(notas):
    if len(notas) == 0:
        return "No se ingresaron notas"
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

print(calcularPromedio(notas))
