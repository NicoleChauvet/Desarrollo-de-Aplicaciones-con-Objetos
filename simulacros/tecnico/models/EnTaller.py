from models.Reparacion import Reparacion

class EnTaller(Reparacion):

    def __init__(self, codigo, cliente, equipo, costo_base, dias_estadia):
        super().__init__(codigo, cliente, equipo, costo_base)
        self.dias_estadia = dias_estadia

    def costo_total(self):
        return super().costo_total() + (300*self.dias_estadia)

    def tipo(self):
        return 2