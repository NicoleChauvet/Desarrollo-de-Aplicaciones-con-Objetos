from entities.Carga import Carga

class Bidon(Carga):
    def __init__(self, contenido, capacidad, densidad):
        super().__init__(contenido)
        self.capacidad = capacidad
        self.densidad = densidad

    def peso(self):
        return self.capacidad*self.densidad

    def __str__(self):
        return super().__str__() + f" | Capacidad: {self.capacidad} | Densidad: {self.densidad}"