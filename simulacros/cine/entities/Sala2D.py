from entities.Sala import Sala

class Sala2D(Sala):

    def __init__(self, numero, capacidad, recaudacion, premium):
        super().__init__(numero, capacidad, recaudacion)
        self.premium = premium

    def resultado_neto(self):
        return self.recaudacion

    def es_rentable(self):
        if self.capacidad != 0:
            if self.premium:
                return self.conocer_indice() > 55

            return self.conocer_indice() > 40

        return False

    def conocer_indice(self):
        if self.capacidad > 0:
            return round(self.resultado_neto()/self.capacidad, 2)

        return 0

    def tipo(self):
        return 1