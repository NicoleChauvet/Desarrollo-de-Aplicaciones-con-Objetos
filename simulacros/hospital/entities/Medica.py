from entities.Atencion import Atencion
from entities.Paciente import Paciente

class Medica(Atencion):

    def __init__(self, codigo, tipo_cobro, importe, paciente):
        super().__init__(codigo, tipo_cobro)
        self.importe = importe
        self.paciente = paciente

    def imptACobrar(self):
        total = self.importe

        if self.paciente.esHabitual():
            total = total - total*0.25

        if self.tipo_cobro == 1:
            total = total - total*0.10
        else:
            total = total + total*0.20
        
        return total

    def esMedica(self):
        return True

    def obtenerImporte(self):
        return self.importe

    def __str__(self):
        return super().__str__() + f" | Importe: {self.importe} | Paciente: [{str(self.paciente)}]"