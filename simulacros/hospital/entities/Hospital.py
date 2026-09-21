from entities.Atencion import Atencion

class Hospital:

    def __init__(self, razon_social):
        self.razon_social = razon_social
        self.atenciones = []

    def addAtencion(self, atencion):
        self.atenciones.append(atencion)
        return print(f"La atencion {atencion} - se agrego con exito en la coleccion")

    def impTotalAtCons(self):
        importe_total = 0
        for atencion in self.atenciones:
            if atencion.esMedica():
                importe_total += atencion.obtenerImporte()
        return importe_total

    def imptPromAt(self):
        sumador = 0
        contador = 0
        print("Ingrese los dos valores para delimitar los importes: ")
        a = int(input("Ingrese el valor a: "))
        b = int(input("Ingrese el valor b: "))
        for atencion in self.atenciones:
            if atencion.esMedica() and a <= atencion.imptACobrar() <= b:
                sumador += atencion.imptACobrar()
                contador += 1
        if contador == 0:
            return 0
        else:
            return round(sumador/contador, 2)

    def codPrimAtHabt(self):
        for atencion in self.atenciones:
            if atencion.esMedica() and atencion.paciente.esHabitual():
                return atencion.obtenerCodigo()

        return 0

    def __str__(self):
        return f"Razon social: {self.razon_social}"