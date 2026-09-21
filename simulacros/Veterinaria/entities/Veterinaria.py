from entities.Atencion import Atencion

class Veterinaria():

    def __init__(self):
        self.atenciones = []

    def agregar_atencion(self, atencion):
        self.atenciones.append(atencion)

    def suma_facturado(self):
        sumador = 0
        for atencion in self.atenciones:
            sumador += atencion.costo_total()

        return sumador

    def atenciones_costosas(self):
        contador = 0
        for atencion in self.atenciones:
            if atencion.costo_total() > 15000:
                contador += 1

        return contador

    def cirugia_mas_larga(self):
        ganador = None

        for atencion in self.atenciones:
            if atencion.tipo() == 2:
                if ganador is None or atencion.horas_quirofano > ganador.horas_quirofano:
                    ganador = atencion

        if ganador is None:
            return None

        return ganador.obtener_fecha_veterinario()

