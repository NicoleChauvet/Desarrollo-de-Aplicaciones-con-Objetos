from abc import ABC, abstractmethod

class Inmueble:
    def __init__(self, codigo, propietario, superficie, alquiler_base):
        self.codigo = codigo
        self.propietario = propietario
        self.superficie = superficie
        self.alquiler_base = alquiler_base

    @abstractmethod
    def alquiler(self):
        pass

    def es_casa(self):
        return False

    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre propietario: {self.propietario} | Superficie de construccion: {self.superficie} | Importe base alquiler mensual: {self.alquiler_base}"

