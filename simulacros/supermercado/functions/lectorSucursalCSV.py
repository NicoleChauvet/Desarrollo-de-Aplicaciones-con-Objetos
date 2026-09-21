import csv

from entities.Hiper import Hiper
from entities.Mini import Mini
from entities.Super import Super

def lector_csv(ruta_archivo):
    lista_inmuebles = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(leer_csv, start=1):

                if not fila:
                    continue

                try:
                    numero = int(fila[1].strip())
                    superficie = int(fila[2].strip())
                    facturacion = float(fila[3].strip())

                    if int(fila[0].strip()) == 1:
                        alquileres = int(fila[4].strip())
                        h = Hiper(numero, superficie, facturacion, alquileres)
                        lista_inmuebles.append(h)

                    elif int(fila[0].strip()) == 2:
                        mayorista = True if int(fila[4].strip()) == 1 else False
                        s = Super(numero, superficie, facturacion, mayorista)
                        lista_inmuebles.append(s)

                    else:
                        alquiler = int(fila[4].strip())
                        m = Mini(numero, superficie, facturacion, alquiler)
                        lista_inmuebles.append(m)

                except (IndexError, ValueError) as e:
                    print(f"Error: hubo un error inesperado en {numero_linea} como {e}")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo {ruta_archivo}")
    except PermissionError:
        print(f"Error: no se tiene permisos de lector del arhivo {ruta_archivo}")
    except Exception as e:
        print(f"Error: error inesperado al abrir el archivo ({e})")

    return lista_inmuebles