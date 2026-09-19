from entities.Mantenimiento import Mantenimiento


class Preventivo(Mantenimiento):
    def __init__(self, fecha, nombre, importe, resultado, impt_insumos):
        super().__init__(fecha, nombre, importe)
        self.resultado = resultado
        self.impt_insumos = impt_insumos

    def obtener_gasto(self):
        return super().obtener_gasto() + self.impt_insumos

    def es_correctivo(self):
        return super().es_correctivo()

    def __str__(self):
        return super().__str__() + f" | Resultado: {self.resultado} | Importe insumos: {self.impt_insumos}"