# El service técnico

## Consigna (tipo parcial)

Un service técnico de electrodomésticos registra las reparaciones que realiza a sus clientes.

De cada reparación se conoce un código numérico, el nombre del cliente, el equipo reparado y un costo base fijado según el tipo de falla. El costo definitivo de la reparación se calcula a partir del costo base y de las particularidades de cada tipo de servicio.

- En las reparaciones **a domicilio**, al costo base se le adicionan $500 por cada kilómetro recorrido para llegar hasta el domicilio del cliente.
- En las reparaciones **en taller**, al costo base se le adiciona $300 por cada día que el equipo permanece en el taller en concepto de guarda.

Se necesita un programa que lea del archivo `reparaciones.csv` la lista de todas las reparaciones y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma facturado**: informe el total a cobrar en concepto de todas las reparaciones registradas.
2. **Cantidad de reparaciones premium**: informe la cantidad de reparaciones a domicilio que hayan recorrido más de 20 kilómetros y cuyo costo base sea mayor a $50.000.
3. **Cliente de la reparación más barata**: informe el nombre del cliente de la reparación en taller cuyo costo definitivo sea el más bajo.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `reparaciones.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por reparación):

1. Tipo de reparación: 1 para a domicilio y 2 para en taller
2. Código: número sin repetición que identifica cada reparación
3. Cliente: nombre del cliente
4. Equipo: nombre o tipo de equipo reparado
5. Costo base: número de tipo float
6. Si es una reparación a domicilio, la cantidad de kilómetros recorridos (número entero); si es una reparación en taller, la cantidad de días de estadía (número entero)

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Reparacion(codigo, cliente, equipo, costo_base)` — clase base con atributos homónimos y métodos `costo_total()` y `tipo()`.
- `ADomicilio(codigo, cliente, equipo, costo_base, kilometros)` — suma $500 por cada kilómetro recorrido; `tipo()` = 1.
- `EnTaller(codigo, cliente, equipo, costo_base, dias_estadia)` — suma $300 por cada día de estadía; `tipo()` = 2.
- `ServicioTecnico()` — contiene la colección de reparaciones y ofrece:
  - `agregar(reparacion)`
  - `suma_facturado()`
  - `cantidad_reparaciones_premium()` — considera únicamente reparaciones a domicilio.
  - `cliente_reparacion_mas_barata()` — considera únicamente reparaciones en taller; si no hay ninguna, devuelve `None`.

## Archivos

- `reparaciones.csv` — datos del parcial.
- `test_service.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (paquete `entities` con `Reparacion.py`, `ADomicilio.py`, `EnTaller.py`, `ServicioTecnico.py`) junto a `test_service.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 14 pruebas en verde.
