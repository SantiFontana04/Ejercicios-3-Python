
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

def dibujar_rectangulo(filas, columnas):
    for _ in range(filas): 
        print("|" * columnas)

dibujar_rectangulo(filas, columnas)