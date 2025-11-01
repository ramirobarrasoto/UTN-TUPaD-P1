# 📘 Parcial 2 – Programación 1  
### **Sistema de Biblioteca (con persistencia en CSV)**  
**Autor:** *Ramiro Barra Soto*  
**Lenguaje:** Python 3.10 o superior  

---

## 🧩 Descripción General  
Este programa permite gestionar un pequeño catálogo de biblioteca escolar.  
Se desarrolla completamente con estructuras básicas de Python, sin excepciones, clases ni estructuras avanzadas, cumpliendo las consignas del trabajo práctico.

Los datos se almacenan en un archivo `catalogo.csv`, que se actualiza automáticamente con cada operación realizada.

---

## 🧠 Funcionalidades Principales  

1. **Ingresar títulos (múltiples)**  
   - Permite cargar varios libros nuevos con su cantidad de ejemplares inicial.  
   - Valida que el título no esté repetido y no sea vacío.  

2. **Ingresar ejemplares (sumar/restar)**  
   - Muestra el catálogo numerado.  
   - Permite aumentar o disminuir la cantidad disponible de un título existente.  
   - Controla que no se resten más ejemplares de los disponibles.  

3. **Mostrar catálogo completo**  
   - Lista todos los títulos con su cantidad actual de ejemplares.  

4. **Consultar disponibilidad de un título**  
   - Permite buscar un libro por nombre (sin distinguir mayúsculas/minúsculas).  
   - Informa la cantidad de ejemplares disponibles.  

5. **Listar libros agotados**  
   - Muestra los títulos con cantidad igual a 0.  

6. **Agregar título nuevo**  
   - Carga un nuevo libro validando que no exista en el catálogo.  

7. **Actualizar ejemplares (préstamo / devolución)**  
   - Permite registrar un préstamo (resta 1 ejemplar) o una devolución (suma 1 ejemplar).  
   - Evita préstamos cuando no hay stock.  

8. **Salir del sistema**  
   - Solicita confirmación antes de cerrar el programa. 👋  

---

## 💾 Estructura del Archivo CSV  

El archivo `catalogo.csv` contiene los datos del catálogo con el siguiente formato:

