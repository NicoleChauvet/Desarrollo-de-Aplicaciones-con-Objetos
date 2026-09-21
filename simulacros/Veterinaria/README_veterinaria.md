# La veterinaria

## Consigna (tipo parcial)

Una clínica veterinaria registra las atenciones que realiza a las mascotas que llegan al consultorio.

De cada atención se registra la fecha en que se realizó, el nombre del veterinario que la atendió, el nombre de la mascota y un costo base fijado por la clínica.

Existen dos tipos de atención. Por un lado, las **consultas**, en las que además del costo base puede aplicarse una cierta cantidad de vacunas, cada una con un costo adicional de $1.500. Por otro lado, las **cirugías**, que requieren el uso del quirófano por una cantidad de horas, cada una con un costo adicional de $5.000.

Se necesita un programa que lea del archivo `atenciones.csv` la lista de todas las atenciones y las almacene en algún objeto (no en la función principal) que ofrezca los siguientes métodos:

1. **Suma facturado**: total cobrado por todo concepto en todas las atenciones registradas.
2. **Cantidad de atenciones costosas**: cantidad de atenciones de cualquier tipo cuyo costo total haya sido de más de $15.000.
3. **Cirugía más larga**: fecha y nombre del veterinario de la cirugía que más horas de quirófano haya insumido.

La función principal debe ingresar los datos desde el archivo de texto y finalizar luego de imprimir el resultado de la ejecución de los tres métodos anteriores.

### Estructura del archivo `atenciones.csv`

El archivo posee la siguiente estructura (sin línea de títulos, una línea por atención):

1. Tipo de atención: 1 para consulta y 2 para cirugía
2. Fecha: una cadena
3. Veterinario: nombre del veterinario que realizó la atención
4. Mascota: nombre de la mascota atendida
5. Costo base: número de tipo float
6. Si es una consulta, la cantidad de vacunas aplicadas (número entero); si es una cirugía, la cantidad de horas de uso del quirófano (número float)

### Contrato esperado (para los tests)

Las clases deben llamarse y comportarse de la siguiente manera para que pasen las pruebas:

- `Atencion(fecha, veterinario, mascota, costo_base)` — clase base con atributos homónimos y métodos `costo_total()` y `tipo()`.
- `Consulta(fecha, veterinario, mascota, costo_base, cantidad_vacunas)` — suma $1.500 por cada vacuna aplicada; `tipo()` = 1.
- `Cirugia(fecha, veterinario, mascota, costo_base, horas_quirofano)` — suma $5.000 por cada hora de quirófano; `tipo()` = 2.
- `Veterinaria()` — contiene la colección de atenciones y ofrece:
  - `agregar_atencion(atencion)`
  - `suma_facturado()`
  - `atenciones_costosas()`
  - `cirugia_mas_larga()` — debe considerar únicamente las atenciones de tipo cirugía; si no hay ninguna, devuelve `None`.

## Archivos

- `atenciones.csv` — datos del parcial.
- `test_veterinaria.py` — casos de prueba (pytest) entregados junto a la consigna.

## Cómo correr las pruebas

Con pytest instalado, desde una carpeta que contenga los módulos de la solución (paquete `entities` con `Atencion.py`, `Consulta.py`, `Cirugia.py`, `Veterinaria.py`) junto a `test_veterinaria.py`:

```
python -m pytest
python -m pytest -v
```

Salida esperada: 13 pruebas en verde.
