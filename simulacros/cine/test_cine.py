import pytest

from entities.Cine import Cine
from entities.Sala2D import Sala2D
from entities.Sala3D import Sala3D
from entities.SalaVIP import SalaVIP


@pytest.fixture()
def cine():
    c = Cine()
    c.agregar_sala(Sala2D(1, 100, 5000, False))
    c.agregar_sala(Sala2D(2, 100, 3500, False))
    c.agregar_sala(Sala2D(3, 100, 6000, True))
    c.agregar_sala(Sala2D(4, 100, 5000, True))
    c.agregar_sala(Sala3D(5, 100, 5000, 2000))
    c.agregar_sala(Sala3D(6, 100, 5000, 500))
    c.agregar_sala(SalaVIP(7, 100, 12000, 2000))
    c.agregar_sala(SalaVIP(8, 100, 10000, 2000))
    return c


def test_resultado_neto_2d_es_la_recaudacion():
    sala = Sala2D(1, 100, 5000, False)
    assert sala.resultado_neto() == 5000


def test_resultado_neto_3d_suma_adicional_lentes():
    sala = Sala3D(5, 100, 5000, 2000)
    # recaudacion + adicional_lentes
    assert sala.resultado_neto() == 7000


def test_resultado_neto_vip_resta_costo_servicio():
    sala = SalaVIP(7, 100, 12000, 2000)
    # recaudacion - costo_servicio
    assert sala.resultado_neto() == 10000


def test_2d_estandar_rentable_solo_si_indice_mayor_40():
    assert Sala2D(1, 100, 5000, False).es_rentable() is True   # 50
    assert Sala2D(2, 100, 4000, False).es_rentable() is False  # 40


def test_2d_premium_rentable_solo_si_indice_mayor_55():
    assert Sala2D(3, 100, 6000, True).es_rentable() is True    # 60
    assert Sala2D(4, 100, 5500, True).es_rentable() is False   # 55


def test_3d_rentable_solo_si_indice_mayor_60():
    assert Sala3D(1, 100, 5000, 2000).es_rentable() is True    # 70
    assert Sala3D(2, 100, 5000, 1000).es_rentable() is False   # 60


def test_vip_rentable_solo_si_indice_mayor_90():
    assert SalaVIP(1, 100, 12000, 2000).es_rentable() is True   # 100
    assert SalaVIP(2, 100, 11000, 2000).es_rentable() is False  # 90


def test_cine_comienza_vacio():
    c = Cine()
    assert c.recaudacion_total() == 0
    assert c.cantidad_no_rentables() == 0
    assert c.sala_mas_rentable() is None


def test_agregar_salas(cine):
    assert len(cine.salas) == 8


def test_recaudacion_total(cine):
    # 5000 + 3500 + 6000 + 5000 + 7000 + 5500 + 10000 + 8000
    assert cine.recaudacion_total() == 50000


def test_cantidad_no_rentables(cine):
    # no rentables: sala 2 (40), sala 4 (50), sala 6 (55) y sala 8 (80)
    assert cine.cantidad_no_rentables() == 4


def test_sala_mas_rentable(cine):
    sala = cine.sala_mas_rentable()
    assert sala.numero == 7
    assert sala.tipo() == 3
    assert str(sala) == "7 3"


def test_sala_mas_rentable_con_una_sola_sala():
    c = Cine()
    c.agregar_sala(SalaVIP(20, 100, 15000, 1000))
    sala = c.sala_mas_rentable()
    assert sala.numero == 20
    assert sala.tipo() == 3
