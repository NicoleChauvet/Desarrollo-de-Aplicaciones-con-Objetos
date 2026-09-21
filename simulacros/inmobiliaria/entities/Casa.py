from entities.Inmueble import Inmueble

class Casa(Inmueble):
    def __init__(self, codigo, propietario, superficie, alquiler_base, dormitorios, pileta):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.dormitorios = dormitorios
        self.pileta = pileta

    def alquiler(self):
        importe_pileta = 100000 if self.pileta else 0
        return self.alquiler_base + self.dormitorios*30000 + importe_pileta

    def es_casa(self):
        return True

    def es_casa_premium(self):
        return (self.superficie > 150 and self.dormitorios > 2 and self.pileta)

    def __str__(self):
        return super().__str__() + f" | Cantidad de habitaciones: {self.dormitorios} | Tiene pileta: {self.pileta}"