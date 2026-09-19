import csv
from entities.Packing import Packing

def leerCSV(ruta_archivo):
    lista_packing = []

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
                    cantidad = int(fila[2].strip())
                    estructura = int(fila[3].strip())

                    p = Packing(producto, peso, cantidad, estructura)
                    lista_packing.append(p)

                except (IndexError, ValueError) as e:
                    print(f"Error: registro invalido {e} en linea {numero_linea}")

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: No se tienen permisos para leer {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado al abrir el archivo: {e}")

    return lista_packing