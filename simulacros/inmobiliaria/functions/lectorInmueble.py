import csv
from entities.Casa import Casa
from entities.Departamento import Departamento

def lector_csv(ruta_archivo):
    lista_inmuebles = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            for numero_linea, fila in enumerate(leer_csv, start=1):

                if not fila:
                    continue

                try:
                    tipo_inmueble = int(fila[0].strip())
                    codigo = int(fila[1].strip())
                    nombre = fila[2].strip()
                    importe_base = float(fila[3].strip())
                    superficie = int(fila[4].strip())

                    if tipo_inmueble == 1:
                        cant_habt = int(fila[5].strip())
                        pileta = True if int(fila[6].strip()) else False

                        c = Casa(codigo, nombre, superficie, importe_base, cant_habt, pileta)
                        lista_inmuebles.append(c)
                    else:
                        expensas = int(fila[5].strip())
                        piso = int(fila[6].strip())

                        d = Departamento(codigo, nombre, superficie, importe_base, expensas, piso)
                        lista_inmuebles.append(d)

                except (IndexError, ValueError) as e:
                    print(f"Error: en la linea {numero_linea} sucedio algo inesperado {e}")

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: no se tienen permisos de lectura de archivo {ruta_archivo}")
    except Exception as e:
        print(f"Error: sucedio algo inesperado al abrir el archivo: {e}")

    return lista_inmuebles
