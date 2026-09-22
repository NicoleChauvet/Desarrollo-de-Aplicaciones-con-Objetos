from models.PaqueteViaje import PaqueteViaje

class AgenciaViajes():

    def __init__(self):
        self.paquetes = []

    def agregar_paquete(self, paquete):
        self.paquetes.append(self.paquetes) if isinstance(paquete, PaqueteViaje) else print(f" (x) Error: el objeto {paquete} no es una instancia de PaqueteViaje")

    def total_recaudado(self):
        sumador = 0
        for paquete in self.paquetes:
            sumador += paquete. precio_total()
        return sumador

    def cantidad_paquetes_grupales(self):
        pass