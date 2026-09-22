from models.PaqueteViaje import PaqueteViaje

class AgenciaViajes():

    def __init__(self):
        self.paquetes = []

    def agregar_paquete(self, paquete):
        self.paquetes.append(paquete) if isinstance(paquete, PaqueteViaje) else print(f" (x) Error: el objeto {paquete} no es una instancia de PaqueteViaje")

    def total_recaudado(self):
        sumador = 0
        for paquete in self.paquetes:
            sumador += paquete.precio_total()
        return sumador

    def cantidad_paquetes_grupales(self):
        contador = 0
        for paquete in self.paquetes:
            if paquete.es_paquete_grupal():
                contador +=1
        return contador

    def cliente_paquete_mas_caro(self):
        ganador = None

        for paquete in self.paquetes:
            if paquete.tipo() == 2:
                if ganador == None:
                    ganador = paquete
                elif paquete.precio_total() > ganador.precio_total():
                    ganador = paquete
        if ganador != None:
            return ganador.getCliente()
        return ganador