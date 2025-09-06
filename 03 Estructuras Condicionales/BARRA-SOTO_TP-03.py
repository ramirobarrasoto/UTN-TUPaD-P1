# Práctico 3 – Estructuras Condicionales
# Autor: Ramiro Barra Soto
# Archivo: tp3_condicionales_ramiro-barra-soto.py
#
# NOTA: Estos 10 ejercicios cubren los casos más comunes de la unidad:
# if, elif, else; operadores relacionales y lógicos; condicionales anidadas;
# validación simple y mensajes claros de salida.
# Si tu enunciado exacto difiere, te lo adapto sin drama cuando me lo compartas.

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠ Ingresá un número entero válido.")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠ Ingresá un número válido (con punto si hace falta).")

# -------------------------------------------------------------------------
# EJERCICIO 1: Mayoría de edad.
def ej1_mayoria_edad():
    edad = pedir_int("Ingresá tu edad: ")
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("Es menor de edad.")

# -------------------------------------------------------------------------
# EJERCICIO 2: Nota numérica -> condición.
# (ejemplo clásico: < 6 desaprobado; >= 6 aprobado)
def ej2_nota_a_condicion():
    nota = pedir_int("Ingresá tu nota (0 a 10): ")
    if nota < 0 or nota > 10:
        print("Nota fuera de rango.")
    elif nota < 6:
        print("Desaprobado.")
    else:
        print("Aprobado.")       

# -------------------------------------------------------------------------
# EJERCICIO 3: Par o impar.
def ej3_paridad():
    n = pedir_int("Ingresá un número entero: ")
    # Paridad
    if n % 2 == 0:
        print("El número es par.") 
    else:
        print("El número es impar.")

# -------------------------------------------------------------------------
# EJERCICIO 4: Solicitar la edad al usuario y asignarle una categoría.
def ej4_categorias_por_edad():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Categoría: Niño/a")
    elif 12 <= edad < 18:
        print("Categoría: Adolescente")
    elif 18 <= edad < 30:
        print("Categoría: Adulto/a joven")
    else:
        print("Categoría: Adulto/a")

# -------------------------------------------------------------------------
# EJERCICIO 5: Solicitar contraseña al usuario.

def ej5_verificar_contrasena():
    contrasena = input("Ingresá tu contraseña que contenga entre 8 y 14 caracteres: ")

    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# -------------------------------------------------------------------------
# EJERCICIO 6: 
import random
from statistics import mean, median, mode

def ej6_estadisticas_lista():
    # Generar lista de 50 números aleatorios entre 1 y 100
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    # Calcular moda, mediana y media
    mi_moda = mode(numeros_aleatorios)
    mi_mediana = median(numeros_aleatorios)
    mi_media = mean(numeros_aleatorios)

    print("Lista de números:", numeros_aleatorios)
    print(f"Moda: {mi_moda}")
    print(f"Mediana: {mi_mediana}")
    print(f"Media: {mi_media:.2f}")

    # Comparación para determinar sesgo
    if mi_media > mi_mediana and mi_mediana > mi_moda:
        print("Sesgo positivo o a la derecha")
    elif mi_media < mi_mediana and mi_mediana < mi_moda:
        print("Sesgo negativo o a la izquierda")
    elif mi_media == mi_mediana == mi_moda:
        print("Sin sesgo (los tres son iguales)")
    else:
        print("No hay un sesgo claro en la distribución")


# -------------------------------------------------------------------------
# EJERCICIO 7: Frase terminada en vocal.

def ej7_frase_con_exclamacion():
    frase = input("Ingrese una palabra o frase: ")
    if frase[-1].lower() in "aeiou":  # verificamos última letra
        frase = frase + "!"
    print("Resultado:", frase)

# -------------------------------------------------------------------------
# EJERCICIO 8: Transformar nombre.

def ej8_transformar_nombre():
    nombre = input("Ingrese su nombre: ")
    opcion = input("Ingrese 1 para transformar en mayúsculas, 2 para Transformar en minúsculas o 3 para primera letra mayúscula: ")

    if opcion == "1":
        print("Resultado:", nombre.upper())
    elif opcion == "2":
        print("Resultado:", nombre.lower())
    elif opcion == "3":
        print("Resultado:", nombre.title())
    else:
        print("Opción no válida. Intente nuevamente.")

# -------------------------------------------------------------------------
# EJERCICIO 9: Clasificacion de terremoto.

def ej9_clasificar_terremoto():
    try:
        magnitud = float(input("Ingrese la magnitud del terremoto: "))

        if magnitud < 3:
            print("Muy leve (imperceptible).")
        elif 3 <= magnitud < 4:
            print("Leve (ligeramente perceptible).")
        elif 4 <= magnitud < 5:
            print("Moderado (sentido por personas, pero generalmente no causa daños).")
        elif 5 <= magnitud < 6:
            print("Fuerte (puede causar daños en estructuras débiles).")
        elif 6 <= magnitud < 7:
            print("Muy Fuerte (puede causar daños significativos).")
        else:
            print("Extremo (puede causar graves daños a gran escala).")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# -------------------------------------------------------------------------
# EJERCICIO 10: Determinar estaciones.

def ej10_determinar_estacion():
    try:
        hemisferio = input("Ingrese su hemisferio (N para norte, S para sur): ").strip().upper()
        mes = int(input("Ingrese el número del mes (1-12): "))
        dia = int(input("Ingrese el día (1-31): "))

        if hemisferio not in ["N", "S"]:
            print("Hemisferio no válido. Ingrese 'N' o 'S'.")
            return

        # Clasificación de estaciones según la tabla
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion_norte, estacion_sur = "Invierno", "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion_norte, estacion_sur = "Primavera", "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion_norte, estacion_sur = "Verano", "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion_norte, estacion_sur = "Otoño", "Primavera"
        else:
            print("Fecha inválida.")
            return

        # Mostrar resultado
        if hemisferio == "N":
            print(f"En el hemisferio norte, la estación es {estacion_norte}.")
        else:
            print(f"En el hemisferio sur, la estación es {estacion_sur}.")
    
    except ValueError:
        print("Por favor ingrese un número válido para mes y día.")

# -------------------------------------------------------------------------
# MENÚ
def menu():
    opciones = {
        "1": ("Mayoría de edad", ej1_mayoria_edad),
        "2": ("Aprobado o No aprobado", ej2_nota_a_condicion),
        "3": ("Par o impar", ej3_paridad),
        "4": ("Categoria por edad", ej4_categorias_por_edad),
        "5": ("Solicitar contraseña", ej5_verificar_contrasena),
        "6": ("Números aleatorios", ej6_estadisticas_lista),
        "7": ("Frase con exclamación", ej7_frase_con_exclamacion),
        "8": ("Transformar nombre", ej8_transformar_nombre),
        "9": ("Clasificación de terremoto", ej9_clasificar_terremoto),
        "10": ("Determinar estación", ej10_determinar_estacion),
        "0": ("Salir", None),
    }

    while True:
        print("\n=== TP3 – Condicionales ===")
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")
        eleccion = input("Elegí una opción: ").strip()
        if eleccion == "0":
            print("¡Listo! 👋")
            break
        elif eleccion in opciones:
            print(f"\n>> {opciones[eleccion][0]}")
            opciones[eleccion][1]() 
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
