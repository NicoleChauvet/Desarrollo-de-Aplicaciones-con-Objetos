from entities.Mantenimiento import Mantenimiento

class Maquina:
    def __init__(self):
        self.mantenimientos = []

    def agregar_mantenimiento(self, mantenimiento):
        if isinstance(mantenimiento, Mantenimiento):
            self.mantenimientos.append(mantenimiento)
        else:
            raise TypeError("El objeto a agregar debe ser de la clase Mantenimiento")

    def suma_gastos(self):
        gasto_total = 0
        for mantenimiento in self.mantenimientos:
            gasto_total += mantenimiento.obtener_gasto()
        return gasto_total

    def mantenimientos_caros(self):
        contador = 0
        for mantenimiento in self.mantenimientos:
            if mantenimiento.obtener_gasto() > 10000:
                contador +=1
        return contador

    def rotura_larga(self):
        ganador = None
        duracion = 0
        for mantenimiento in self.mantenimientos:
            if mantenimiento.es_correctivo():
                if mantenimiento.cant_horas > duracion:
                    ganador = mantenimiento
                    duracion = mantenimiento.cant_horas
        return ganador.fecha, ganador.nombre

        
