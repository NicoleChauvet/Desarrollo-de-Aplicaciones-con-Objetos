import csv

from entities.Cirugia import Cirugia
from entities.Consulta import Consulta

def lector_csv(ruta_archivo):
    lista_atenciones = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue

                try:
                    tipo = int(fila[0].strip())
                    fecha = fila[1].strip()
                    veterinario = fila[2].strip()
                    mascota = fila[3].strip()
                    costo_base = float(fila[4].strip())

                    if tipo == 1:
                        cantidad_vacunas = int(fila[5].strip())
                        cons = Consulta(fecha, veterinario, mascota, costo_base, cantidad_vacunas)
                        lista_atenciones.append(cons)

                    else:
                        horas_quirofano = float(fila[5].strip())
                        ciru = Cirugia(fecha, veterinario, mascota, costo_base, horas_quirofano)
                        lista_atenciones.append(ciru)

                except (IndexError, ValueError) as e:
                    print(f" (x) Error: hubo un error en linea {numero_linea}")

    except PermissionError:
        print(f" (x) Error: no se tienen permisos de lectura del archivo {e}")
    except FileNotFoundError:
        print(f" (x) Error: no se encontro el archivo {e}")
    except Exception as e:
        print(f" (x) Error: ocurrio un error inesperado {e}")

    return lista_atenciones