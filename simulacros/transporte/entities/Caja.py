from entities.Carga import Carga

class Caja(Carga):
    def __init__(self, contenido, peso_kg):
        super().__init__(contenido)
        self.peso_kg = peso_kg

    def peso(self):
        return self.peso_kg

    def __str__(self):
        return super().__str__() + f" | Peso en kg: {self.peso_kg}"