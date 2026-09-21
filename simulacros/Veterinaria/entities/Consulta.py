from entities.Atencion import Atencion

class Consulta(Atencion):

    def __init__(self, fecha, veterinario, mascota, costo_base, cantidad_vacunas):
        super().__init__(fecha, veterinario, mascota, costo_base)
        self.cantidad_vacunas = cantidad_vacunas

    def costo_total(self):
        return super().costo_total() + (self.cantidad_vacunas*1500)

    def tipo(self):
        return 1