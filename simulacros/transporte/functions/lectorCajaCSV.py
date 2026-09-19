import csv
from entities.Caja import Caja


def leerCSV(ruta_archivo):
    lista_cajas = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            encabezado = next(leer_csv, None)

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue
                try:
                    producto = fila[0].strip()
                    peso = int(fila[1].strip())

                    c = Caja(producto, peso)
                    lista_cajas.append(c)

                except (IndexError, ValueError) as e:
                    print(f"Error en la linea {numero_linea}: registro invalido {e}")

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: No se tienen permisos para leer {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado al abrir el archivo: {e}")

    return lista_cajas