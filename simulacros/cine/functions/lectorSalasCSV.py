import csv

from entities.Sala2D import Sala2D
from entities.Sala3D import Sala3D
from entities.SalaVIP import SalaVIP

def lector_csv(ruta_archivo):
    lista_salas = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(leer_csv, start=1):

                if not fila:
                    continue

                try:
                    tipo = int(fila[0].strip())
                    numero = int(fila[1].strip())
                    capacidad = int(fila[2].strip())
                    recaudacion = float(fila[3].strip())

                    if tipo == 1:
                        premium = True if int(fila[4].strip()) else False
                        s2d = Sala2D(numero, capacidad, recaudacion, premium)
                        lista_salas.append(s2d)

                    elif tipo == 2:
                        adicional_lentes = float(fila[4].strip())
                        s3d = Sala3D(numero, capacidad, recaudacion, adicional_lentes)
                        lista_salas.append(s3d)
                    else:
                        costo_servicio = float(fila[4].strip())
                        svip = SalaVIP(numero, capacidad, recaudacion, costo_servicio)
                        lista_salas.append(svip)

                except (IndexError, ValueError) as e:
                    print(f"Error: se encontraron problemas en la linea {numero_linea}")

    except PermissionError:
        print(f"Error: no se tienen permisos de lectura del archivo {ruta_archivo}")
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error: hubo un error inesperado {e}")

    return lista_salas
