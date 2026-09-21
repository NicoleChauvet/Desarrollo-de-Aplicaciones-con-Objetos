from abc import ABC, abstractmethod

class Atencion(ABC):

    def __init__(self, fecha, veterinario, mascota, costo_base):
        self.fecha = fecha
        self.veterinario = veterinario 
        self.mascota = mascota
        self.costo_base = costo_base

    @abstractmethod
    def costo_total(self):
        return self.costo_base

    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        return f"{self.fecha} {self.veterinario}"

