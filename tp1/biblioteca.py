# Parcial Programación 1 - Biblioteca (con match/case)
# Autor: Ramiro Barra Soto

PRESTAMO = "p"
DEVOLUCION = "d"
SI = "s"

opciones_menu = [
    "1. Ingresar títulos (sin ejemplares)",
    "2. Ingresar ejemplares disponibles (sin título)",
    "3. Mostrar catálogo",          
    "4. Consultar disponibilidad de un título específico",
    "5. Listar agotados",
    "6. Agregar título (con cantidad de ejemplares)",
    "7. Actualizar ejemplares (préstamo/devolución)",
    "8. Salir"
]

titulos = []
ejemplares = []

opcion = ""
while True:
    print("\n=== Menú Biblioteca ===")
    for item in opciones_menu:
        print(item)
    opcion = input("Elegí una opción: ")

    print()  # línea en blanco para mejor lectura

    match opcion:
        # 1) Ingresar títulos
        case "1":
            cantidad = input("¿Cuántos títulos desea ingresar?: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                for i in range(cantidad):
                    titulo = input(f"Ingrese título {i+1}: ").strip().lower()
                    while titulo == "" or titulo.lower() in [t.lower() for t in titulos]:
                        titulo = input("Título inválido o repetido, ingrese nuevamente: ").strip()
                    titulos.append(titulo)
                    ejemplares.append(0)  # se inicializan en 0
                    print(f"Título '{titulo}' agregado correctamente con 0 ejemplares.")
            else:
                print("Debe ingresar un número válido.")

        # 2) Ingresar ejemplares
        case "2":
            if not titulos:
                print("No hay títulos ingresados. Primero deben existir títulos para poder ingresar cantidad de ejemplares.")
                continue

            for i, titulo in enumerate(titulos):
                print(f"{i + 1}. {titulo}")

            posicion = int(input("Seleccione el número de título para ingresar ejemplares: ")) - 1

            while posicion < 0 or posicion >= len(titulos):
                print("Posición inválida, intente nuevamente")
                posicion = int(input("Seleccione el número de título para ingresar ejemplares: ")) - 1

            cantidad = int(input("Ingrese cantidad de ejemplares: "))

            while cantidad < 0:
                print("Cantidad inválida, debe ser un número no negativo.")
                cantidad = int(input("Ingrese cantidad de ejemplares: "))
            ejemplares[posicion] += cantidad
            print(f"Se han agregado {cantidad} ejemplares a '{titulos[posicion]}'. Total ahora: {ejemplares[posicion]} ejemplares.")
            

        # 3) Mostrar catálogo
        case "3":
            if not titulos:
                print("Catálogo vacío.")
            else:
                for i in range(len(titulos)):
                    print(f"{titulos[i]} → {ejemplares[i]} ejemplares")

        # 4) Consultar disponibilidad
        case "4":
            if not titulos:
                print("No hay libros para consulta en el catálogo.")
                continue

            while True:
                consulta = input("Ingrese el título a buscar: ").strip()
                if consulta.lower() in [t.lower() for t in titulos]:
                    i = [t.lower() for t in titulos].index(consulta.lower())
                    print(f"{titulos[i]} → {ejemplares[i]} ejemplares")
                    break
                else:
                    print(f"El título '{consulta}' no existe en el catálogo.")
                    reconsulta = input("Deseas volver a intentar? (s/n): ").strip().lower()
                    if reconsulta != SI:
                        break


        # 5) Listar agotados
        case "5":
            agotados = False
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"AGOTADO: {titulos[i]}")
                    agotados = True
            if not agotados:
                print("No hay libros agotados.")

        # 6) Agregar título
        case "6":
            nuevo = input("Ingrese el nuevo título: ").strip().lower()
            if nuevo != "" and nuevo.lower() not in [t.lower() for t in titulos]:
                cantidad = input("Ingrese ejemplares disponibles: ")
                if cantidad.isdigit() and int(cantidad) >= 0:
                    titulos.append(nuevo)
                    posicion = titulos.index(nuevo)
                    ejemplares.insert(posicion, int(cantidad))
                    print(f"Título '{nuevo}' agregado con éxito con '{cantidad}' ejemplares.")
                else:
                    print("Cantidad inválida.")
            else:
                print("Título vacío o ya existente.")

        # 7) Actualizar ejemplares (préstamo / devolución)
        case "7":
            buscar = input("Ingrese el título: ").strip()
            if buscar.lower() in [t.lower() for t in titulos]:
                i = [t.lower() for t in titulos].index(buscar.lower())
                accion = input("Ingrese 'p' para préstamo o 'd' para devolución: ").lower()
                if accion == PRESTAMO:
                    if ejemplares[i] > 0:
                        ejemplares[i] -= 1
                        print("Préstamo registrado.")
                    else:
                        print("No hay ejemplares disponibles.")
                elif accion == DEVOLUCION:
                    ejemplares[i] += 1
                    print("Devolución registrada.")
                else:
                    print("Opción inválida.")
            else:
                print("El título no existe.")

        # 8) salir
        case "8":
            confirmar = input("¿Seguro que deseas salir del sistema? (s/n): ").strip().lower()
            if confirmar == SI:
                print("Saliendo del sistema... Gracias vuelva pronto. 👋")
                break
            else:
                print("Operación cancelada. Volviendo al menú principal...")   

        # Default
        case _:
            print("Opción inválida. Intente nuevamente.")
