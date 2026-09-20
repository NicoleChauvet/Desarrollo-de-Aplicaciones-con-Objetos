import csv
from entities.Farmacia import Farmacia

def leer_csv(ruta_archivo):
    lista_farmacia = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            encabezado = next(leer_csv, None)

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue

                try:
                    codigo = int(fila[0].strip())
                    tipo_cobro = int(fila[1].strip())
                    importe = float(fila[2].strip())
                    cupon = float(fila[3].strip)

                    f = Farmacia(codigo, tipo_cobro, importe, cupon)
                    lista_farmacia.append(f)

                except (IndexError, ValueError) as e:
                    print(f"Error: en la linea {numero_linea} hubo un error inesperado {e}")

    except FileNotFoundError:
        print(f"Error: error en el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: no se tienen permisos para leer {ruta_archivo}")
    except Exception as e:
        print(f"Error: hubo un error inesperado al abrir el archivo {e}")

    return lista_farmacia