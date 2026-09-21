from entities.Sucursal import Sucursal

class Hiper(Sucursal):

    def __init__(self, numero, superficie, facturacion, alquileres):
        super().__init__(numero, superficie, facturacion)
        self.alquileres = alquileres

    def resultado_comercial(self):
        return self.facturacion + self.alquileres

    def es_rentable(self):
        return ((self.resultado_comercial()/self.superficie) > 50)

    def tipo(self):
        return 1

    def numero_rentabilidad(self):
        return self.resultado_comercial()/self.superficie

    def __str__(self):
        return super().__str__() + f" {self.tipo()}"