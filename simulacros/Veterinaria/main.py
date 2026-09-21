from entities.Veterinaria import Veterinaria
from entities.Atencion import Atencion
from functions.lectorAtencionesCSV import lector_csv as lectorAtenciones

def main():

    print(" --- Se accedio al programa de gestion de Veterinaria --- ")
    print()

    veterinaria = Veterinaria()

    lista_atenciones = lectorAtenciones("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/Veterinaria/data/atenciones.csv")

    for atencion in lista_atenciones:
        veterinaria.agregar_atencion(atencion)

    print(" (-) Los datos de las atenciones de este mes son los sigueintes: ")
    print()
    print(f" (1) Total cobrado por todas las atenciones registradas: {veterinaria.suma_facturado()}")
    print()
    print(f" (2) Cantidad de atenciones cuyo total sea mas de $15.000: {veterinaria.atenciones_costosas()}")
    print()
    print(f" (3) Fecha y nombre del veterinario de la cirgua que mas horas de quirofano consumio: {str(veterinaria.cirugia_mas_larga())}")
    print()

    print(" --- Finalizado ---")

if __name__ == "__main__":
    main()
