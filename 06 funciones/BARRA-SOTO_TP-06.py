# tp_funciones.py
# Práctico 2: Funciones en Python
# Programación I – Tecnicatura en Programación (UTN)
# Autor: Ramiro (alumno) — Estructurado y comentado

from __future__ import annotations
from typing import Optional, Tuple
import math


# 1) ---------------------------------------------------------------------------
def imprimir_hola_mundo() -> None:
    """Imprime 'Hola Mundo!'."""
    print("Hola Mundo!")


# 2) ---------------------------------------------------------------------------
def saludar_usuario(nombre: str) -> str:
    """Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola {nombre}!"


# 3) ---------------------------------------------------------------------------
def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    """
    Imprime la información personal en el formato solicitado.
    Ej: 'Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]'.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4) ---------------------------------------------------------------------------
def calcular_area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)


def calcular_perimetro_circulo(radio: float) -> float:
    """Devuelve el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio


# 5) ---------------------------------------------------------------------------
def segundos_a_horas(segundos: int | float) -> float:
    """Convierte una cantidad de segundos a horas (valor flotante)."""
    return float(segundos) / 3600.0


# 6) ---------------------------------------------------------------------------
def tabla_multiplicar(numero: int) -> None:
    """Imprime la tabla de multiplicar del 1 al 10 para 'numero'."""
    for i in range(1, 11):
        print(f"{numero} x {i:>2} = {numero * i}")


# 7) ---------------------------------------------------------------------------
def operaciones_basicas(a: float, b: float) -> Tuple[float, float, float, Optional[float]]:
    """
    Devuelve una tupla con (suma, resta, multiplicación, división).
    La división es None si b == 0 para evitar división por cero.
    """
    suma = a + b
    resta = a - b
    mult = a * b
    div = None if b == 0 else a / b
    return (suma, resta, mult, div)


# 8) ---------------------------------------------------------------------------
def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el Índice de Masa Corporal (IMC = peso / altura^2)."""
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que 0.")
    return peso / (altura ** 2)


# 9) ---------------------------------------------------------------------------
def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32.0


# 10) --------------------------------------------------------------------------
def calcular_promedio(a: float, b: float, c: float) -> float:
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3.0


# Utilidades de entrada --------------------------------------------------------
def _leer_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip())
        except ValueError:
            print("Valor inválido. Intente nuevamente (use números).")


def _leer_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Valor inválido. Intente nuevamente (use enteros).")


# Programa principal con menú --------------------------------------------------
def main() -> None:
    opciones = {
        "1": "imprimir_hola_mundo",
        "2": "saludar_usuario",
        "3": "informacion_personal",
        "4": "área y perímetro del círculo",
        "5": "segundos a horas",
        "6": "tabla de multiplicar",
        "7": "operaciones básicas",
        "8": "calcular IMC",
        "9": "Celsius a Fahrenheit",
        "10": "calcular promedio",
        "0": "salir",
    }

    while True:
        print("\n=== PRÁCTICO 2: FUNCIONES EN PYTHON ===")
        for k in ["1","2","3","4","5","6","7","8","9","10","0"]:
            print(f"{k:>2}) {opciones[k]}")
        elec = input("Elija una opción: ").strip()

        if elec == "0":
            print("Saliendo... ¡Éxitos!")
            break

        if elec == "1":
            imprimir_hola_mundo()

        elif elec == "2":
            nombre = input("Ingrese su nombre: ").strip()
            print(saludar_usuario(nombre))

        elif elec == "3":
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            edad = _leer_int("Edad (entero): ")
            residencia = input("Residencia (ciudad/país): ").strip()
            informacion_personal(nombre, apellido, edad, residencia)

        elif elec == "4":
            r = _leer_float("Radio del círculo: ")
            area = calcular_area_circulo(r)
            peri = calcular_perimetro_circulo(r)
            print(f"Área = {area:.4f}")
            print(f"Perímetro = {peri:.4f}")

        elif elec == "5":
            seg = _leer_float("Segundos: ")
            horas = segundos_a_horas(seg)
            print(f"{seg:.0f} segundos equivalen a {hojas:=.4f}")
            # Correction: variable name typo fixed below
        elif elec == "5":
            seg = _leer_float("Segundos: ")
            horas = segundos_a_horas(seg)
            print(f"{seg:.0f} segundos equivalen a {horas:.4f} horas.")

        elif elec == "6":
            n = _leer_int("Número para la tabla (entero): ")
            tabla_multiplicar(n)

        elif elec == "7":
            a = _leer_float("a: ")
            b = _leer_float("b: ")
            s, r, m, d = operaciones_basicas(a, b)
            print(f"Suma: {s}")
            print(f"Resta: {r}")
            print(f"Multiplicación: {m}")
            print("División:", "indefinida (b=0)" if d is None else f"{d}")

        elif elec == "8":
            peso = _leer_float("Peso (kg): ")
            altura = _leer_float("Altura (m): ")
            try:
                imc = calcular_imc(peso, altura)
                print(f"IMC: {imc:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif elec == "9":
            c = _leer_float("Temperatura (°C): ")
            f = celsius_a_fahrenheit(c)
            print(f"{c:.2f} °C = {f:.2f} °F")

        elif elec == "10":
            a = _leer_float("a: ")
            b = _leer_float("b: ")
            c = _leer_float("c: ")
            prom = calcular_promedio(a, b, c)
            print(f"Promedio: {prom:.4f}")

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
