from entities.Maquina import Maquina
from functions.lectorCSV import leer_csv

# parametros iniciales
m = Maquina()

lista_mantenimientos = leer_csv("C:/Users/Usuario/Desktop/Nicole/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/mantenimiento/data/mantenimientos.csv")

for mantenimiento in lista_mantenimientos:
    m.agregar_mantenimiento(mantenimiento)


# Printeo de los parametros pedidos
print(f"Segun los mantenimientos realizados a la maquina, se obtubieron los siguientes resultados: ")

fecha, nombre = m.rotura_larga()
print(f"Total abonado por todo concepto de los mantenimientos registrados: {m.suma_gastos()}")
print(f"Total de mantenimientos que hayan tenido un gasto total de mas de $10000: {m.mantenimientos_caros()}")
print(f"El mantenimiento correctivo de mayor duracion se realizo la fecha {fecha} con el operario {nombre}")