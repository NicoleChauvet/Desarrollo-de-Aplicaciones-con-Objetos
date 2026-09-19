from entities.Mantenimiento import Mantenimiento

class Correctivo(Mantenimiento):
    def __init__(self, fecha, nombre, importe, cant_horas, impt_cobro):
        super().__init__(fecha, nombre, importe)
        self.cant_horas = cant_horas
        self.impt_cobro = impt_cobro

    def obtener_gasto(self):
        return super().obtener_gasto() + self.impt_cobro

    def es_correctivo(self):
        return True

    def __str__(self):
        return super().__str__() + f" | Cantidad Horas: {self.cant_horas} | Importe cobro: {self.impt_cobro}"