import csv
from entities.Bidon import Bidon

def leerCSV(ruta_archivo):
    lista_bidones = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            encabezado = next(leer_csv, None)

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue
                try:
                    producto = fila[0].strip()
                    capacidad = int(fila[1].strip())
                    densidad = float(fila[2].strip())

                    b = Bidon(producto, capacidad, densidad)
                    lista_bidones.append(b)

                except (IndexError, ValueError) as e:
                    print(f"Error en linea {numero_linea}: Registro invalido {e}")

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: No se tienen permisos de lectura {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado al abrir el archivo: {e}")


    return lista_bidones