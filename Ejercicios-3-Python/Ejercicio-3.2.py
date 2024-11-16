
colores_primarios = ["Rojo", "Amarillo","Azul"]

def esPrimario(color):
    if color.capitalize() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

esPrimario("Verde")
