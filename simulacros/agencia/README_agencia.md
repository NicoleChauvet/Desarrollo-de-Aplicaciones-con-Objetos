# La agencia de viajes

## Consigna (tipo parcial)

Una agencia de viajes vende paquetes turísticos a sus clientes, agrupados en dos modalidades.

De cada paquete se conoce un código numérico, el nombre del cliente, la cantidad de personas que viajan y un precio base fijado por la agencia. El precio definitivo del paquete se calcula a partir del precio base y de las particularidades de cada modalidad.

- En los paquetes **nacionales**, si el paquete incluye traslados, al precio base se le adicionan $5.000 por cada persona que viaje. Si no incluye traslados, el precio definitivo es igual al precio base.
- En los paquetes **internacionales**, al precio base se le adiciona el importe del seguro de viajero multiplicado por la cantidad de personas, y además un impuesto fijo de $20.000 por paquete.

Se necesita un programa que lea del archivo `paquetes.csv` la lista de todos los paquetes y los almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Total recaudado**: informe el total a cobrar por todos los paquetes vendidos.
2. **Cantidad de paquetes grupales**: informe la cantidad de paquetes, de cualquier modalidad, vendidos a más de 4 personas y cuyo precio definitivo sea mayor a $100.000.
3. **Cliente del paquete internacional más caro**: informe el nombre del cliente del paquete internacional cuyo precio definitivo sea el más alto.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `paquetes.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por paquete):

1. Tipo de paquete: 1 para nacional y 2 para internacional
2. Código: número sin repetición que identifica cada paquete
3. Cliente: nombre del cliente
4. Cantidad de personas: número entero
5. Precio base: número de tipo float
6. Si es un paquete nacional, un 1 si incluye traslados y 0 si no; si es un paquete internacional, el importe del seguro de viajero por persona

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `PaqueteViaje(codigo, cliente, cantidad_personas, precio_base)` — clase base con atributos homónimos y métodos `precio_total()` y `tipo()`.
- `Nacional(codigo, cliente, cantidad_personas, precio_base, incluye_traslados)` — `incluye_traslados` booleano; suma $5.000 por persona solo si incluye traslados; `tipo()` = 1.
- `Internacional(codigo, cliente, cantidad_personas, precio_base, seguro_por_persona)` — suma el seguro por persona y un impuesto fijo de $20.000; `tipo()` = 2.
- `AgenciaViajes()` — contiene la colección de paquetes y ofrece:
  - `agregar_paquete(paquete)`
  - `total_recaudado()`
  - `cantidad_paquetes_grupales()` — considera paquetes de ambas modalidades.
  - `cliente_paquete_mas_caro()` — considera únicamente paquetes internacionales; si no hay ninguno, devuelve `None`.

## Archivos

- `paquetes.csv` — datos del parcial.
- `test_agencia.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (paquete `entities` con `PaqueteViaje.py`, `Nacional.py`, `Internacional.py`, `AgenciaViajes.py`) junto a `test_agencia.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 14 pruebas en verde.
