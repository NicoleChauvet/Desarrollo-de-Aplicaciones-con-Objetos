from entities.Empresa import Empresa
from functions.lectorSucursalCSV import lector_csv as lectorSucursal
from entities.Sucursal import Sucursal

def main():

    print(f" --- Se accedio al sistema de gestion de sucursales --- ")
    print()

    empresa = Empresa()

    sucursales = lectorSucursal("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/supermercado/data/sucursales.csv")

    for sucursal in sucursales:
        empresa.agregar_sucursal(sucursal)

    print(f" (-) Se mostrara la informacion de las sucursales de la empresa: ")
    print()

    print(f" (1) Total de los resultados comerciales de todas las sucursales: {empresa.suma_ganancia()}")
    print()
    print(f" (2) Cantidad de sucursales cuyo indice de rentabilidad sea el menor al exigido: {empresa.cantidad_no_rentables()}")
    print()
    print(f" (3) Numero y tipo de la surcursal cuyo indice de rentabilidad es el mayor de todos: {empresa.local_mas_rentable().obtener_numero_tipo()}")
    print()

    print(f" -- Finalizacion -- ")

if __name__ == "__main__":
    main()    