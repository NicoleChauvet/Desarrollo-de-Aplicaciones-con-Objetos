import csv
from entities.Correctivo import Correctivo
from entities.Preventivo import Preventivo

def leer_csv(ruta_archivo):
    lista_mantenimientos = []

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
            leer_csv = csv.reader(archivo, delimiter=",")

            # si tuviera encabezados: encabezados = next(lector_csv, None)

            for numero_linea, fila in enumerate(leer_csv, start=1):
                if not fila:
                    continue
                try:
                    tipo = int(fila[0].strip())
                    fecha = fila[1].strip()
                    nombre = fila[2].strip()
                    importe = float(fila[3].strip())
                    if tipo == 1:
                        resultado = int(fila[4].strip())
                        impt_insumos = int(fila[5].strip())
                        p = Preventivo(fecha, nombre, importe, resultado, impt_insumos)
                        lista_mantenimientos.append(p)
                    else:
                        cant_horas = int(fila[4].strip())
                        impt_cobro = int(fila[5].strip())
                        c = Correctivo(fecha, nombre, importe, cant_horas, impt_cobro)
                        lista_mantenimientos.append(c)


                except (IndexError, ValueError) as e:
                    print(f"Error en la linea {numero_linea}: Registro invalido {e}")

    except FileNotFoundError:
        print(f"Error: el archivo {ruta_archivo} no existe")
    except PermissionError:
        print(f"Error: No se tienen permisos para leer {ruta_archivo}")
    except Exception as e:
        print(f"Error inesperado al abrir el archivo: {e}")

    return lista_mantenimientos
                    
