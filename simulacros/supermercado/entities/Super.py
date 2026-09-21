from entities.Sucursal import Sucursal

class Super(Sucursal):

    def __init__(self, numero, superficie, facturacion, mayorista):
        super().__init__(numero, superficie, facturacion)
        self.mayorista = mayorista

    def resultado_comercial(self):
        return self.facturacion

    def es_rentable(self):
        if self.superficie != 0:
            if self.mayorista:
                return (self.resultado_comercial()/self.superficie) > 45
            else:
                return (self.resultado_comercial()/self.superficie) > 40

        return False

    def tipo(self):
        return 2

    def numero_rentabilidad(self):
        return self.resultado_comercial()/self.superficie

    def __str__(self):
        return super().__str__() + f" {self.tipo()}"
        
