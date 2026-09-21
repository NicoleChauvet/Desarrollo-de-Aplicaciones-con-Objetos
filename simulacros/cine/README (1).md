# El cine

## Consigna (tipo parcial)

Una cadena de cines posee varias salas distribuidas en sus complejos, agrupadas en tres formatos diferentes.

- **Salas 2D**: salas convencionales. Algunas incorporan butacas reclinables (formato "premium"), lo que exige un mayor rendimiento para considerarse rentables.
- **Salas 3D**: además de la venta de entradas, cobran un adicional por el alquiler de los anteojos 3D.
- **Salas VIP**: incluyen un servicio de confitería (bebidas y snacks) dentro del precio de la entrada, cuyo costo debe descontarse de lo recaudado.

De cada sala el cine registra la capacidad en butacas y el total recaudado en el último mes por venta de entradas. Adicionalmente existen dos cálculos relevantes: el **resultado neto** y el **índice de ocupación rentable**.

- El resultado neto de una sala 2D es equivalente a la recaudación por entradas. En las salas 3D se suma el adicional cobrado por el alquiler de anteojos; en las salas VIP se resta el costo del servicio de confitería incluido.
- El índice de ocupación rentable es el cociente entre el resultado neto y la capacidad (butacas). Una sala 2D estándar es rentable si su índice es mayor a 40, pero si es premium (butacas reclinables) debe ser mayor a 55. Una sala 3D es rentable si su índice es mayor a 60. Una sala VIP es rentable si su índice es mayor a 90.

Se necesita un programa que lea del archivo `salas.csv` la lista de todas las salas y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Recaudación total**: total del resultado neto de todas las salas.
2. **Cantidad de salas no rentables**: cantidad de salas cuyo índice de ocupación rentable sea menor o igual al exigido para su tipo.
3. **Sala más rentable**: número y tipo de la sala cuyo índice de ocupación rentable sea el mayor de todas.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `salas.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por sala):

1. Tipo de sala: 1 para 2D, 2 para 3D y 3 para VIP
2. Número: número sin repetición que identifica cada sala
3. Capacidad: número de tipo entero con la cantidad de butacas
4. Recaudación: número de tipo float con la recaudación por entradas del último mes, expresada en miles de pesos
5. Si es una sala 2D, un 1 si tiene butacas premium/reclinables y 0 si no; si es una sala 3D, el importe cobrado por el alquiler de anteojos; si es una sala VIP, el importe abonado por el servicio de confitería incluido

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Sala(numero, capacidad, recaudacion)` — clase base con atributos homónimos y métodos `resultado_neto()`, `es_rentable()` y `tipo()`.
- `Sala2D(numero, capacidad, recaudacion, premium)` — `premium` booleano; el resultado es la recaudación; rentable si índice > 40 (estándar) o > 55 (premium); `tipo()` = 1.
- `Sala3D(numero, capacidad, recaudacion, adicional_lentes)` — suma el adicional de lentes al resultado; rentable si índice > 60; `tipo()` = 2.
- `SalaVIP(numero, capacidad, recaudacion, costo_servicio)` — resta el costo del servicio al resultado; rentable si índice > 90; `tipo()` = 3.
- `Cine()` — contiene la colección de salas y ofrece:
  - `agregar_sala(sala)`
  - `recaudacion_total()`
  - `cantidad_no_rentables()`
  - `sala_mas_rentable()`

Nota: `str(sala)` debe devolver `"<numero> <tipo>"` (por ejemplo `"7 3"`), tal como se verifica en los tests.

## Archivos

- `salas.csv` — datos del parcial.
- `test_cine.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (paquete `entities` con `Sala.py`, `Sala2D.py`, `Sala3D.py`, `SalaVIP.py`, `Cine.py`) junto a `test_cine.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 13 pruebas en verde.
