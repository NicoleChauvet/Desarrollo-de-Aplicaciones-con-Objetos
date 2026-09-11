# 1. ejercicios basicos sobre esta unidad:

# Dada la lista numeros = [4, 7, 2, 9, 3, 6, 1, 8], creá por comprensión una lista llamada dobles que contenga cada número multiplicado por 2.ç

numeros = [4, 7, 2, 9, 3, 6, 1, 8]

dobles = [nro*2 for nro in numeros]

print(dobles)

# Con la misma lista numeros, creá por comprensión una lista mayores_a_5 que contenga solo los números mayores a 5 (sin transformarlos, solo filtrarlos).

mayores_a_5 = [nro for nro in numeros if nro > 5]

print(mayores_a_5)

# Dada palabras = ["sol", "luna", "estrella", "cielo", "mar"], creá por comprensión una lista largas con solo las palabras que tengan más de 3 letras.

palabras = ["sol", "luna", "estrella", "cielo", "mar"]

lista_larga = [pal for pal in palabras if len(pal) > 3]

print(lista_larga)


# 2. ejercicios con lambdas

# Con numeros = [4, 7, 2, 9, 3, 6, 1, 8], creá por comprensión una lista cuadrados_pares que contenga el cuadrado de cada número, pero solo de los que son pares.

cuadrados_pares = [nro**2 for nro in numeros if nro % 2 == 0]

print(cuadrados_pares)

# Con palabras = ["sol", "luna", "estrella", "cielo", "mar"], creá por comprensión un diccionario longitudes donde cada clave sea la palabra y el valor sea su longitud.

dic = {pal:len(pal) for pal in palabras}

print(dic)

# Dada temperaturas = [18, 22, 15, 30, 12, 25, 19], creá por comprensión una lista clasificacion que contenga el string "Calor" si la temperatura es mayor a 20, 
# o "Frío" en caso contrario (para cada temperatura de la lista, usando el operador ternario dentro de la comprensión).

temperaturas = [18, 22, 15, 30, 12, 25, 19]

clasificacion = ["Calor" if temp > 20  else "Frio" for temp in temperaturas]

print(clasificacion)

# 3. funciones lambdas

# Creá una lambda llamada es_par que reciba un número y devuelva True si es par, False si no.

es_par = lambda num: num % 2 == 0

print(es_par(5))

# Creá una lambda llamada mayor que reciba dos números a y b, y devuelva el mayor de los dos (usando el operador ternario).

mayor = lambda a,b: a if a > b else b

print(mayor(6,4))

# Creá una lambda llamada iniciales que reciba un string y devuelva solo su primera letra en mayúscula.

iniciales = lambda pal: pal[0].upper()

print(iniciales("zanahoria"))

# 4. map

# Dada numeros = [3, 8, 1, 6, 9, 4], usá map() con una lambda para crear una lista cubos con el cubo de cada número.

numeros = [3, 8, 1, 6, 9, 4]

cubos = list(map(lambda x: x**3, numeros))

print(cubos)

# Dada nombres = ["ana", "pedro", "lucia", "juan"], usá map() con una lambda para crear una lista capitalizados 
# donde cada nombre empiece con mayúscula (usá el método .capitalize() dentro de la lambda).

nombres = ["ana", "pedro", "lucia", "juan"]

capitalizados = list(map(lambda x: x.capitalize(), nombres))

print(capitalizados)

# Dadas dos listas precios = [100, 250, 80, 300] y descuentos = [10, 20, 5, 15] (porcentajes), 
# usá map() con una lambda de dos parámetros para calcular el precio final de cada producto después de aplicar su descuento correspondiente.

precios = [100, 250, 80, 300]
descuentos = [10, 20, 5, 15]

precio_final = list(map(lambda x,y: x-x*(y/100), precios, descuentos))

print(precio_final)

# 5. filter

# Dada edades = [15, 22, 8, 34, 17, 45, 12, 19], usá filter() con una lambda para obtener una lista mayores_edad con las edades que sean 18 o más.

edades = [15, 22, 8, 34, 17, 45, 12, 19]

mayores_edad = list(filter(lambda x: x >= 18, edades))

print(mayores_edad)

# Dada palabras = ["auto", "sol", "computadora", "flor", "murciélago", "pan"], usá filter() con una lambda para obtener las palabras que tengan 6 o menos caracteres.

palabras = ["auto", "sol", "computadora", "flor", "murciélago", "pan"]

pal_car = list(filter(lambda x: len(x) <= 6, palabras))

print(pal_car)

# Dada numeros = [-5, 3, -2, 8, 0, -9, 4, -1], combiná filter() para quedarte solo con los negativos, y después map() sobre ese resultado para obtener sus valores absolutos.

numeros = [-5, 3, -2, 8, 0, -9, 4, -1]

neg = list(filter(lambda x: x < 0, numeros))
val_abs = list(map(lambda x: abs(x), neg))

print(val_abs)