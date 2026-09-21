from entities.Cine import Cine
from entities.Sala import Sala

from functions.lectorSalasCSV import lector_csv as lectorCine

def main():

    print(" --- Se ingreso al sistema de gestion de salas del Cine --- ")
    print()

    cine = Cine()

    lista_salas = lectorCine("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/cine/data/salas.csv")

    for sala in lista_salas:
        cine.agregar_sala(sala)

    print(" (-) Se mostrara la informacion recaudada del mes de las diferentes salas: ")
    print()
    print(f" (2) Recaudacion total de las salas: {cine.recaudacion_total()}")
    print()
    print(f" (2) Cantidad de salas no rentables segun el indice de ocupacion exigido: {cine.cantidad_no_rentables()}")
    print()
    print(f" (3) La sala mas rentable del mes fue: {cine.sala_mas_rentable().conocer_numero_tipo()}")
    print()

    print(" --- Finalizado ---")

if __name__ == "__main__":
    main()