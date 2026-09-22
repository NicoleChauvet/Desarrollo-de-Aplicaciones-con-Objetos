from abc import ABC, abstractmethod

class PaqueteViaje(ABC):

    def __init__(self, codigo, cliente, cantidad_personas, precio_base):
        self.codigo = codigo
        self.cliente = cliente
        self.cantidad_personas = cantidad_personas
        self.precio_base = precio_base

    @abstractmethod
    def precio_total(self):
        return self.precio_base

    @abstractmethod
    def tipo(self):
        pass

    def es_paquete_grupal(self):
        return (self.cantidad_personas > 4 and self.precio_total() > 100000)
    