# ==========================================
# Trabajo Práctico 1 - Estructuras Secuenciales
# Alumno: Ramiro Barra Soto
# ==========================================

# Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Ejercicio 1, imprimir por pantalla el mensaje: “Hola Mundo!”\n")
print("Hola Mundo!\n")

# ------------------------------------------

# Ejercicio 2
# Crear un programa que pida al usuario su nombre e imprima un saludo.
print("Ejercicio 2, pedir al usuario su nombre e imprima un saludo.\n")
nombre = input("Ingresá tu nombre: ")
print("\n")
print(f"Hola {nombre}!\n")

# ------------------------------------------

# Ejercicio 3
# Crear un programa que pida nombre, apellido, edad y residencia.
print("Ejercicio 3, pedir al usuario nombre, apellido, edad, residencia e imprimir un mensaje en pantalla. \n")
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
while True:
    try:
        edad = int(input("Ingresá tu edad: "))
        break  
    except ValueError:
        print("❌ Error: Debés ingresar un número para la edad.")

residencia = input("Ingresá tu lugar de residencia: ")
print()
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.\n")

# ------------------------------------------

# Ejercicio 4
# Crear un programa que pida el radio de un círculo y muestre su área y perímetro.
print("Ejercicio 4, pedir el radio de un círculo y mostrar su área y perímetro.\n")

import math

radio = float(input("Ingresá el radio del círculo: "))
print()
area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}\n")

# ------------------------------------------

# Ejercicio 5
# Crear un programa que pida una cantidad de segundos y los convierta en horas.
print("Ejercicio 5, pedir una cantidad de segundos y convertirlos en horas.\n")
segundos = int(input("Ingresá la cantidad de segundos: "))
print()
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.\n")

# ------------------------------------------

# Ejercicio 6
# Crear un programa que pida un número y muestre su tabla de multiplicar.
print("Ejercicio 6, pedir un número y mostrar su tabla de multiplicar.\n")
numero = int(input("Ingresá un número: "))
print(f"Tabla de multiplicar del {numero}: /n")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}\n")

# ------------------------------------------

# Ejercicio 7
# Crear un programa que pida dos números y muestre suma, resta, multiplicación y división.
print("Ejercicio 7, pedir dos números y mostrar suma, resta, multiplicación y división.\n")
a = int(input("Ingresá el primer número (≠ 0): "))
b = int(input("Ingresá el segundo número (≠ 0): "))
print()

print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}\n")

# ------------------------------------------

# Ejercicio 8
# Crear un programa que calcule el IMC (peso / altura^2).
print("Ejercicio 8, calcular el IMC (Índice de Masa Corporal).\n")
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
print()

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}\n")

# ------------------------------------------

# Ejercicio 9
# Crear un programa que convierta Celsius a Fahrenheit.
print("Ejercicio 9, convertir Celsius a Fahrenheit.\n")
celsius = float(input("Ingresá la temperatura en °C: "))
print()
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F\n")

# ------------------------------------------

# Ejercicio 10
# Crear un programa que calcule el promedio de 3 números.
print("Ejercicio 10, calcular el promedio de 3 números.\n")
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))
print()

promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}\n")
