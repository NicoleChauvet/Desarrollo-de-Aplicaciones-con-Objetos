import pytest

from entities.Nacional import Nacional
from entities.Internacional import Internacional
from entities.AgenciaViajes import AgenciaViajes


@pytest.fixture()
def agencia():
    a = AgenciaViajes()
    a.agregar_paquete(Nacional(1, "ANA", 5, 80000, True))
    a.agregar_paquete(Nacional(2, "BETO", 3, 90000, True))
    a.agregar_paquete(Internacional(3, "CARI", 6, 150000, 3000))
    a.agregar_paquete(Internacional(4, "DIEGO", 2, 200000, 5000))
    a.agregar_paquete(Nacional(5, "ELENA", 4, 60000, False))
    a.agregar_paquete(Internacional(6, "FEDE", 8, 100000, 2000))
    return a


def test_precio_total_nacional_con_traslados():
    paquete = Nacional(1, "ANA", 5, 80000, True)
    # 80000 + 5 * 5000
    assert paquete.precio_total() == 105000


def test_precio_total_nacional_sin_traslados():
    paquete = Nacional(5, "ELENA", 4, 60000, False)
    assert paquete.precio_total() == 60000


def test_precio_total_internacional_suma_seguro_e_impuesto():
    paquete = Internacional(3, "CARI", 6, 150000, 3000)
    # 150000 + 6 * 3000 + 20000
    assert paquete.precio_total() == 188000


def test_tipo_nacional_es_1():
    assert Nacional(1, "ANA", 5, 80000, True).tipo() == 1


def test_tipo_internacional_es_2():
    assert Internacional(3, "CARI", 6, 150000, 3000).tipo() == 2


def test_agencia_comienza_vacia():
    a = AgenciaViajes()
    assert a.total_recaudado() == 0
    assert a.cantidad_paquetes_grupales() == 0
    assert a.cliente_paquete_mas_caro() is None


def test_agregar_paquetes(agencia):
    assert len(agencia.paquetes) == 6


def test_total_recaudado(agencia):
    # 105000 + 105000 + 188000 + 230000 + 60000 + 136000
    assert agencia.total_recaudado() == 824000


def test_grupal_no_cuenta_pocas_personas():
    a = AgenciaViajes()
    a.agregar_paquete(Nacional(1, "X", 4, 100000, True))
    assert a.cantidad_paquetes_grupales() == 0


def test_grupal_no_cuenta_precio_bajo():
    a = AgenciaViajes()
    a.agregar_paquete(Nacional(1, "X", 5, 50000, False))
    assert a.cantidad_paquetes_grupales() == 0


def test_cantidad_paquetes_grupales(agencia):
    # grupales: ANA (105000, 5 personas), CARI (188000, 6 personas) y FEDE (136000, 8 personas)
    assert agencia.cantidad_paquetes_grupales() == 3


def test_cliente_paquete_mas_caro(agencia):
    # el internacional de DIEGO (230000) es el mas caro
    assert agencia.cliente_paquete_mas_caro() == "DIEGO"


def test_mas_caro_considera_solo_internacional():
    a = AgenciaViajes()
    a.agregar_paquete(Nacional(1, "CARO_NACIONAL", 10, 999999, True))
    a.agregar_paquete(Internacional(2, "BARATO_INTL", 1, 10000, 1000))
    assert a.cliente_paquete_mas_caro() == "BARATO_INTL"


def test_mas_caro_sin_internacionales():
    a = AgenciaViajes()
    a.agregar_paquete(Nacional(1, "X", 5, 80000, True))
    assert a.cliente_paquete_mas_caro() is None
