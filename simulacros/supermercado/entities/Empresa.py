from entities.Sucursal import Sucursal

class Empresa:

    def __init__(self):
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def suma_ganancia(self):
        sumador = 0
        for sucursal in self.sucursales:
            sumador += sucursal.resultado_comercial()

        return sumador

    def cantidad_no_rentables(self):
        contador = 0
        for sucursal in self.sucursales:
            if not sucursal.es_rentable():
                contador += 1

        return contador

    def local_mas_rentable(self):
        if not self.sucursales:
            return None
        ganador = self.sucursales[0]
        for sucursal in self.sucursales:
            if ganador.numero_rentabilidad() < sucursal.numero_rentabilidad():
                ganador = sucursal

        return ganador
