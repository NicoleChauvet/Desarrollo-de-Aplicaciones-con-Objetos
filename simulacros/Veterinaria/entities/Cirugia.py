from entities.Atencion import Atencion

class Cirugia(Atencion):

    def __init__(self, fecha, veterinario, mascota, costo_base, horas_quirofano):
        super().__init__(fecha, veterinario, mascota, costo_base)
        self._horas_quirofano = horas_quirofano

    def costo_total(self):
        return super().costo_total() + (self._horas_quirofano*5000)

    def tipo(self):
        return 2

    @property
    def horas_quirofano(self):
        return self._horas_quirofano

    def obtener_fecha_veterinario(self):
        return self.fecha, self.veterinario