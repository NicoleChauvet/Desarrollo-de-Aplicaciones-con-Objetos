
class Paciente:

    def __init__(self, nombre, sintoma, habitual):
        self.nombre = nombre
        self.sintoma = sintoma
        self.habitual = habitual

    def esHabitual(self):
        return self.habitual

    def __str__(self):
        return f"Nombre: {self.nombre} | Sintoma: {self.sintoma} | Habitual: {self.habitual}"