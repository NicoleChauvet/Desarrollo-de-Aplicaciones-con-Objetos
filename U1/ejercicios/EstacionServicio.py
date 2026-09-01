# parametros iniciales
surtidores = []

total_litros = [0, 0, 0]  # gasolina, diesel, etanol
surtidor_menor_vendido= 0
cantidad_menor = 0
sumador = 0



# funciones validadoras
def validar_numero_surtidor(numero):
    while not 1 <= numero <= 30:
        print("Número de surtidor inválido. Debe estar entre 1 y 30.")
        numero = int(input("Ingrese el número de surtidor: "))
    return numero

def validador_numero_positivo(numero):
    while numero < 0:
        print("Número inválido. Debe ser un número positivo.")
        numero = int(input("Ingrese un número positivo: "))
    return numero

def validador_tipo_combustible(tipo):
    while tipo not in [1,2,3]:
        print("Tipo de combustible inválido. Debe ser 1-'gasolina', 2-'diesel' o 3-'etanol'.")
        tipo = int(input("Ingrese el tipo de combustible (1: gasolina, 2: diesel, 3: etanol): "))
    return tipo

for i in range(10):
    numero = int(input("Ingrese el número de surtidor: "))
    validar_numero_surtidor(numero)

    cantidad = int(input("Ingrese la cantidad de litros de combustible: "))
    validador_numero_positivo(cantidad)

    tipo = int(input("Ingrese el tipo de combustible (1: gasolina, 2: diesel, 3: etanol): "))
    validador_tipo_combustible(tipo)

    if tipo == 1:
        total_litros[0] += cantidad
    elif tipo == 2:
        total_litros[1] += cantidad
    else:
        total_litros[2] += cantidad

    if cantidad < cantidad_menor or cantidad_menor == 0:
        surtidor_menor_vendido = numero
        cantidad_menor = cantidad

    sumador += cantidad

    print(f"Registro {i+1}: Surtidor {numero}, Cantidad: {cantidad} litros, Tipo: {tipo}")
    surtidor = [numero, cantidad, tipo]
    surtidores.append(surtidor)

promedio = sumador / 10
# resultados
print("Total de litros vendidos por tipo de combustible:")
print(f"Gasolina: {total_litros[0]} litros")
print(f"Diesel: {total_litros[1]} litros")
print(f"Etanol: {total_litros[2]} litros")
print(f"Surtidor con menor cantidad vendida: {surtidor_menor_vendido}")
print(f"Cantidad total de litros vendidos: {promedio} litros")