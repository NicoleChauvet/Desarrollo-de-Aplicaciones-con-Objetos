import csv
from models.Nacional import Nacional
from models.Internacional import Internacional

def lector_csv(ruta_archivo):
    lista_paquetes = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue
                try:
                    tipo = int(fila[0].strip())
                    codigo = int(fila[1].strip())
                    cliente = fila[2].strip()
                    cant_personas = int(fila[3].strip())
                    precio_base = float(fila[4].strip())

                    if tipo == 1:
                        traslado = (int(fila[5].strip()) == 1)
                        p = Nacional(codigo, cliente, cant_personas, precio_base, traslado)
                    else:
                        seguro = float(fila[5].strip())
                        p = Internacional(codigo, cliente, cant_personas, precio_base, seguro)

                    lista_paquetes.append(p)

                except (IndexError, ValueError) as e:
                    print(f" (x) Error: hubo un error en la fila {numero_linea} as {e}")

    except FileNotFoundError:
        print(f" (x) Error: no existe el archivo {ruta_archivo}")
    except PermissionError:
        print(f" (x) Error: no se tienen permisos de lectura del archivo {ruta_archivo}")
    except Exception as e:
        print(f" (x) Error: ocurrio un error inesperado al abrir el archivo {e}")

    return lista_paquetes