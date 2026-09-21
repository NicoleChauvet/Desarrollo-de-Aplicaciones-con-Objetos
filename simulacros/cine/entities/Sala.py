from abc import ABC, abstractmethod

class Sala(ABC):

    def __init__(self, numero, capacidad, recaudacion):
        self.numero = numero
        self.capacidad = capacidad
        self.recaudacion = recaudacion

    @abstractmethod
    def resultado_neto(self):
        pass

    @abstractmethod
    def es_rentable(self):
        pass

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def conocer_indice(self):
        pass

    def conocer_numero_tipo(self):
        return self.numero, self.tipo()

    def __str__(self):
        return f"{self.numero} {self.tipo()}"