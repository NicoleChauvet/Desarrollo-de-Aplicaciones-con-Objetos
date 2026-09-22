from models.PaqueteViaje import PaqueteViaje

class Nacional(PaqueteViaje):

    def __init__(self, codigo, cliente, cantidad_personas, precio_base, incluye_traslados):
        super().__init__(codigo, cliente, cantidad_personas, precio_base)
        self.incluye_traslados = incluye_traslados

    def precio_total(self):
        if self.incluye_traslados:
            return super().precio_total() + (self.cantidad_personas*5000)
        return super().precio_total()

    def tipo(self):
        return 1