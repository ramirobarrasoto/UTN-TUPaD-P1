"""
TP 8 - Manejo de Archivos
Versión interactiva con inputs
Autor: Ramiro barra soto
"""

import os

ARCHIVO = 'productos.txt'

# ------------------ Utilitarios ------------------

def _to_float(val: str) -> float:
    return float(val.replace(',', '.').strip())

def _to_int(val: str) -> int:
    return int(val.strip())

def _input_no_vacio(msg: str) -> str:
    while True:
        s = input(msg).strip()
        if s:
            return s
        print("El valor no puede estar vacío.")

def _confirmar(msg: str) -> bool:
    return input(f"{msg} (s/n): ").strip().lower() == 's'

def _normalizar_nombre(nombre: str) -> str:
    return nombre.strip()

# ------------------ Persistencia ------------------

def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO):
        productos_iniciales = [
            "Lapicera,120.5,30",
            "Cuaderno,250.0,15",
            "Regla,75.0,50"
        ]
        with open(ARCHIVO, 'w', encoding='utf-8', newline='') as f:
            for producto in productos_iniciales:
                f.write(producto + '\n')

def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            for nlinea, linea in enumerate(f, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(',')
                if len(partes) != 3:
                    print(f"[Aviso] Línea {nlinea} inválida: {linea}")
                    continue
                nombre, precio, cantidad = partes
                try:
                    productos.append({
                        'nombre': _normalizar_nombre(nombre),
                        'precio': float(precio),
                        'cantidad': int(cantidad)
                    })
                except ValueError:
                    print(f"[Aviso] Tipos inválidos en línea {nlinea}: {linea}")
    return productos

def guardar_productos(productos):
    with open(ARCHIVO, 'w', encoding='utf-8', newline='') as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

# ------------------ Operaciones ------------------

def mostrar_productos(productos):
    if not productos:
        print("\nNo hay productos.\n")
        return
    print("\n=== LISTA DE PRODUCTOS ===")
    for i, p in enumerate(productos, start=1):
        print(f"{i:02d}. {p['nombre']} | ${p['precio']:.2f} | stock: {p['cantidad']}")
    print()

def buscar_indice_por_nombre(productos, nombre_buscar):
    nb = nombre_buscar.lower().strip()
    for i, p in enumerate(productos):
        if p['nombre'].lower() == nb:
            return i
    return -1

def agregar_producto(productos):
    nombre = _normalizar_nombre(_input_no_vacio("Nombre: "))
    # Manejo de duplicados
    idx = buscar_indice_por_nombre(productos, nombre)
    if idx != -1:
        print(f"Ya existe '{nombre}': ${productos[idx]['precio']:.2f} | stock {productos[idx]['cantidad']}")
        print("Opciones: [1] Sumar stock  [2] Reemplazar precio/stock  [3] Cancelar")
        opcion = input("Elija 1/2/3: ").strip()
        if opcion == '1':
            while True:
                try:
                    cant_sumar = _to_int(_input_no_vacio("Cantidad a sumar: "))
                    if cant_sumar < 0: 
                        print("La cantidad no puede ser negativa.")
                        continue
                    productos[idx]['cantidad'] += cant_sumar
                    print(f"✔ Stock actualizado. Nuevo stock: {productos[idx]['cantidad']}")
                    return
                except ValueError:
                    print("Cantidad inválida.")
        elif opcion == '2':
            # Reemplazar totalmente
            while True:
                try:
                    precio = _to_float(_input_no_vacio("Nuevo precio: "))
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Precio inválido (ej: 120.5 o 120,5).")
            while True:
                try:
                    cantidad = _to_int(_input_no_vacio("Nueva cantidad: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Cantidad inválida (entero).")
            productos[idx]['precio'] = precio
            productos[idx]['cantidad'] = cantidad
            print("✔ Producto actualizado.")
            return
        else:
            print("Acción cancelada.")
            return
    else:
        # Nuevo producto
        while True:
            try:
                precio = _to_float(_input_no_vacio("Precio: "))
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Precio inválido (ej: 120.5 o 120,5).")
        while True:
            try:
                cantidad = _to_int(_input_no_vacio("Cantidad: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Cantidad inválida (entero).")
        productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print(f"✔ Producto '{nombre}' agregado.")

def buscar_producto(productos):
    nombre = _input_no_vacio("Nombre a buscar: ")
    idx = buscar_indice_por_nombre(productos, nombre)
    if idx == -1:
        print("Producto no encontrado.")
    else:
        p = productos[idx]
        print(f"Encontrado: {p['nombre']} | ${p['precio']:.2f} | stock: {p['cantidad']}")

def editar_producto(productos):
    nombre = _input_no_vacio("Nombre del producto a editar: ")
    idx = buscar_indice_por_nombre(productos, nombre)
    if idx == -1:
        print("Producto no encontrado.")
        return
    p = productos[idx]
    print(f"Editando '{p['nombre']}' (Precio actual: ${p['precio']:.2f}, Stock actual: {p['cantidad']})")
    print("Deje vacío para mantener el valor.")

    nuevo_nombre = input("Nuevo nombre: ").strip()
    if nuevo_nombre:
        p['nombre'] = _normalizar_nombre(nuevo_nombre)

    precio_txt = input("Nuevo precio: ").strip()
    if precio_txt:
        try:
            precio = _to_float(precio_txt)
            if precio < 0:
                print("Precio no actualizado (valor negativo).")
            else:
                p['precio'] = precio
        except ValueError:
            print("Precio no actualizado (valor inválido).")

    cant_txt = input("Nuevo stock: ").strip()
    if cant_txt:
        try:
            cantidad = _to_int(cant_txt)
            if cantidad < 0:
                print("Stock no actualizado (valor negativo).")
            else:
                p['cantidad'] = cantidad
        except ValueError:
            print("Stock no actualizado (valor inválido).")
    print("✔ Cambios aplicados.")

def eliminar_producto(productos):
    nombre = _input_no_vacio("Nombre del producto a eliminar: ")
    idx = buscar_indice_por_nombre(productos, nombre)
    if idx == -1:
        print("Producto no encontrado.")
        return
    p = productos[idx]
    if _confirmar(f"¿Eliminar '{p['nombre']}'?"):
        productos.pop(idx)
        print("✔ Producto eliminado.")
    else:
        print("Acción cancelada.")

def ordenar_productos(productos):
    if not productos:
        print("No hay productos para ordenar.")
        return
    print("Ordenar por: [1] Nombre  [2] Precio  [3] Cantidad")
    op = input("Elija 1/2/3: ").strip()
    if op == '1':
        productos.sort(key=lambda x: x['nombre'].lower())
    elif op == '2':
        productos.sort(key=lambda x: x['precio'])
    elif op == '3':
        productos.sort(key=lambda x: x['cantidad'])
    else:
        print("Opción inválida.")
        return
    print("✔ Productos ordenados.")

# ------------------ Menú ------------------

def menu():
    crear_archivo_inicial()
    productos = leer_productos()

    opciones = {
        '1': ("Listar productos", lambda: mostrar_productos(productos)),
        '2': ("Agregar producto", lambda: agregar_producto(productos)),
        '3': ("Buscar producto", lambda: buscar_producto(productos)),
        '4': ("Editar producto", lambda: editar_producto(productos)),
        '5': ("Eliminar producto", lambda: eliminar_producto(productos)),
        '6': ("Ordenar productos", lambda: ordenar_productos(productos)),
        '7': ("Guardar cambios", lambda: guardar_productos(productos)),
        '8': ("Salir", None),
    }

    while True:
        print("\n=== MENÚ ===")
        for k, (txt, _) in opciones.items():
            print(f"{k}. {txt}")
        elec = input("Seleccione una opción: ").strip()

        if elec == '8':
            if _confirmar("¿Desea guardar antes de salir?"):
                guardar_productos(productos)
                print("✔ Cambios guardados.")
            print("Saliendo...")
            break

        accion = opciones.get(elec)
        if accion:
            accion[1]()  # ejecutar handler
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
