from models.AgenciaViajes import AgenciaViajes
from models.PaqueteViaje import PaqueteViaje
from functions.lectorPaquetesCSV import lector_csv as lectorPaquete

def main():

    print(" --- Se ingreso al sistema de gestion de paquetes turisticos --- ")
    print()

    agencia = AgenciaViajes()
    paquetes = lectorPaquete("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/agencia/data/paquetes.csv")

    for paquete in paquetes:
        agencia.agregar_paquete(paquete)

    print(" - Segun los paquetes en la base de datos, se tiene la siguiente informacion: - ")
    print()
    print(f" (1) Informe del total a cobrar por los pquetes vendidos: {agencia.total_recaudado()}")
    print()
    print(f" (2) Cantidad de paquetes grupales vendidos (cantidad de pesonas > 4 y total a cobrar > $100.000): {agencia.cantidad_paquetes_grupales()}")
    print()
    print(f" (3) Nombre del cliente que compro el paquete internacional mas caro: {agencia.cliente_paquete_mas_caro()}")
    print()
    print(" --- Finalizado ---")

if __name__ == "__main__":
    main()