from abc import ABC, abstractmethod

class Mantenimiento:
    def __init__(self, fecha, nombre, importe):
        self.fecha = fecha
        self.nombre = nombre
        self.importe = importe
    
    def __str__(self):
        return f"Fecha: {self.fecha} \n Nombre operario: {self.nombre} \n Importe gastado: {self.importe}"

    @abstractmethod
    def obtener_gasto(self):
        return self.importe

    def es_correctivo(self):
        return False

    def __str__(self):
        return f"Fecha: {self.fecha} | Nombre: {self.nombre} | Importe: {self.importe}"