from functions.lectorBidonCSV import leerCSV as leer_bidones
from functions.lectorCajaCSV import leerCSV as leer_cajas
from functions.lectorPackingCSV import leerCSV as leer_packing
from entities.Camion import Camion

# --- Datos iniciales ---
lista_bidones = leer_bidones("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/transporte/data/bidones.csv")
lista_cajas = leer_cajas("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/transporte/data/cajas.csv")
lista_packing = leer_packing("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/transporte/data/packing.csv")
print("Cajas:", len(lista_cajas))
print("Packing:", len(lista_packing))
print("Bidones:", len(lista_bidones))

camion1 = Camion("AA534BT", "disponible", 87)
camion2 = Camion("OKT071", "en reparacion", 130)

camiones = {1: camion1, 2: camion2}


def elegir_camion():
    print("\n--- Elegí un camión ---")
    print(f" (1) {camion1}")
    print(f" (2) {camion2}")
    op = int(input("Camión: "))
    return camiones.get(op)


def elegir_carga():
    print("\n--- Elegí de qué lista tomar la carga ---")
    print(" (1) Cajas sueltas")
    print(" (2) Packing")
    print(" (3) Bidones")
    tipo = int(input("Tipo de carga: "))

    if tipo == 1:
        lista = lista_cajas
    elif tipo == 2:
        lista = lista_packing
    elif tipo == 3:
        lista = lista_bidones
    else:
        print("Opción inválida.")
        return None

    if not lista:
        print("Esa lista está vacía.")
        return None

    for i, carga in enumerate(lista):
        print(f" ({i}) {carga}")

    idx = int(input("Índice de la carga: "))
    try:
        return lista[idx]
    except IndexError:
        print("Índice inválido.")
        return None


def menu():
    op = -1
    while op != 0:
        print("\n===== MENÚ =====")
        print(" (1) Listar cargas sueltas disponibles")
        print(" (2) Agregar carga a un camión")
        print(" (3) Bajar carga de un camión")
        print(" (4) Total de carga de un camión")
        print(" (5) Poner camión en reparación")
        print(" (6) Camión sale reparado")
        print(" (7) Mandar camión de viaje")
        print(" (8) Camión de regreso")
        print(" (9) Ver cargas de un camión (cargas_en_orden)")
        print(" (10) ¿Camión listo para salir?")
        print(" (0) Salir")

        op = int(input("Opción: "))

        if op == 1:
            print("\n-- Cajas --")
            for c in lista_cajas:
                print(c)
            print("\n-- Packing --")
            for p in lista_packing:
                print(p)
            print("\n-- Bidones --")
            for b in lista_bidones:
                print(b)

        elif op == 2:
            camion = elegir_camion()
            carga = elegir_carga()
            if camion and carga:
                camion.subir_carga(carga)

        elif op == 3:
            camion = elegir_camion()
            if camion:
                if camion.cantidad_cargas() == 0:
                    print("El camión no tiene cargas.")
                else:
                    for i, c in enumerate(camion.cargas):
                        print(f" ({i}) {c}")
                    idx = int(input("Índice de la carga a bajar: "))
                    try:
                        camion.bajar_carga(camion.cargas[idx])
                    except IndexError:
                        print("Índice inválido.")

        elif op == 4:
            camion = elegir_camion()
            if camion:
                print(f"Peso total cargado: {camion.peso_cargas()} kg")

        elif op == 5:
            camion = elegir_camion()
            if camion:
                camion.a_reparacion()
                print(f"Estado actual: {camion.estado}")

        elif op == 6:
            camion = elegir_camion()
            if camion:
                camion.sale_reparado()
                print(f"Estado actual: {camion.estado}")

        elif op == 7:
            camion = elegir_camion()
            if camion:
                camion.en_viaje()
                print(f"Estado actual: {camion.estado}")

        elif op == 8:
            camion = elegir_camion()
            if camion:
                camion.de_regreso()
                print(f"Estado actual: {camion.estado}")

        elif op == 9:
            camion = elegir_camion()
            if camion:
                print(camion.cargas_en_orden())

        elif op == 10:
            camion = elegir_camion()
            if camion:
                print("Listo para salir:", camion.listo_para_salir())

        elif op == 0:
            print("Saliendo...")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
