import csv

RUTA_CSV = "paises.csv"

# ============================
# CARGA DE CSV
# ============================
def cargar_csv(ruta):
    paises = []
    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    if not nombre or not continente:
                        print("⚠ Fila con campos vacíos, se omite:", fila)
                        continue

                    pais = {
                        "nombre": nombre,
                        "poblacion": poblacion,
                        "superficie": superficie,
                        "continente": continente
                    }
                    paises.append(pais)
                except (KeyError, ValueError):
                    print("⚠ Error de formato en fila CSV, se omite:", fila)
        return paises
    except FileNotFoundError:
        print("⚠ No existe el archivo CSV. Se iniciará lista vacía.")
        return []

# ============================
# GUARDAR CSV
# ============================
def guardar_csv(ruta, paises):
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(paises)
    print("✔ Archivo guardado correctamente en", ruta)

# ============================
# ENTRADAS VALIDADAS
# ============================
def input_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("⚠ Este campo no puede estar vacío.")

def input_entero_positivo(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            valor = int(dato)
            if valor > 0:
                return valor
            else:
                print("⚠ Debe ser un número entero positivo.")
        except ValueError:
            print("⚠ Debe ingresar un número entero.")

# ============================
# AGREGAR PAÍS
# ============================
def agregar_pais(paises):
    print("\n--- Agregar país ---")
    nombre = input_no_vacio("Nombre del país: ")
    poblacion = input_entero_positivo("Población: ")
    superficie = input_entero_positivo("Superficie: ")
    continente = input_no_vacio("Continente: ")

    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo)
    print("✔ País agregado correctamente.")

# ============================
# ACTUALIZAR
# ============================
def actualizar_pais(paises):
    print("\n--- Actualizar país ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    nombre = input_no_vacio("Ingrese nombre (o parte del nombre) del país a actualizar: ").lower()
    candidatos = [p for p in paises if nombre in p["nombre"].lower()]

    if not candidatos:
        print("⚠ No se encontró ningún país que coincida.")
        return

    # Si hay más de uno, los muestro
    if len(candidatos) > 1:
        print("Se encontraron varios países:")
        for i, p in enumerate(candidatos, start=1):
            print(f"{i}. {p['nombre']} (Población {p['poblacion']}, Sup {p['superficie']})")
        idx = input_entero_positivo("Seleccione número de país a actualizar: ") - 1
        if not (0 <= idx < len(candidatos)):
            print("⚠ Opción inválida.")
            return
        pais = candidatos[idx]
    else:
        pais = candidatos[0]

    print("Actualizando:", pais["nombre"])
    pais["poblacion"] = input_entero_positivo("Nueva población: ")
    pais["superficie"] = input_entero_positivo("Nueva superficie: ")
    print("✔ Datos actualizados.")

# ============================
# BUSCAR
# ============================
def buscar_pais(paises):
    print("\n--- Buscar país ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    texto = input_no_vacio("Buscar por nombre: ").lower()
    resultados = [p for p in paises if texto in p["nombre"].lower()]

    if resultados:
        print(f"✔ Se encontraron {len(resultados)} resultado(s):")
        for p in resultados:
            print(p)
    else:
        print("⚠ Búsqueda sin resultados.")

# ============================
# FILTROS
# ============================
def filtrar_por_continente(paises):
    print("\n--- Filtrar por continente ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    cont = input_no_vacio("Continente: ").lower()
    filtrado = [p for p in paises if p["continente"].lower() == cont]
    if filtrado:
        for p in filtrado:
            print(p)
    else:
        print("⚠ No se encontraron países para ese continente.")

def filtrar_rango_poblacion(paises):
    print("\n--- Filtrar por rango de población ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    minimo = input_entero_positivo("Población mínima: ")
    maximo = input_entero_positivo("Población máxima: ")
    if minimo > maximo:
        minimo, maximo = maximo, minimo  # los intercambio

    filtrado = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    if filtrado:
        for p in filtrado:
            print(p)
    else:
        print("⚠ No se encontraron países en ese rango de población.")

def filtrar_rango_superficie(paises):
    print("\n--- Filtrar por rango de superficie ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    minimo = input_entero_positivo("Superficie mínima: ")
    maximo = input_entero_positivo("Superficie máxima: ")
    if minimo > maximo:
        minimo, maximo = maximo, minimo

    filtrado = [p for p in paises if minimo <= p["superficie"] <= maximo]
    if filtrado:
        for p in filtrado:
            print(p)
    else:
        print("⚠ No se encontraron países en ese rango de superficie.")

# ============================
# ORDENAR
# ============================
def ordenar_paises(paises, clave, descendente=False):
    print(f"\n--- Ordenar por {clave} ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return
    ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)
    for p in ordenados:
        print(p)

# ============================
# ESTADÍSTICAS
# ============================
def estadisticas(paises):
    print("\n--- Estadísticas ---")
    if not paises:
        print("⚠ No hay países cargados.")
        return

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    prom_pobl = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("País con mayor población:", mayor)
    print("País con menor población:", menor)
    print("Promedio de población:", prom_pobl)
    print("Promedio de superficie:", prom_sup)

    continentes = {}
    for p in paises:
        c = p["continente"]
        continentes[c] = continentes.get(c, 0) + 1

    print("Cantidad de países por continente:")
    for cont, cant in continentes.items():
        print(f"  {cont}: {cant}")

# ============================
# MENÚ PRINCIPAL
# ============================
def menu():
    paises = cargar_csv(RUTA_CSV)

    while True:
        print("""
========= MENÚ =========
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Estadísticas
7. Guardar CSV
0. Salir
""")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            print("a) Continente\nb) Rango de población\nc) Rango de superficie")
            f = input("Elegir filtro: ").lower().strip()
            if f == "a":
                filtrar_por_continente(paises)
            elif f == "b":
                filtrar_rango_poblacion(paises)
            elif f == "c":
                filtrar_rango_superficie(paises)
            else:
                print("⚠ Opción de filtro inválida.")
        elif opcion == "5":
            print("a) Nombre\nb) Población\nc) Superficie")
            o = input("Ordenar por: ").lower().strip()
            if o == "a":
                ordenar_paises(paises, "nombre")
            elif o == "b":
                ordenar_paises(paises, "poblacion")
            elif o == "c":
                d = input("Descendente? (s/n): ").lower().strip() == "s"
                ordenar_paises(paises, "superficie", d)
            else:
                print("⚠ Opción de orden inválida.")
        elif opcion == "6":
            estadisticas(paises)
        elif opcion == "7":
            guardar_csv(RUTA_CSV, paises)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("⚠ Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()
