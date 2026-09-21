from entities.Inmueble import Inmueble

class Inmobiliaria:
    def __init__(self):
        self.inmuebles = []

    def agregar(self, inmueble):
        self.inmuebles.append(inmueble)

    def suma_alquileres(self):
        sumador = 0
        for inmueble in self.inmuebles:
            sumador += inmueble.alquiler()

        return sumador

    def cantidad_casas_premium(self):
        contador = 0
        for inmueble in self.inmuebles:
            if inmueble.es_casa() and inmueble.es_casa_premium():
                contador += 1

        return contador

    def propietario_alquiler_mas_bajo(self):
        ganador = 9999999999999999999999999
        nombre = None
        for inmueble in self.inmuebles:
            if not inmueble.es_casa() and inmueble.alquiler() < ganador:
                ganador = inmueble.alquiler()
                nombre = inmueble.propietario

        return nombre