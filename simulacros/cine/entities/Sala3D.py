from entities.Sala import Sala

class Sala3D(Sala):

    def __init__(self, numero, capacidad, recaudacion, adicional_lentes):
        super().__init__(numero, capacidad, recaudacion)
        self.adicional_lentes = adicional_lentes

    def resultado_neto(self):
        return self.recaudacion + self.adicional_lentes

    def conocer_indice(self):
        if self.capacidad != 0:
            return round(self.resultado_neto()/self.capacidad, 2)

        return 0

    def es_rentable(self):
        return self.conocer_indice() > 60

    def tipo(self):
        return 2