import csv
from models.ADomicilio import ADomicilio
from models.EnTaller import EnTaller

def lector_csv(ruta_archivo):
    lista_reparaciones = []

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
                    equipo = fila[3].strip()
                    costo_base = float(fila[4].strip())

                    if tipo == 1:
                        kilometros = int(fila[5].strip())
                        domicilio = ADomicilio(codigo, cliente, equipo, costo_base, kilometros)
                        lista_reparaciones.append(domicilio)
                    elif tipo == 2:
                        dias_estadia = int(fila[5].strip())
                        taller = EnTaller(codigo, cliente, equipo, costo_base, dias_estadia)
                        lista_reparaciones.append(taller)

                except (IndexError, ValueError) as e:
                    print(f" (x) Error: hubo un error en la linea {numero_linea} como {e}")

    except FileNotFoundError:
        print(f" (x) Error: no se encontro el archivo {ruta_archivo}")
    except PermissionError:
        print(f" (x) Error: no se tienen permisos de lectura del archivo {ruta_archivo}")
    except Exception as e:
        print(f" (x) Error: hubo un error inesperado {e}")

    return lista_reparaciones
