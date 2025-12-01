# 🌍 Gestión de Países en Python  
### Trabajo Práctico Integrador – Programación 1  
### Tecnicatura Universitaria en Programación – UTN  
---

## 📌 Descripción del Proyecto  
Este programa permite gestionar información de países utilizando **listas, diccionarios, funciones, archivos CSV, filtros, ordenamientos y estadísticas básicas**.  
El objetivo es aplicar los contenidos principales de Programación 1 mediante una aplicación modular, clara y funcional que opere por consola.

La aplicación carga los datos desde un archivo **CSV**, permite modificarlos y luego guardar los cambios.

---

## 🧩 Funcionalidades Principales  

### 🔹 Gestión de países  
- Agregar un país (validación de campos obligatorios).  
- Actualizar población y superficie.  
- Buscar países por coincidencia parcial o exacta del nombre.  

### 🔹 Filtros  
- Por continente.  
- Por rango de población.  
- Por rango de superficie.  

### 🔹 Ordenamientos  
- Por nombre.  
- Por población.  
- Por superficie (ascendente o descendente).  

### 🔹 Estadísticas  
- País con mayor población.  
- País con menor población.  
- Promedio de población.  
- Promedio de superficie.  
- Cantidad de países por continente.  

---

## 📂 Estructura del Proyecto  

TPI_Paises
│
├── paises.csv # Base de datos inicial
├── programa.py # Código principal en Python
├── README.md # Este archivo
└── /capturas # (Opcional) Evidencias de funcionamiento


---

## 🗂 Archivo CSV (dataset)

El sistema utiliza un archivo llamado `paises.csv` con el siguiente formato:

nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
Australia,26000000,7692024,Oceanía


---

## ▶️ Instrucciones para ejecutar el programa

### 1️⃣ Requisitos
- Python 3.x  
- Archivo `paises.csv` en la misma carpeta que `programa.py`

### 2️⃣ Ejecutar el programa
Abrir una terminal en la carpeta del proyecto y ejecutar:


### 3️⃣ Usar el menú interactivo  
El programa mostrará opciones como estas:

1. Agregar país

2. Actualizar país

3. Buscar país

4. Filtrar países

5. Ordenar países

6. Estadísticas

7. Guardar CSV

8. Salir


---

## 🧠 Conceptos aplicados en el proyecto

El trabajo integra los siguientes contenidos de la materia:

- Listas  
- Diccionarios  
- Funciones y modularización  
- Condicionales  
- Bucles  
- Ordenamientos con `sorted()`  
- Manejo de archivos CSV  
- Manejo básico de errores  
- Entrada y validación de datos  

---

## 📸 Ejemplos de ejecución

### Agregar país
Nombre: Chile
Población: 19107216
Superficie: 756102
Continente: América
✔ País agregado correctamente.


### Estadísticas
País con mayor población: Brasil
País con menor población: Australia
Promedio de población: 98900383.2
Promedio de superficie: 3973644.6
Países por continente:
{'América': 3, 'Asia': 1, 'Europa': 1, 'Oceanía': 1}


---

## 👥 Integrantes grupo81
- **Ramiro Barra Soto**  

---

## 📝 Licencia  
Proyecto académico sin fines comerciales.  
Uso permitido únicamente para fines educativos y de evaluación dentro de la asignatura.

---

## 🎓 Conclusión  
Este trabajo permitió consolidar los conceptos de estructuras de datos, manipulación de archivos, modularización y análisis de información mediante estadísticas simples. Además, se reforzó la importancia de la validación de datos y el diseño de programas organizados y legibles.

---

