from entities.Sala import Sala

class Cine():

    def __init__(self):
        self.salas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def recaudacion_total(self):
        sumador = 0
        for sala in self.salas:
            sumador += sala.resultado_neto()

        return sumador

    def cantidad_no_rentables(self):
        contador = 0
        for sala in self.salas:
            if not sala.es_rentable():
                contador += 1

        return contador

    def sala_mas_rentable(self):
        if not self.salas:
            return None
        ganador = self.salas[0]
        for sala in self.salas:
            if sala.conocer_indice() > ganador.conocer_indice():
                ganador = sala

        return ganador
