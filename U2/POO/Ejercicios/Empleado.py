class Empleado:
    def __init__(self, legajo, nombre, sueldo, antiguedad):
        self.legajo = legajo
        self.nombre = nombre
        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def __str__(self):
        return f"Legajo: {self.legajo} - Nombre: {self.nombre} - Sueldo {self.sueldo} - Antiguedad {self.antiguedad}"

    def aumentar_sueldo(self, porcentaje):
        self.sueldo += (self.sueldo*(porcentaje/100))
        return self.sueldo

    def es_antiguo(self):
        return True if self.antiguedad >= 10 else False

empleado1 = Empleado(400567, "Felipe Quinteros", 100, 4)
empleado2 = Empleado(401362, "Benjamin Ottonelo", 1200000, 12)

print(empleado1)
print(empleado2)

print(f"Aumentar el sueldo en 30: {empleado1.aumentar_sueldo(30)}")
print(f"Antiguedad del Feli: {empleado1.es_antiguo()}")
print(f"Antiguedad del Benja: {empleado2.es_antiguo()}")