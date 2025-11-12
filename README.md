README — Gestión de Países (TPI)

Archivo: TPI_Programacion1.py
CSV por defecto: paises.csv
Autor / Integrantes: Facundo Nicolás Martino, Julián Campanini

Descripción

Aplicación de consola en Python para gestionar un listado de países almacenado en un CSV. Permite:

Cargar y guardar países en paises.csv.

Agregar nuevos países (nombre, población, superficie, continente).

Actualizar población o superficie de un país existente.

Buscar un país por nombre.

Filtrar por continente o por rango de población/superficie.

Ordenar por nombre, población o superficie (asc/desc).

Mostrar estadísticas básicas (mayor/menor población, promedios, conteo por continente).

Es una versión estilo estudiante, pensada para un trabajo práctico (TPI).

Requisitos

Python 3.8+ (probado con 3.8/3.10)

No requiere librerías externas (usa sólo la stdlib).

Archivo CSV con encabezado UTF-8 recomendado.

Estructura esperada del CSV

Nombre del archivo por defecto: paises.csv
Cabecera obligatoria (las líneas se guardan con este header):

NOMBRE,POBLACION,SUPERFICIE,CONTINENTE


Ejemplo de contenido válido:

NOMBRE,POBLACION,SUPERFICIE,CONTINENTE
Argentina,45800000,2780400,América
Francia,67000000,643801,Europa
Brasil,213000000,8515767,América


Notas:

Población y superficie se manejan como enteros (si no son dígitos, el programa los convierte a 0 al cargar).

El programa crea paises.csv la primera vez que se guarda un país si no existe.

Uso / Ejecución

Guardar el archivo TPI_Programacion1.py (o el nombre que uses) en una carpeta.

(Opcional) Colocar paises.csv en la misma carpeta o dejar que el programa lo cree.

Ejecutar en consola:

python TPI_Programacion1.py


Al iniciar se mostrará la cantidad de países cargados y luego el menú principal.

Menú (funcionalidades y flujo)

Al ejecutar verás:

===== GESTIÓN DE PAÍSES =====
1. Agregar país
2. Actualizar población/superficie
3. Buscar país por nombre
4. Filtrar países
5. Ordenar países
6. Estadísticas
7. Mostrar todos
8. Salir


1 Agregar país: solicita nombre (único), población (entero), superficie (entero) y continente. Guarda automáticamente.

2 Actualizar: pregunta por nombre y permite dejar campos en blanco para no modificar. Valida que las entradas numéricas sean dígitos.

3 Buscar: buscar por nombre exacto (se normaliza antes de comparar).

4 Filtrar: submenú

a) Por continente (case-insensitive)

b) Rango de población (mínimo/máximo, dejar vacío para omitir límite)

c) Rango de superficie (igual que población)

5 Ordenar: elegir criterio (NOMBRE/POBLACION/SUPERFICIE) y ascendente/descendente. Guarda cambios al ordenar.

6 Estadísticas: muestra país con mayor/menor población, promedios de población y superficie y conteo por continente.

7 Mostrar todos: lista completa con índice.

8 Salir: termina ejecución.

Formato de entrada y validaciones importantes

El campo nombre no puede quedar vacío ni duplicarse.

Población y superficie deben ser enteros; el helper pedir_entero fuerza esta validación al pedir datos. Al cargar desde CSV, si el campo no es dígito se interpreta como 0.

buscar_pais usa normalizar que hace .strip().lower() y elimina espacios redundantes, por lo que las búsquedas son insensibles a mayúsculas y espacios extras.

Para filtros por rango: si dejas mínimo o máximo vacío, se omite ese límite.

Cambiar la ruta/archivo CSV

El script usa la variable global ARCHIVO = "paises.csv".
Para usar otra ruta o nombre de archivo, cambiar esa constante al inicio:

ARCHIVO = "ruta/mi_paises.csv"
