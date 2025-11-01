# Parcial Programación 1 - Biblioteca

Este programa simula la gestión de una **biblioteca escolar** utilizando estructuras secuenciales, condicionales y repetitivas en Python.  
Está implementado con `match/case` (Python 3.10+) y permite administrar un catálogo de libros con ejemplares disponibles.

## Funcionalidades

1. **Ingresar títulos (sin ejemplares):**  
   Permite cargar una lista inicial de títulos, con validación para evitar duplicados (case-insensitive).

2. **Ingresar ejemplares disponibles (sin título):**  
   Muestra los títulos enumerados y permite asignar, sumar o restar ejemplares a cada uno.

3. **Mostrar catálogo:**  
   Lista todos los títulos con la cantidad de ejemplares disponibles.

4. **Consultar disponibilidad de un título específico:**  
   Permite buscar un libro en el catálogo (ignora mayúsculas/minúsculas).  
   Si no existe, da la opción de volver a intentar.

5. **Listar agotados:**  
   Muestra los títulos que no tienen ejemplares disponibles.

6. **Agregar título (con cantidad de ejemplares):**  
   Agrega un nuevo libro al catálogo y la cantidad, validando duplicados.

7. **Actualizar ejemplares (préstamo/devolución):**  
   - **Préstamo:** resta un ejemplar si hay disponibles.  
   - **Devolución:** suma un ejemplar.  

8. **Salir:**  
   Solicita confirmación antes de cerrar el sistema.  
   Mensaje de despedida con emoji 👋.

## Requisitos

- Python **3.10 o superior** (para usar `match/case`).
- No utiliza excepciones, clases, funciones propias ni estructuras avanzadas, respetando las reglas del práctico.




