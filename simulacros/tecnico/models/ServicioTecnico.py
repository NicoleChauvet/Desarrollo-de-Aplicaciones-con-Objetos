from models.Reparacion import Reparacion

class ServicioTecnico():

    def __init__(self):
        self.reparaciones = []

    def agregar(self, reparacion):
        if reparacion.es_Reparacion(reparacion):
            self.reparaciones.append(reparacion)
        else:
            print(f" (x) Error: no es una instancia de Reparacion el objeto {reparacion}")

    def suma_facturado(self):
        sumador = 0
        for reparacion in self.reparaciones:
            sumador += reparacion.costo_total()
        return sumador

    def cantidad_reparaciones_premium(self):
        contador = 0
        for reparacion in self.reparaciones:
            if reparacion.tipo() == 1 and reparacion.es_premium():
                contador +=1

        return contador

    def cliente_reparacion_mas_barata(self):
        ganador = None

        for reparacion in self.reparaciones:
            if reparacion.tipo() == 2:
                if ganador == None:
                    ganador = reparacion
                elif reparacion.costo_total() < ganador.costo_total():
                    ganador = reparacion

        if ganador == None:
            return None
        return ganador.getCliente()
