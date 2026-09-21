from entities.Inmueble import Inmueble

class Departamento(Inmueble):

    def __init__(self, codigo, propietario, superficie, alquiler_base, expensas, piso):
        super().__init__(codigo, propietario, superficie, alquiler_base)
        self.expensas = expensas
        self.piso = piso

    def alquiler(self):
        importe_piso_inferior = 20000 if self.piso < 3 else 0
        return self.alquiler_base + importe_piso_inferior + self.expensas

    def es_casa(self):
        return super().es_casa()

    def __str__(self):
        return super().__str__() + f" | Importe expensas: {self.expensas} | Nro de piso: {self.piso}"