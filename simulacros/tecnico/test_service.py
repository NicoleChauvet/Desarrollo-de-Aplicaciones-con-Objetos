import pytest

from models.ADomicilio import ADomicilio
from models.EnTaller import EnTaller
from models.ServicioTecnico import ServicioTecnico


@pytest.fixture()
def service():
    s = ServicioTecnico()
    s.agregar(ADomicilio(1, "ANA", "Heladera", 60000, 10))
    s.agregar(ADomicilio(2, "BETO", "Aire Acondicionado", 55000, 25))
    s.agregar(EnTaller(3, "CARI", "Televisor", 40000, 5))
    s.agregar(EnTaller(4, "DIEGO", "Notebook", 30000, 2))
    return s


def test_costo_total_adomicilio_suma_kilometros():
    reparacion = ADomicilio(1, "ANA", "Heladera", 60000, 10)
    # 60000 + 10 * 500
    assert reparacion.costo_total() == 65000


def test_costo_total_entaller_suma_dias_estadia():
    reparacion = EnTaller(3, "CARI", "Televisor", 40000, 5)
    # 40000 + 5 * 300
    assert reparacion.costo_total() == 41500


def test_tipo_adomicilio_es_1():
    assert ADomicilio(1, "ANA", "Heladera", 60000, 10).tipo() == 1


def test_tipo_entaller_es_2():
    assert EnTaller(3, "CARI", "Televisor", 40000, 5).tipo() == 2


def test_service_comienza_vacio():
    s = ServicioTecnico()
    assert s.suma_facturado() == 0
    assert s.cantidad_reparaciones_premium() == 0
    assert s.cliente_reparacion_mas_barata() is None


def test_agregar_reparaciones(service):
    assert len(service.reparaciones) == 4


def test_suma_facturado(service):
    # 65000 + 67500 + 41500 + 30600
    assert service.suma_facturado() == 204600


def test_cantidad_reparaciones_premium(service):
    # solo BETO: más de 20 km y costo base mayor a 50000
    assert service.cantidad_reparaciones_premium() == 1


def test_premium_no_cuenta_pocos_kilometros():
    s = ServicioTecnico()
    s.agregar(ADomicilio(1, "X", "Y", 60000, 20))
    assert s.cantidad_reparaciones_premium() == 0


def test_premium_no_cuenta_costo_base_bajo():
    s = ServicioTecnico()
    s.agregar(ADomicilio(1, "X", "Y", 50000, 25))
    assert s.cantidad_reparaciones_premium() == 0


def test_premium_no_cuenta_reparaciones_en_taller():
    s = ServicioTecnico()
    s.agregar(EnTaller(1, "X", "Y", 90000, 50))
    assert s.cantidad_reparaciones_premium() == 0


def test_cliente_reparacion_mas_barata(service):
    # el taller de DIEGO (30600) es el más barato
    assert service.cliente_reparacion_mas_barata() == "DIEGO"


def test_mas_barata_considera_solo_en_taller():
    s = ServicioTecnico()
    s.agregar(ADomicilio(1, "BARATO", "Y", 1000, 1))
    s.agregar(EnTaller(2, "CARO", "Z", 90000, 10))
    assert s.cliente_reparacion_mas_barata() == "CARO"


def test_mas_barata_sin_reparaciones_en_taller():
    s = ServicioTecnico()
    s.agregar(ADomicilio(1, "X", "Y", 1000, 1))
    assert s.cliente_reparacion_mas_barata() is None
