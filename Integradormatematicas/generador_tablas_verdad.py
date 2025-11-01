import itertools

def implica(p, q):
    return (not p) or q

def equivalencia(p, q):
    return p == q

# Menú de opciones
opciones_menu = [
    "1. AND (p ∧ q)",
    "2. OR (p ∨ q)",
    "3. NOT (¬p)",
    "4. IMPLICA (p ⇒ q)",
    "5. EQUIVALENCIA (p ⇔ q)",
    "6. TAUTOLOGÍA (p ∨ ¬p)",
    "7. CONTRADICCIÓN (p ∧ ¬p)",
    "8. Salir"
]

while True:
    print("\n=== Simulador de Proposiciones Lógicas ===")
    for item in opciones_menu:
        print(item)

    opcion = input("Elegí una opción: ")

    if opcion == "8":
        print("Saliendo del programa...")
        break

    tabla = []
    resultados = []

    # Caso especial: NOT (solo depende de p)
    if opcion == "3":
        expr = "NOT p"
        print(f"\nTabla de verdad para: {expr}")
        print(f"{'p':<5}{'Resultado':<10}")
        print("-" * 15)

        for p in [0, 1]:
            resultado = int(not bool(p))
            tabla.append((p, resultado))
            resultados.append(resultado)
            print(f"{p:<5}{resultado:<10}")

    # Tautología p ∨ ¬p
    elif opcion == "6":
        expr = "p ∨ ¬p"
        print(f"\nTabla de verdad para: {expr}")
        print(f"{'p':<5}{'Resultado':<10}")
        print("-" * 15)

        for p in [0, 1]:
            resultado = int(bool(p) or not bool(p))
            tabla.append(resultado)
            resultados.append(resultado)
            print(f"{p:<5}{resultado:<10}")

    # Contradicción p ∧ ¬p
    elif opcion == "7":
        expr = "p ∧ ¬p"
        print(f"\nTabla de verdad para: {expr}")
        print(f"{'p':<5}{'Resultado':<10}")
        print("-" * 15)

        for p in [0, 1]:
            resultado = int(bool(p) and not bool(p))
            tabla.append(resultado)
            resultados.append(resultado)
            print(f"{p:<5}{resultado:<10}")    

    else:
        # Para las demás opciones se usan p y q
        if opcion == "1":
            expr = "p AND q"
        elif opcion == "2":
            expr = "p OR q"
        elif opcion == "4":
            expr = "p ⇒ q"
        elif opcion == "5":
            expr = "p ⇔ q"
        else:
            print("Opción no válida.")
            continue

        print(f"\nTabla de verdad para: {expr}")
        print(f"{'p':<5}{'q':<5}{'Resultado':<10}")
        print("-" * 20)

        for p, q in itertools.product([0, 1], repeat=2):
            if opcion == "1":
                resultado = int(bool(p) and bool(q))
            elif opcion == "2":
                resultado = int(bool(p) or bool(q))
            elif opcion == "4":
                resultado = int(implica(bool(p), bool(q)))
            elif opcion == "5":
                resultado = int(equivalencia(bool(p), bool(q)))
            
            tabla.append((p, q, resultado))
            resultados.append(resultado)
            print(f"{p:<5}{q:<5}{resultado:<10}")

    # Clasificación de la proposición
    if all(r == 1 for r in resultados):
        print("Clasificación: Tautología")
    elif all(r == 0 for r in resultados):
        print("Clasificación: Contradicción")
    else:
        print("Clasificación: Contingencia")