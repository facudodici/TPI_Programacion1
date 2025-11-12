ARCHIVO = "paises.csv"

def normalizar(s):
    return " ".join(s.strip().lower().split())


def pedir_entero(mensaje):   # Validamos que se ingresen numeros
    n = input(mensaje).strip()
    while not n.isdigit():
        print("Debe ingresar un número entero (sin comas ni puntos).")
        n = input(mensaje).strip()
    return int(n)

def cargar_paises():
    lista = []
    try:
        with open(ARCHIVO, "a+") as f:    # a+ para read and write
            f.seek(0)
            lineas = f.readlines()
            if len(lineas) <= 1:
                if len(lineas) == 0:
                    print(f"Archivo '{ARCHIVO}' no existe. Se creará al guardar el primer país.")
                else:
                    print(f"Archivo '{ARCHIVO}' existe pero está vacío (solo encabezado o sin datos).")
                return lista

            for i in range(1, len(lineas)):  # salto encabezado
                linea = lineas[i].strip()
                if linea == "":
                    continue
                partes = linea.split(",")
                if len(partes) != 4:
                    print("Línea con formato inválido en CSV (se ignora).")
                    continue

                nombre = partes[0].strip()
                pobl = partes[1].strip()
                sup = partes[2].strip()
                cont = partes[3].strip()

                if pobl.isdigit():
                    pobl = int(pobl)
                else:
                    pobl = 0

                if sup.isdigit():
                    sup = int(sup)
                else:
                    sup = 0

                lista.append({
                    "NOMBRE": nombre,
                    "POBLACION": pobl,
                    "SUPERFICIE": sup,
                    "CONTINENTE": cont
                })

    except Exception as e:
        print("Error al leer el archivo:", e)

    return lista


def guardar_paises(lista):
    try:
        with open(ARCHIVO, "w") as f:
            f.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")
            for p in lista:
                f.write(f"{p['NOMBRE']},{p['POBLACION']},{p['SUPERFICIE']},{p['CONTINENTE']}\n")
    except Exception as e:
        print("Error al guardar el archivo:", e)


def buscar_pais(lista, nombre):
    nombre_n = normalizar(nombre)
    for i, p in enumerate(lista):
        p_n = normalizar(p["NOMBRE"])
        if p_n == nombre_n:
            print(f"{p['NOMBRE']} - Población: {p['POBLACION']} - Superficie: {p['SUPERFICIE']} - Continente: {p['CONTINENTE']}")
            return i
    return -1


def agregar_pais(lista):
    nombre = input("Nombre del país: ").strip()
    while nombre == "" or buscar_pais(lista, nombre) != -1:
        if nombre == "":
            print("El nombre no puede estar vacío.")
        else:
            print("Ese país ya existe. Ingresá otro nombre.")
        nombre = input("Nombre del país: ").strip()

    pobl = pedir_entero("Población (entero): ")
    sup = pedir_entero("Superficie en km² (entero): ")

    cont = input("Continente: ").strip()
    while cont == "":
        print("Continente no puede quedar vacío.")
        cont = input("Continente: ").strip()

    lista.append({
        "NOMBRE": nombre,
        "POBLACION": pobl,
        "SUPERFICIE": sup,
        "CONTINENTE": cont
    })

    guardar_paises(lista)
    print("País agregado correctamente.")


def actualizar_pais(lista):
    nombre = input("Nombre del país a actualizar: ").strip()
    pos = buscar_pais(lista, nombre)

    if pos == -1:
        print("País no encontrado.")
        return

    print("Dejar en blanco para no modificar el campo.")
    nuevo_pob = input("Nueva población: ").strip()
    nueva_sup = input("Nueva superficie: ").strip()

    if nuevo_pob != "":
        if nuevo_pob.isdigit():
            lista[pos]["POBLACION"] = int(nuevo_pob)
        else:
            print("Población inválida. No se cambió.")

    if nueva_sup != "":
        if nueva_sup.isdigit():
            lista[pos]["SUPERFICIE"] = int(nueva_sup)
        else:
            print("Superficie inválida. No se cambió.")

    guardar_paises(lista)
    print("Actualización completada.")


def mostrar_todos(lista):
    if not lista:
        print("No hay países cargados.")
        return

    print("LISTADO DE PAÍSES:")
    for i, p in enumerate(lista):
        print(f"[{i}] {p['NOMBRE']} - Población: {p['POBLACION']} - Superficie: {p['SUPERFICIE']} km² - Continente: {p['CONTINENTE']}")


def filtrar_por_continente(lista):
    cont = input("Continente a filtrar: ").strip().lower()
    resultados = [p for p in lista if p["CONTINENTE"].strip().lower() == cont]

    if not resultados:
        print("No se encontraron países en ese continente.")
        return

    for p in resultados:
        print(f"{p['NOMBRE']} - Población: {p['POBLACION']} - Superficie: {p['SUPERFICIE']} - Continente: {p['CONTINENTE']}")


def filtrar_por_rango(lista, campo):
    print("Ingrese valores enteros. Dejar vacío para omitir límite.")
    minimo = input("Mínimo: ").strip()
    maximo = input("Máximo: ").strip()

    def convertir(x):
        return int(x) if x.isdigit() else None

    minimo = convertir(minimo)
    maximo = convertir(maximo)

    resultados = []
    for p in lista:
        valor = p[campo]
        ok = True

        if minimo is not None and valor < minimo:
            ok = False
        if maximo is not None and valor > maximo:
            ok = False

        if ok:
            resultados.append(p)

    if not resultados:
        print("No hay resultados para ese rango.")
        return

    for r in resultados:
        print(r)


def ordenar_paises(lista, criterio, asc=True):
    if criterio == "NOMBRE":
        lista.sort(key=lambda x: normalizar(x["NOMBRE"]), reverse=not asc)
    else:
        lista.sort(key=lambda x: x[criterio], reverse=not asc)

    print("Lista ordenada.")
    guardar_paises(lista)


def mostrar_estadisticas(lista):
    if not lista:
        print("No hay datos cargados.")
        return

    mayor = max(lista, key=lambda x: x["POBLACION"])
    menor = min(lista, key=lambda x: x["POBLACION"])
    prom_pob = sum(x["POBLACION"] for x in lista) / len(lista)
    prom_sup = sum(x["SUPERFICIE"] for x in lista) / len(lista)

    continentes = {}
    for p in lista:
        c = p["CONTINENTE"]
        continentes[c] = continentes.get(c, 0) + 1

    print(f"País con mayor población: {mayor['NOMBRE']} ({mayor['POBLACION']})")
    print(f"País con menor población: {menor['NOMBRE']} ({menor['POBLACION']})")
    print(f"Promedio de población: {prom_pob:.2f}")
    print(f"Promedio de superficie: {prom_sup:.2f}")
    print("Cantidad de países por continente:")
    for c, n in continentes.items():
        print(f"  {c}: {n}")

# MENU
def mostrar_menu():
    print("===== GESTIÓN DE PAÍSES =====")
    print("1. Agregar país")
    print("2. Actualizar población/superficie")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Mostrar todos")
    print("8. Salir")


def main():
    paises = cargar_paises()
    print(f"Paises cargados: {len(paises)}")

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            termino = input("Escriba el NOMBRE COMPLETO del país: ").strip()
            pos = buscar_pais(paises, termino)
            if pos == -1:
                print("No se encontraron coincidencias.")

        elif opcion == "4":
            print("a) Por continente")
            print("b) Por rango de población")
            print("c) Por rango de superficie")
            sub = input("Elija filtro (a/b/c): ").strip().lower()

            if sub == "a":
                filtrar_por_continente(paises)
            elif sub == "b":
                filtrar_por_rango(paises, "POBLACION")
            elif sub == "c":
                filtrar_por_rango(paises, "SUPERFICIE")
            else:
                print("Opción inválida.")

        elif opcion == "5":
            print("Ordenar por: 1) NOMBRE 2) POBLACION 3) SUPERFICIE")
            c = input("Elija 1/2/3: ").strip()
            asc = input("Ascendente? (s/n): ").strip().lower() == "s"

            if c == "1":
                ordenar_paises(paises, "NOMBRE", asc)
            elif c == "2":
                ordenar_paises(paises, "POBLACION", asc)
            elif c == "3":
                ordenar_paises(paises, "SUPERFICIE", asc)
            else:
                print("Opción inválida.")

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            mostrar_todos(paises)

        elif opcion == "8":
            print("Saliendo... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
