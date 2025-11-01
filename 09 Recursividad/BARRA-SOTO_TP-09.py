"""
TP 9 - Recursividad
Versión interactiva con inputs
Autor: Ramiro barra soto
"""

# 1) Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales():
    num = int(input("Ingrese un número: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i} = {factorial(i)}")

# 2) Serie de Fibonacci recursiva
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    n = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))
    print("Serie de Fibonacci:")
    for i in range(n):
        print(fibonacci(i), end=" ")
    print()

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def probar_potencia():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base} elevado a la {exponente} = {potencia(base, exponente)}")

# 4) Conversión decimal a binario recursiva
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def probar_binario():
    n = int(input("Ingrese un número decimal: "))
    if n == 0:
        print("0")
    else:
        print(f"El número binario es: {decimal_a_binario(n)}")

# 5) Verificar palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    if es_palindromo(palabra):
        print("Es un palíndromo ✅")
    else:
        print("No es un palíndromo ❌")

# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    n = int(input("Ingrese un número entero positivo: "))
    print(f"La suma de sus dígitos es: {suma_digitos(n)}")

# 7) Pirámide de bloques recursiva
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def probar_piramide():
    n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(n)}")

# 8) Contar dígitos recursivo
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

def probar_contar_digito():
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a buscar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n--- TP7: Aplicación de la Recursividad ---")
        print("1) Factorial de un número")
        print("2) Serie Fibonacci")
        print("3) Potencia de un número")
        print("4) Conversión decimal a binario")
        print("5) Verificar palíndromo")
        print("6) Suma de dígitos")
        print("7) Contar bloques (pirámide)")
        print("8) Contar dígitos dentro de un número")
        print("9) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_factoriales()
        elif opcion == "2":
            mostrar_fibonacci()
        elif opcion == "3":
            probar_potencia()
        elif opcion == "4":
            probar_binario()
        elif opcion == "5":
            probar_palindromo()
        elif opcion == "6":
            probar_suma_digitos()
        elif opcion == "7":
            probar_piramide()
        elif opcion == "8":
            probar_contar_digito()
        elif opcion == "9":
            print("Saliendo del programa... 👋")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
