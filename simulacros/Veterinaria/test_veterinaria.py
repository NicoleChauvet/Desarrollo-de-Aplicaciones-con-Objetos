import pytest

from entities.Consulta import Consulta
from entities.Cirugia import Cirugia
from entities.Veterinaria import Veterinaria


@pytest.fixture()
def veterinaria():
    v = Veterinaria()
    v.agregar_atencion(Consulta("01/03/2026", "Perez", "Rex", 5000, 2))
    v.agregar_atencion(Consulta("02/03/2026", "Gomez", "Milo", 6000, 0))
    v.agregar_atencion(Cirugia("03/03/2026", "Diaz", "Toby", 10000, 2))
    v.agregar_atencion(Cirugia("04/03/2026", "Diaz", "Nina", 8000, 3))
    v.agregar_atencion(Cirugia("05/03/2026", "Ruiz", "Kiki", 5000, 1))
    v.agregar_atencion(Consulta("06/03/2026", "Perez", "Luna", 4000, 3))
    return v


def test_costo_total_consulta_suma_vacunas():
    consulta = Consulta("01/03/2026", "Perez", "Rex", 5000, 2)
    # 5000 + 2 * 1500
    assert consulta.costo_total() == 8000


def test_costo_total_consulta_sin_vacunas():
    consulta = Consulta("02/03/2026", "Gomez", "Milo", 6000, 0)
    assert consulta.costo_total() == 6000


def test_costo_total_cirugia_suma_horas_quirofano():
    cirugia = Cirugia("03/03/2026", "Diaz", "Toby", 10000, 2)
    # 10000 + 2 * 5000
    assert cirugia.costo_total() == 20000


def test_tipo_consulta_es_1():
    assert Consulta("01/03/2026", "Perez", "Rex", 5000, 2).tipo() == 1


def test_tipo_cirugia_es_2():
    assert Cirugia("03/03/2026", "Diaz", "Toby", 10000, 2).tipo() == 2


def test_veterinaria_comienza_vacia():
    v = Veterinaria()
    assert v.suma_facturado() == 0
    assert v.atenciones_costosas() == 0
    assert v.cirugia_mas_larga() is None


def test_agregar_atenciones(veterinaria):
    assert len(veterinaria.atenciones) == 6


def test_suma_facturado(veterinaria):
    # 8000 + 6000 + 20000 + 23000 + 10000 + 8500
    assert veterinaria.suma_facturado() == 75500


def test_atencion_costosa_no_cuenta_igual_al_limite():
    v = Veterinaria()
    v.agregar_atencion(Cirugia("07/03/2026", "Ruiz", "Coco", 5000, 2))  # 15000
    assert v.atenciones_costosas() == 0


def test_atencion_costosa_cuenta_mayor_al_limite():
    v = Veterinaria()
    v.agregar_atencion(Cirugia("07/03/2026", "Ruiz", "Coco", 5000, 3))  # 20000
    assert v.atenciones_costosas() == 1


def test_atenciones_costosas(veterinaria):
    # costosas: cirugia del 03/03 (20000) y la del 04/03 (23000)
    assert veterinaria.atenciones_costosas() == 2


def test_cirugia_mas_larga(veterinaria):
    # la de mayor horas_quirofano es la del 04/03/2026 (3 horas)
    assert veterinaria.cirugia_mas_larga() == ("04/03/2026", "Diaz")


def test_cirugia_mas_larga_sin_cirugias():
    v = Veterinaria()
    v.agregar_atencion(Consulta("08/03/2026", "Gomez", "Fido", 4000, 1))
    assert v.cirugia_mas_larga() is None
