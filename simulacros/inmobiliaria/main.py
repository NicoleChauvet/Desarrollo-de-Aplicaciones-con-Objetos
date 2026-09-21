from entities.Inmobiliaria import Inmobiliaria
from entities.Inmueble import Inmueble
from functions.lectorInmueble import lector_csv

def main():

    # primero leemos el archivo
    lista_inmuebles = lector_csv("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/inmobiliaria/data/inmuebles.csv")

    inmobiliaria = Inmobiliaria()
    for inmueble in lista_inmuebles:
        inmobiliaria.agregar(inmueble)

    print(f" --- Se inicio el sistema de manejo de inmuebles en alquiler --- ")
    print()

    print(f" (-) Estos son actualemente los datos de los presentes inmuebles en alquiler (-) ")
    print()

    print(f" (1) Total a recaudar en concepto de alquileres: {inmobiliaria.suma_alquileres()}")
    print()
    print(f" (2) Cantidad de casas premium: {inmobiliaria.cantidad_casas_premium()}")
    print()
    print(f" (3) Propietario del alquiler mas bajo de departamento: {inmobiliaria.propietario_alquiler_mas_bajo()}")
    print()

    print(f" --- Fin del programa ---")

if __name__ == "__main__":
    main()
