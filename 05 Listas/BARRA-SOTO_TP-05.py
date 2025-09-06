# TP5 - Listas
# Autor: Ramiro Barra Soto

import random

# ----------------------------------------------------------------------
# 1) Notas de estudiantes
def ej1_notas_estudiantes():
    notas = [random.randint(1, 10) for _ in range(10)]
    print("Notas:", notas)
    print("Promedio:", sum(notas)/len(notas))
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))


# ----------------------------------------------------------------------
# 2) Lista de productos
def ej2_lista_productos():
    productos = []
    for i in range(5):
        productos.append(input(f"Ingrese producto {i+1}: "))
    print("Lista ordenada:", sorted(productos))
    eliminar = input("Ingrese producto a eliminar: ")
    if eliminar in productos:
        productos.remove(eliminar)
    print("Lista final:", productos)


# ----------------------------------------------------------------------
# 3) Números aleatorios: pares e impares
def ej3_pares_impares():
    lista = [random.randint(1, 100) for _ in range(15)]
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    print("Lista completa:", lista)
    print("Pares:", pares, "Cantidad:", len(pares))
    print("Impares:", impares, "Cantidad:", len(impares))


# ----------------------------------------------------------------------
# 4) Eliminar duplicados
def ej4_eliminar_duplicados():
    lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
    print("Lista original:", lista)
    lista_sin_repetidos = list(set(lista))
    print("Lista sin duplicados:", lista_sin_repetidos)


# ----------------------------------------------------------------------
# 5) Nombres de estudiantes
def ej5_nombres_estudiantes():
    estudiantes = ["Ana", "Luis", "Juan", "Pedro", "María", "Lucía", "Pablo", "Sofía"]
    print("Lista actual:", estudiantes)
    accion = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()
    if accion == "A":
        nuevo = input("Nombre del estudiante a agregar: ")
        estudiantes.append(nuevo)
    elif accion == "E":
        eliminar = input("Nombre del estudiante a eliminar: ")
        if eliminar in estudiantes:
            estudiantes.remove(eliminar)
    print("Lista final:", estudiantes)


# ----------------------------------------------------------------------
# 6) Rotar elementos
def ej6_rotar_elementos():
    lista = [1, 2, 3, 4, 5, 6, 7]
    print("Lista original:", lista)
    lista = [lista[-1]] + lista[:-1]
    print("Lista rotada:", lista)


# ----------------------------------------------------------------------
# 7) Matriz temperaturas (7x2)
def ej7_temperaturas():
    dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
    temps = [[random.randint(0, 15), random.randint(16, 35)] for _ in range(7)]
    print("Temperaturas mínimas y máximas (semana):")
    for d, t in zip(dias, temps):
        print(f"{d}: Min {t[0]}, Max {t[1]}")
    prom_min = round(sum(t[0] for t in temps)/7,2)
    prom_max = round(sum(t[1] for t in temps)/7,2)
    print("Promedio mínimas:", prom_min)
    print("Promedio máximas:", prom_max)
    amplitudes = [t[1] - t[0] for t in temps]
    dia_max = dias[amplitudes.index(max(amplitudes))]
    print("Mayor amplitud térmica:", dia_max)


# ----------------------------------------------------------------------
# 8) Matriz notas (5x3)
def ej8_matriz_notas():
    estudiantes = ["Estudiante.1", "Estudiante.2", "Estudiante.3", "Estudiante.4", "Estudiante.5"]
    materias = ["Matemática", "Lengua", "Historia"]
    notas = [[random.randint(1, 10) for _ in range(3)] for _ in range(5)]
    print("Notas:")
    for e, fila in zip(estudiantes, notas):
        print(e, fila, "Promedio:", round(sum(fila)/3,2))
    for j, m in enumerate(materias):
        prom_materia = sum(notas[i][j] for i in range(5))/5
        print("Promedio en", m, ":", prom_materia)


# ----------------------------------------------------------------------
# 9) Ta-Te-Ti
def ej9_tateti():
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    jugador = "X"
    for _ in range(9):
        for fila in tablero:
            print(" ".join(fila))
        f = int(input(f"Jugador {jugador}, fila (0-2): "))
        c = int(input(f"Jugador {jugador}, columna (0-2): "))
        if tablero[f][c] == "-":
            tablero[f][c] = jugador
            jugador = "O" if jugador == "X" else "X"
        else:
            print("Casilla ocupada, pierdes turno")
    for fila in tablero:
        print(" ".join(fila))


# ----------------------------------------------------------------------
# 10) Ventas (4x7)
def ej10_ventas():
    productos = ["Prod1", "Prod2", "Prod3", "Prod4"]
    dias = [f"Día{j+1}" for j in range(7)]

    # 4x7: 4 productos x 7 días
    ventas = [[random.randint(10, 100) for _ in range(7)] for _ in range(4)]

    # ------- Cabecera (días) -------
    ancho_prod = 8      # ancho de la columna de productos
    ancho_num = 5       # ancho para cada número
    cabecera = f"{'':<{ancho_prod}}" + "".join(f"{d:>{ancho_num}}" for d in dias) + f" | {'Total':>{ancho_num}}"
    print(cabecera)
    print("-" * len(cabecera))

    # ------- Filas (producto + ventas + total por producto) -------
    totales_prod = []
    for p, fila in zip(productos, ventas):
        total_fila = sum(fila)
        totales_prod.append(total_fila)
        fila_str = "".join(f"{n:>{ancho_num}}" for n in fila)
        print(f"{p:<{ancho_prod}}{fila_str} | {total_fila:>{ancho_num}}")

    # ------- Totales por día (columna) -------
    totales_dias = [sum(ventas[i][j] for i in range(len(productos))) for j in range(len(dias))]
    print("-" * len(cabecera))
    tot_dias_str = "".join(f"{t:>{ancho_num}}" for t in totales_dias)
    print(f"{'Tot/Día':<{ancho_prod}}{tot_dias_str} | {sum(totales_dias):>{ancho_num}}")

    # ------- Análisis: mejor día y producto más vendido -------
    dia_max = totales_dias.index(max(totales_dias)) + 1
    prod_max = productos[totales_prod.index(max(totales_prod))]

    print(f"\nDía con mayores ventas: {dia_max}")
    print(f"Producto más vendido: {prod_max}")


# ============================= MENÚ ==============================
def menu():
    opciones = {
        "1": ej1_notas_estudiantes,
        "2": ej2_lista_productos,
        "3": ej3_pares_impares,
        "4": ej4_eliminar_duplicados,
        "5": ej5_nombres_estudiantes,
        "6": ej6_rotar_elementos,
        "7": ej7_temperaturas,
        "8": ej8_matriz_notas,
        "9": ej9_tateti,
        "10": ej10_ventas,
    }
    while True:
        print("\n=== TP5 - Listas ===")
        for k in opciones:
            print(f"{k}) Ejercicio {k}")
        print("0) Salir")
        op = input("Elegí una opción: ")
        if op == "0":
            break
        if op in opciones:
            opciones[op]()
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
