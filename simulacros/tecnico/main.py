from models.ServicioTecnico import ServicioTecnico
from models.Reparacion import Reparacion
from functions.lectorReparacionesCSV import lector_csv as lectorReparacion

def main():

    print(" --- Sistema de reparacion de electrodomesticos ---")
    print()

    servTec = ServicioTecnico()

    lista_reparaciones = lectorReparacion("C:/Users/Usuario/Desktop/Facultad/4to año/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/tecnico/data/reparaciones.csv")

    for reparacion in lista_reparaciones:
        servTec.agregar(reparacion)

    print(" - Se mostrara la informacion de las reparaciones cargadas en el sistema - ")
    print()
    print(f" (1) Informe total a cobrar: {servTec.suma_facturado()}")
    print()
    print(f" (2) Cantidad de reparaciones a domicilio que recorrieron mas de 20 km y su costo base es mayor a $50.000: {servTec.cantidad_reparaciones_premium()}")
    print()
    print(f" (3) Nombre del cliente de la reparacion del taller cuyo costo definitivo fue el mas bajo: {servTec.cliente_reparacion_mas_barata()}")
    print()

    print(" --- Finalizado ---")

if __name__ == "__main__":
    main()
