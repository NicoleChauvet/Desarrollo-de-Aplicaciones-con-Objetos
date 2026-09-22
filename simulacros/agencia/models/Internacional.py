from models.PaqueteViaje import PaqueteViaje

class Internacional(PaqueteViaje):

    def __init__(self, codigo, cliente, cantidad_personas, precio_base, seguro_por_persona):
        super().__init__(codigo, cliente, cantidad_personas, precio_base)
        self.seguro_por_persona = seguro_por_persona

    def precio_total(self):
        return super().precio_total() + (self.seguro_por_persona*self.cantidad_personas) + 20000

    def tipo(self):
        return 2