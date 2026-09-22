from models.Reparacion import Reparacion

class ADomicilio(Reparacion):

    def __init__(self, codigo, cliente, equipo, costo_base, kilometros):
        super().__init__(codigo, cliente, equipo, costo_base)
        self.kilometros = kilometros

    def costo_total(self):
        return super().costo_total() + (500*self.kilometros)

    def tipo(self):
        return 1

    def es_premium(self):
        return (self.kilometros > 20 and self.costo_base > 50000)