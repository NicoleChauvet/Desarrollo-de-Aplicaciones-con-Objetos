from entities.Carga import Carga

class Camion:

    def __init__(self, patente, estado, carga_maxima):
        self.patente = patente
        self.estado = estado
        self.carga_maxima = carga_maxima
        self.cargas = []

    def cantidad_cargas(self):
        return len(self.cargas)

    def subir_carga(self, carga):
        if self.estado == "disponible" and (self.peso_cargas() + carga.peso()) <= self.carga_maxima:
            self.cargas.append(carga)
            print("La carga fue subida al camion")
        else:
            print("No se pudo subir la carga al camion")

    def bajar_carga(self, carga):
        if carga in self.cargas and self.estado == "disponible":
            self.cargas.remove(carga)
            print("La carga fue removida")
        else:
            print("La carga no se encontraba en el camion")

    def peso_cargas(self):
        sumador = 0
        for carga in self.cargas:
            sumador += carga.peso()
        return sumador

    def a_reparacion(self):
        if self.estado not in ("en reparacion", "de viaje"):
            self.estado = "en reparacion"

    def sale_reparado(self):
        if self.estado != "de viaje":
            self.estado = "disponible"

    def en_viaje(self):
        if self.estado != "en reparacion":
            self.estado = "de viaje"

    def de_regreso(self):
        if self.estado != "en reparacion":
            self.estado = "disponible"

    def listo_para_salir(self):
        if self.estado == "disponible" and (self.peso_cargas() >= 0.75 * self.carga_maxima):
            return True
        return False

    def cargas_en_orden(self):
        imprimir = ""
        for carga in self.cargas:
            imprimir += str(carga) + "\n"
        return imprimir

    def __str__(self):
        return f"Patente: {self.patente} | Estado: {self.estado} | Carga Maxima: {self.carga_maxima}"