import random

# parametros iniciales
temperaturas = []

tmp_cero = 0
sumatoria = 0
tmp_may_20 = 0
tmp_may_40 = "no"
may_tmp = 0
tmp_men_prom = 0

for i in range(50):
    temperatura = random.randint(-20,49)

    if temperatura < 0:
        tmp_cero += 1

    if temperatura > 20:
        tmp_may_20 += 1
        if temperatura > may_tmp:
            may_tmp = temperatura

    if temperatura > 40:
        tmp_may_40 = "si"

    sumatoria += temperatura
    temperaturas.append(temperatura)




