from entities.Sala import Sala

class SalaVIP(Sala):

    def __init__(self, numero, capacidad, recaudacion, costo_servicio):
        super().__init__(numero, capacidad, recaudacion)
        self.costo_servicio = costo_servicio

    def resultado_neto(self):
        return self.recaudacion - self.costo_servicio

    def conocer_indice(self):
        if self.capacidad != 0:
            return round(self.resultado_neto()/self.capacidad)

        return 0

    def es_rentable(self):
        return self.conocer_indice() > 90

    def tipo(self):
        return 3