#!/usr/bin/env python3
# TP4 - Estructuras repetitivas
# Menú con 10 ejercicios, cada uno implementado como función.

import random


# ---------------------------------------------------------------------
# 1) Imprimir todos los números del 0 al 100 en orden creciente
def ej1_imprimir_0_a_100():
    print("\nEjercicio 1: Números del 0 al 100 (creciente)")
    for i in range(101):
        print(i)
    print("—— fin ——\n")


# ---------------------------------------------------------------------
# 2) Pedir entero y decir cuántos dígitos tiene
def ej2_cantidad_digitos():
    print("\nEjercicio 2: Cantidad de dígitos")
    while True:
        try:
            n = int(input("Ingresá un número entero (puede ser negativo): "))
            break
        except ValueError:
            print("→ Debe ser un entero. Probá de nuevo.")
    # Contar dígitos ignorando el signo
    n_abs = abs(n)
    # Caso especial 0
    cantidad = 1 if n_abs == 0 else 0
    while n_abs > 0:
        n_abs //= 10
        cantidad += 1
    print(f"El número tiene {cantidad} dígito(s).\n")


# ---------------------------------------------------------------------
# 3) Sumar todos los enteros entre dos valores (excluyendo los extremos)
def ej3_suma_entre_exclusiva():
    print("\nEjercicio 3: Suma de enteros entre A y B (excluye extremos)")
    while True:
        try:
            a = int(input("Ingresá A (entero): "))
            b = int(input("Ingresá B (entero): "))
            break
        except ValueError:
            print("→ Deben ser enteros. Probá de nuevo.")

    if a > b:
        a, b = b, a  
    total = 0
    for x in range(a + 1, b):
        total += x
    print(f"Suma de los enteros entre {a} y {b} (excl.): {total}\n")


# ---------------------------------------------------------------------
# 4) Leer enteros y sumarlos; terminar cuando se ingresa 0
def ej4_sumatoria_hasta_cero():
    print("\nEjercicio 4: Sumatoria hasta ingresar 0")
    total = 0
    while True:
        try:
            n = int(input("Ingresá un entero (0 para terminar): "))
        except ValueError:
            print("→ Debe ser un entero. Probá de nuevo.")
            continue
        if n == 0:
            break
        total += n
    print(f"La suma acumulada es: {total}\n")


# ---------------------------------------------------------------------
# 5) Juego: adivinar un número aleatorio entre 0 y 9
def ej5_adivina_0_a_9():
    print("\nEjercicio 5: ¡Adiviná el número (0 a 9)!")
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        try:
            guess = int(input("Tu intento: "))
        except ValueError:
            print("→ Debe ser un entero entre 0 y 9.")
            continue
        if guess < 0 or guess > 9:
            print("→ Debe estar entre 0 y 9.")
            continue
        intentos += 1
        if guess == secreto:
            print(f"¡Correcto! El número era {secreto}. Intentos: {intentos}\n")
            break
        # (Opcional) feedback
        if guess < secreto:
            print("Muy bajo…")
        else:
            print("Muy alto…")


# ---------------------------------------------------------------------
# 6) Imprimir los números pares del 0 al 100 en orden decreciente
def ej6_pares_decreciente():
    print("\nEjercicio 6: Pares de 100 a 0 (decreciente)")
    for x in range(100, -1, -2):
        print(x)
    print("—— fin ——\n")


# ---------------------------------------------------------------------
# 7) Suma de 0 hasta N (N entero no negativo)
def ej7_suma_0_hasta_n():
    print("\nEjercicio 7: Suma de 0 hasta N")
    while True:
        try:
            n = int(input("Ingresá N (entero ≥ 0): "))
            if n < 0:
                print("→ N debe ser ≥ 0.")
                continue
            break
        except ValueError:
            print("→ Debe ser un entero.")
    # Podríamos usar la fórmula n*(n+1)//2, pero lo hacemos con bucle:
    total = 0
    for i in range(n + 1):
        total += i
    print(f"La suma de 0 hasta {n} es: {total}\n")


# ---------------------------------------------------------------------
# 8) Leer 100 enteros; contar pares, impares, negativos y positivos
def ej8_contadores_100():
    print("\nEjercicio 8: 100 números → pares, impares, negativos, positivos")
    pares = impares = positivos = negativos = 0
    for i in range(1, 101):
        while True:
            try:
                n = int(input(f"[{i}/100] Ingresá un entero: "))
                break
            except ValueError:
                print("→ Debe ser un entero. Probá de nuevo.")
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        # (Si n == 0: cuenta como par y ni positivo ni negativo)
    print(f"Pares: {pares} | Impares: {impares} | Positivos: {positivos} | Negativos: {negativos}\n")


# ---------------------------------------------------------------------
# 9) Leer 100 enteros; calcular la media
def ej9_media_de_100():
    print("\nEjercicio 9: Media de 100 números")
    total = 0
    for i in range(1, 101):
        while True:
            try:
                n = int(input(f"[{i}/100] Ingresá un entero: "))
                break
            except ValueError:
                print("→ Debe ser un entero. Probá de nuevo.")
        total += n
    media = total / 100
    print(f"La media de los 100 valores es: {media}\n")


# ---------------------------------------------------------------------
# 10) Invertir los dígitos de un número (conservando el signo)
def ej10_invertir_digitos():
    print("\nEjercicio 10: Invertir dígitos de un número")
    while True:
        try:
            n = int(input("Ingresá un número entero (puede ser negativo): "))
            break
        except ValueError:
            print("→ Debe ser un entero. Probá de nuevo.")
    signo = -1 if n < 0 else 1
    n_abs = abs(n)
    if n_abs == 0:
        invertido = 0
    else:
        invertido = 0
        while n_abs > 0:
            invertido = invertido * 10 + (n_abs % 10)
            n_abs //= 10
    invertido *= signo
    print(f"Número invertido: {invertido}\n")


# ========================== MENÚ PRINCIPAL ============================

def mostrar_menu():
    print("====== TP 4 - Estructuras Repetitivas ======")
    print("1) Imprimir del 0 al 100 (creciente)")
    print("2) Cantidad de dígitos de un entero")
    print("3) Suma de enteros entre A y B (excluye extremos)")
    print("4) Sumatoria hasta ingresar 0")
    print("5) Juego: adivinar número (0–9)")
    print("6) Pares de 100 a 0 (decreciente)")
    print("7) Suma de 0 a N")
    print("8) 100 números: pares/impares/negativos/positivos")
    print("9) 100 números: media")
    print("10) Invertir dígitos de un número")
    print("0) Salir")
    print("===========================================\n")


def main():
    acciones = {
        1: ej1_imprimir_0_a_100,
        2: ej2_cantidad_digitos,
        3: ej3_suma_entre_exclusiva,
        4: ej4_sumatoria_hasta_cero,
        5: ej5_adivina_0_a_9,
        6: ej6_pares_decreciente,
        7: ej7_suma_0_hasta_n,
        8: ej8_contadores_100,
        9: ej9_media_de_100,
        10: ej10_invertir_digitos,
    }

    while True:
        mostrar_menu()
        try:
            op = int(input("Elegí una opción: "))
        except ValueError:
            print("→ Opción inválida (ingresá un número).")
            continue

        if op == 0:
            print("¡Hasta la próxima!")
            break

        funcion = acciones.get(op)
        if funcion is None:
            print("→ Opción inexistente.")
        else:
            funcion()


if __name__ == "__main__":
    main()
