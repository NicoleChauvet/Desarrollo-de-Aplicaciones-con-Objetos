from abc import ABC, abstractmethod

class Atencion:

    def __init__(self, codigo, tipo_cobro):
        self.codigo = codigo
        self.tipo_cobro = tipo_cobro

    @abstractmethod
    def imptACobrar(self):
        pass

    def esMedica(self):
        return False

    def obtenerCodigo(self):
        return self.codigo

    def __str__(self):
        return f"Codigo: {self.codigo} | Tipo cobro: {self.tipo_cobro}"
