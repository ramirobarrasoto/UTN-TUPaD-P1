# Parcial 2 - Programación 1
# Gestión de Biblioteca con CSV, listas y diccionarios (sin excepciones, sin clases, sin lambdas, sin globales)
# Requiere Python 3.10+ (por match/case)

import os
import csv

CSV_PATH = "catalogo.csv"
ENCABEZADO = ["TITULO", "CANTIDAD"]

# ----------------- Utilidades -----------------

def normalizar_titulo(t):
    # elimina espacios extra y compara sin mayúsculas
    t = t.strip()
    t = " ".join(t.split())
    return t

def titulo_igual(a, b):
    return normalizar_titulo(a).lower() == normalizar_titulo(b).lower()

def pedir_entero_no_negativo(mensaje):
    valor = input(mensaje).strip()
    while not valor.isdigit():
        print("Error: debe ingresar un número entero no negativo.")
        valor = input(mensaje).strip()
    return int(valor)

def existe_titulo(catalogo, titulo):
    i = 0
    while i < len(catalogo):
        if titulo_igual(catalogo[i]["TITULO"], titulo):
            return True
        i += 1
    return False

def buscar_indice(catalogo, titulo):
    i = 0
    while i < len(catalogo):
        if titulo_igual(catalogo[i]["TITULO"], titulo):
            return i
        i += 1
    return -1

def cargar_csv(ruta):
    catalogo = []
    if os.path.exists(ruta):
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            filas = list(lector)
            # Validar encabezado básico
            if len(filas) > 0:
                # si hay encabezado, empezar en 1; si no, desde 0
                inicio = 1 if filas[0] == ENCABEZADO else 0
                i = inicio
                while i < len(filas):
                    fila = filas[i]
                    if len(fila) == 2:
                        t = normalizar_titulo(fila[0])
                        c = fila[1].strip()
                        if t != "" and c.isdigit():
                            # Si repite título, no lo duplica; conserva primer aparición
                            if not existe_titulo(catalogo, t):
                                catalogo.append({"TITULO": t, "CANTIDAD": int(c)})
                    i += 1
    return catalogo

def guardar_csv(ruta, catalogo):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(ENCABEZADO)
        i = 0
        while i < len(catalogo):
            escritor.writerow([catalogo[i]["TITULO"], catalogo[i]["CANTIDAD"]])
            i += 1

def confirmar_guardado(catalogo):
    guardar_csv(CSV_PATH, catalogo)
    print("✅ Cambios guardados en", CSV_PATH)

# ----------------- Funcionalidades -----------------

def op1_ingresar_titulos_multiples(catalogo):
    cantidad = pedir_entero_no_negativo("¿Cuántos libros desea cargar?: ")
    if cantidad == 0:
        print("No se cargaron títulos.")
        return catalogo

    cargados = 0
    i = 0
    while i < cantidad:
        titulo = normalizar_titulo(input(f"Ingrese TITULO #{i+1}: "))
        while titulo == "" or existe_titulo(catalogo, titulo):
            if titulo == "":
                print("Error: el título no puede ser vacío.")
            else:
                print("Error: el título ya existe en el catálogo.")
            titulo = normalizar_titulo(input(f"Ingrese TITULO #{i+1}: "))

        cant = pedir_entero_no_negativo("Ingrese CANTIDAD (>= 0): ")
        # Alta
        catalogo.append({"TITULO": titulo, "CANTIDAD": cant})
        cargados += 1
        i += 1

    confirmar_guardado(catalogo)
    print(f"✅ Se cargaron {cargados} libro(s).")
    return catalogo

def op2_ingresar_ejemplares(catalogo):
    if len(catalogo) == 0:
        print("No hay títulos cargados. Primero debe cargar libros.")
        return catalogo

    print("\nCatálogo:")
    i = 0
    while i < len(catalogo):
        print(f"{i+1}. {catalogo[i]['TITULO']} → {catalogo[i]['CANTIDAD']}")
        i += 1

    pos = pedir_entero_no_negativo("Seleccione el número de título: ")
    # convertir a índice
    if pos == 0 or pos > len(catalogo):
        print("Posición inválida.")
        return catalogo
    idx = pos - 1

    accion = input("¿Desea sumar (s) o restar (r) ejemplares?: ").strip().lower()
    while accion not in ["s", "r"]:
        print("Acción inválida. Use 's' para sumar o 'r' para restar.")
        accion = input("¿Desea sumar (s) o restar (r) ejemplares?: ").strip().lower()

    cant = pedir_entero_no_negativo("Ingrese cantidad: ")

    if accion == "s":
        catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] + cant
        confirmar_guardado(catalogo)
        print(f"✅ Stock actualizado: {catalogo[idx]['TITULO']} → {catalogo[idx]['CANTIDAD']}")
    else:
        # restar
        if cant <= catalogo[idx]["CANTIDAD"]:
            catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] - cant
            confirmar_guardado(catalogo)
            print(f"✅ Stock actualizado: {catalogo[idx]['TITULO']} → {catalogo[idx]['CANTIDAD']}")
        else:
            print("❌ No se puede restar más de lo disponible.")

    return catalogo

def op3_mostrar_catalogo(catalogo):
    if len(catalogo) == 0:
        print("Catálogo vacío.")
        return
    print("\n=== Catálogo ===")
    i = 0
    while i < len(catalogo):
        print(f"- {catalogo[i]['TITULO']} → {catalogo[i]['CANTIDAD']} ejemplares")
        i += 1

def op4_consultar_disponibilidad(catalogo):
    if len(catalogo) == 0:
        print("No hay libros para consulta en el catálogo.")
        return

    while True:
        consulta = normalizar_titulo(input("Ingrese el título a buscar: "))
        idx = buscar_indice(catalogo, consulta)
        if idx != -1:
            print(f"{catalogo[idx]['TITULO']} → {catalogo[idx]['CANTIDAD']} ejemplares")
            break
        else:
            print(f"El título '{consulta}' no existe en el catálogo.")
            otra = input("¿Desea volver a intentar? (s/n): ").strip().lower()
            if otra != "s":
                break

def op5_listar_agotados(catalogo):
    print("\n=== Agotados ===")
    hay = False
    i = 0
    while i < len(catalogo):
        if catalogo[i]["CANTIDAD"] == 0:
            print(f"- {catalogo[i]['TITULO']}")
            hay = True
        i += 1
    if not hay:
        print("No hay libros agotados.")

def op6_agregar_titulo(catalogo):
    titulo = normalizar_titulo(input("Ingrese TITULO: "))
    while titulo == "" or existe_titulo(catalogo, titulo):
        if titulo == "":
            print("Error: el título no puede ser vacío.")
        else:
            print("Error: el título ya existe en el catálogo.")
        titulo = normalizar_titulo(input("Ingrese TITULO: "))

    cant = pedir_entero_no_negativo("Ingrese CANTIDAD inicial (>= 0): ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": cant})
    confirmar_guardado(catalogo)
    print("✅ Título agregado correctamente.")
    return catalogo

def op7_actualizar_prestamo_devolucion(catalogo):
    if len(catalogo) == 0:
        print("No hay libros cargados.")
        return catalogo

    titulo = normalizar_titulo(input("Ingrese el título: "))
    idx = buscar_indice(catalogo, titulo)
    if idx == -1:
        print("El título no existe en el catálogo.")
        return catalogo

    print("Ingrese 'p' para préstamo o 'd' para devolución.")
    acc = input("Acción: ").strip().lower()
    while acc not in ["p", "d"]:
        print("Acción inválida. Use 'p' (préstamo) o 'd' (devolución).")
        acc = input("Acción: ").strip().lower()

    if acc == "p":
        if catalogo[idx]["CANTIDAD"] > 0:
            catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] - 1
            confirmar_guardado(catalogo)
            print("✅ Préstamo registrado.")
        else:
            print("❌ No hay ejemplares disponibles para préstamo.")
    else:
        catalogo[idx]["CANTIDAD"] = catalogo[idx]["CANTIDAD"] + 1
        confirmar_guardado(catalogo)
        print("✅ Devolución registrada.")

    print(f"Estado: {catalogo[idx]['TITULO']} → {catalogo[idx]['CANTIDAD']}")
    return catalogo

# ----------------- Programa principal -----------------

def main():
    catalogo = cargar_csv(CSV_PATH)

    opcion = ""
    while True:
        print("\n=== Biblioteca Escolar (CSV) ===")
        print("1. Ingresar títulos (múltiples)")
        print("2. Ingresar ejemplares (sumar/restar)")
        print("3. Mostrar catálogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar título")
        print("7. Actualizar ejemplares (préstamo/devolución)")
        print("8. Salir")

        opcion = input("Elegí una opción: ").strip()
        print()

        match opcion:
            case "1":
                catalogo = op1_ingresar_titulos_multiples(catalogo)
            case "2":
                catalogo = op2_ingresar_ejemplares(catalogo)
            case "3":
                op3_mostrar_catalogo(catalogo)
            case "4":
                op4_consultar_disponibilidad(catalogo)
            case "5":
                op5_listar_agotados(catalogo)
            case "6":
                catalogo = op6_agregar_titulo(catalogo)
            case "7":
                catalogo = op7_actualizar_prestamo_devolucion(catalogo)
            case "8":
                confirmar = input("¿Seguro que deseas salir del sistema? (s/n): ").strip().lower()
                if confirmar == "s":
                    print("Saliendo del sistema... 👋")
                    break
                else:
                    print("Operación cancelada. Volviendo al menú principal...")
            case _:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
