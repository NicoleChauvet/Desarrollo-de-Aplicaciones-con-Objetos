from entities.Hospital import Hospital
from functions.lectorFarmaciaCSV import leer_csv as lector_farmacia
from functions.lectorMedicasCSV import lector_csv as lector_medica
from functions.lectorPacientesCSV import lector_csv as lector_paciente


diccionario_pacientes = lector_paciente("C:/Users/Usuario/Desktop/Facultad/4to año/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/hospital/data/pacientes.csv")
lista_medicas = lector_medica("C:/Users/Usuario/Desktop/Facultad/4to año/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/hospital/data/atenciones_medicas.csv", diccionario_pacientes)
lista_farmacia = lector_farmacia("C:/Users/Usuario/Desktop/Facultad/4to año/DAO/Desarrollo-de-Aplicaciones-con-Objetos/simulacros/hospital/data/atenciones_farmacia.csv")

lista_atenciones = lista_medicas + lista_farmacia

print(f"Has accedido al sistema del hospital")

razon = int(input("Porfavor ingrese la razon social del hospital: "))

hospital1 = Hospital(razon)

print(f"A continuacion se anexaran las atenciones al hispital: ")
for atenciones in lista_atenciones:
    hospital1.addAtencion(atenciones)

print(f"Segun estas atenciones, la informacion recolectada es: ")

print(f" - El total de los importes de las consultas de las atenciones medicas es: {hospital1.impTotalAtCons()}")
print(f" - El promedio de los importes a cobrar de atenciones medicas cuyo importe se encuentre entre a y b: {hospital1.imptPromAt()}")
print(f" - El codigo de la primera atencion medica se un paciente habitual: {hospital1.codPrimAtHabt()}")

print(f"Gracias por usar el sistema")


