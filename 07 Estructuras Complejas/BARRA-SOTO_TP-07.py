"""
TP 7 - Estructuras de datos complejas (SIN OBJETOS)
Versión interactiva con inputs
Autor: Ramiro barra soto
"""

# -------------------------------------------------------------------
# EJERCICIO 1: Crear diccionario con frutas y precios
# -------------------------------------------------------------------
def ejercicio_1():
    precios_frutas = {}
    while True:
        fruta = input("Ingrese el nombre de una fruta (o 'fin' para terminar): ").capitalize()
        if fruta.lower() == "fin":
            break
        try:
            precio = float(input(f"Ingrese el precio de {fruta}: "))
            precios_frutas[fruta] = precio
        except ValueError:
            print("⚠️ Precio inválido, intente de nuevo.")
    print("\nDiccionario de frutas cargado:")
    print(precios_frutas)
    return precios_frutas


# -------------------------------------------------------------------
# EJERCICIO 2: Actualizar precios de frutas
# -------------------------------------------------------------------
def ejercicio_2(precios_frutas):
    print("\nActualización de precios:")
    while True:
        fruta = input("Ingrese el nombre de la fruta a actualizar (o 'fin' para terminar): ").capitalize()
        if fruta.lower() == "fin":
            break
        if fruta in precios_frutas:
            try:
                nuevo_precio = float(input(f"Ingrese el nuevo precio para {fruta}: "))
                precios_frutas[fruta] = nuevo_precio
            except ValueError:
                print("⚠️ Precio inválido.")
        else:
            print(f"⚠️ La fruta '{fruta}' no está en la lista.")
    print("\nPrecios actualizados:")
    print(precios_frutas)
    return precios_frutas


# -------------------------------------------------------------------
# EJERCICIO 3: Listar las frutas
# -------------------------------------------------------------------
def ejercicio_3(precios_frutas):
    frutas = list(precios_frutas.keys())
    print("\nLista de frutas cargadas:")
    print(frutas)
    return frutas


# -------------------------------------------------------------------
# EJERCICIO 4: Agenda telefónica
# -------------------------------------------------------------------
def ejercicio_4():
    agenda = {}
    print("\nCarga de agenda telefónica (5 contactos)")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ").capitalize()
        telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
        agenda[nombre] = telefono

    consulta = input("\nIngrese el nombre del contacto a consultar: ").capitalize()
    if consulta in agenda:
        print(f"{consulta} → {agenda[consulta]}")
    else:
        print(f"No existe el contacto '{consulta}'.")


# -------------------------------------------------------------------
# EJERCICIO 5: Contar palabras únicas y frecuencia
# -------------------------------------------------------------------
def ejercicio_5():
    frase = input("\nIngrese una frase: ")
    palabras = [p.strip(".,;:¡!¿?()\"'").lower() for p in frase.split() if p.strip()]
    unicas = set(palabras)
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    print("\nPalabras únicas:", unicas)
    print("Frecuencia por palabra:", conteo)


# -------------------------------------------------------------------
# EJERCICIO 6: Promedio de notas por alumno
# -------------------------------------------------------------------
def ejercicio_6():
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ").capitalize()
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("⚠️ Ingrese un número válido.")
        alumnos[nombre] = tuple(notas)

    print("\nPromedios:")
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / 3
        print(f"{alumno}: {promedio:.2f}")


# -------------------------------------------------------------------
# EJERCICIO 7: Aprobados Parcial 1 y Parcial 2
# -------------------------------------------------------------------
def ejercicio_7():
    parcial1 = set(input("Ingrese nombres de aprobados del Parcial 1 separados por coma: ").split(","))
    parcial2 = set(input("Ingrese nombres de aprobados del Parcial 2 separados por coma: ").split(","))

    parcial1 = {p.strip().capitalize() for p in parcial1}
    parcial2 = {p.strip().capitalize() for p in parcial2}

    print("\nAprobaron ambos:", parcial1 & parcial2)
    print("Aprobaron solo uno:", parcial1 ^ parcial2)
    print("Aprobaron al menos uno:", parcial1 | parcial2)


# -------------------------------------------------------------------
# EJERCICIO 8: Gestión de stock
# -------------------------------------------------------------------
def ejercicio_8():
    stock = {"yerba": 10, "azucar": 5}
    print("\nStock inicial:", stock)
    while True:
        producto = input("\nIngrese producto (o 'fin' para salir): ").lower()
        if producto == "fin":
            break
        try:
            cantidad = int(input(f"Ingrese cantidad a agregar para {producto}: "))
        except ValueError:
            print("⚠️ Ingrese un número válido.")
            continue

        if producto in stock:
            stock[producto] += cantidad
        else:
            stock[producto] = cantidad

        print("Stock actualizado:", stock)


# -------------------------------------------------------------------
# EJERCICIO 9: Agenda de eventos (día, hora)
# -------------------------------------------------------------------
def ejercicio_9():
    agenda = {}
    print("\nCarga de eventos (día, hora, descripción)")
    while True:
        dia = input("Día (o 'fin' para salir): ").capitalize()
        if dia.lower() == "fin":
            break
        hora = input("Hora (formato HH:MM): ")
        evento = input("Descripción del evento: ")
        agenda[(dia, hora)] = evento

    consulta_dia = input("\nConsultar día: ").capitalize()
    consulta_hora = input("Consultar hora: ")
    print(agenda.get((consulta_dia, consulta_hora), "No hay evento en ese día y hora."))


# -------------------------------------------------------------------
# EJERCICIO 10: Invertir diccionario de países y capitales
# -------------------------------------------------------------------
def ejercicio_10():
    paises = {}
    while True:
        pais = input("Ingrese país (o 'fin' para terminar): ").capitalize()
        if pais.lower() == "fin":
            break
        capital = input(f"Ingrese la capital de {pais}: ").capitalize()
        paises[pais] = capital

    invertido = {v: k for k, v in paises.items()}
    print("\nDiccionario invertido (capital → país):")
    print(invertido)


# -------------------------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------------------------
def menu():
    while True:
        print("\n=== TP6: Estructuras de datos complejas ===")
        print("1. Frutas y precios")
        print("2. Actualizar precios")
        print("3. Listar frutas")
        print("4. Agenda telefónica")
        print("5. Análisis de frase")
        print("6. Promedios de alumnos")
        print("7. Aprobados parciales")
        print("8. Gestión de stock")
        print("9. Agenda de eventos")
        print("10. Invertir países y capitales")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "0":
            print("👋 Saliendo del programa...")
            break
        elif opcion == "1":
            global frutas
            frutas = ejercicio_1()
        elif opcion == "2":
            if 'frutas' in globals():
                frutas = ejercicio_2(frutas)
            else:
                print("⚠️ Primero debe ejecutar el ejercicio 1.")
        elif opcion == "3":
            if 'frutas' in globals():
                ejercicio_3(frutas)
            else:
                print("⚠️ Primero debe ejecutar el ejercicio 1.")
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


# -------------------------------------------------------------------
# EJECUCIÓN PRINCIPAL
# -------------------------------------------------------------------
if __name__ == "__main__":
    menu()
