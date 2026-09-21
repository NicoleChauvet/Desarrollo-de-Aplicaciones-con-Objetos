from entities.Paciente import Paciente

import csv

def lector_csv(ruta_archivo):
    dicc_pacientes = {}

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(lector_csv, start=2):
                try:
                    #codigo_atencion,nombre,sintoma,habitual
                    clave = int(fila["codigo_atencion"].strip())

                    nombre = fila["nombre"].strip()
                    sintoma = int(fila["sintoma"].strip())
                    habitual = fila["habitual"].strip().lower() == "true"

                    p = Paciente(nombre, sintoma, habitual)
                    dicc_pacientes[clave] = p

                except (IndexError, ValueError) as e:
                    print(f"Error: se detecto un error en la linea {numero_linea} como {e}")

    except FileNotFoundError:
        print(f"Error: error en el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: no se tienen permisos para leer {ruta_archivo}")
    except Exception as e:
        print(f"Error: hubo un error inesperado al abrir el archivo {e}")

    return dicc_pacientes

