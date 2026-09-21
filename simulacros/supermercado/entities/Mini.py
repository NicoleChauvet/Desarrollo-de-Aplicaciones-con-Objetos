from entities.Sucursal import Sucursal

class Mini(Sucursal):

    def __init__(self, numero, superficie, facturacion, alquiler):
        super().__init__(numero, superficie, facturacion)
        self.alquiler = alquiler

    def resultado_comercial(self):
        return self.facturacion - self.alquiler

    def es_rentable(self):
        return (self.resultado_comercial()/self.superficie) > 35

    def tipo(self):
        return 3

    def numero_rentabilidad(self):
        return self.resultado_comercial()/self.superficie

    def __str__(self):
        return super().__str__() + f" {self.tipo()}"