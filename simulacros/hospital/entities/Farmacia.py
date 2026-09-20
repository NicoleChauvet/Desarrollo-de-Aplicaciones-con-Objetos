from entities.Atencion import Atencion

class Farmacia(Atencion):

    def __init__(self, codigo, tipo_cobro, importe, cupon):
        super().__init__(codigo, tipo_cobro)
        self.importe = importe
        self.cupon = cupon

    def imptACobrar(self):
        total = self.importe

        if self.cupon > 0:
            total -= self.cupon

        if self.tipo_cobro == 1:
            total = total - total*0.10
        else:
            total = total + total*0.30

        return total

    def esMedica(self):
        return super().esMedica()

    def __str__(self):
        return super().__str__() + f" | Importe: {self.importe} | Cupon: {self.cupon}"