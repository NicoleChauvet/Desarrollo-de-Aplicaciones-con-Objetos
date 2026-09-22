from abc import ABC, abstractmethod

class Reparacion(ABC):

    def __init__(self, codigo, cliente, equipo, costo_base):
        self.codigo = codigo
        self.cliente = cliente
        self.equipo = equipo
        self.costo_base = costo_base

    @abstractmethod
    def costo_total(self):
        return self.costo_base

    @abstractmethod
    def tipo(self):
        pass

    def es_Reparacion(self, reparacion):
        return isinstance(reparacion, Reparacion)

    def getCliente(self):
        return self.cliente