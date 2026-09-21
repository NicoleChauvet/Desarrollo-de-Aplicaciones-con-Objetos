from entities.Medica import Medica
from entities.Paciente import Paciente

import csv

def lector_csv(ruta_archivo, dicc_pacientes):
    lista_medica = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            lector_csv = csv.DictReader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(lector_csv, start=2):
                try:
                    #codigo,tipo_cobro,importe_consulta
                    codigo = int(fila["codigo"].strip())
                    tipo_cobro = int(fila["tipo_cobro"].strip())
                    importe = float(fila["importe_consulta"].strip())

                    if codigo in dicc_pacientes:
                        m = Medica(codigo, tipo_cobro, importe, dicc_pacientes[codigo])
                        lista_medica.append(m)
                    else:
                        print(f"Error: no se pudo anexar un paciente, codigo de atencion {codigo}")

                except (IndexError, ValueError) as e:
                    print(f"Error: se detecto un error en la linea {numero_linea} como {e}")

    except FileNotFoundError:
        print(f"Error: no existe el archivo {ruta_archivo}")
    except PermissionError:
        print(f"Error: no se tienen permisos de lectura del archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error: paso algo inesperado al abrir {ruta_archivo} ({e})")

    return lista_medica