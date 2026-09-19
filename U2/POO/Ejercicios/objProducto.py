
# class Alumno:

#     def __init__ (self, legajo, nombre, nota1, nota2):
#         self.legajo = legajo
#         self.nombre = nombre
#         self.nota1 = nota1
#         self.nota2 = nota2

#     def __str__ (self):
#         return "\nLegajo: "+ str(self.legajo) + \
#         "- Nombre: " + str(self.nombre) + \
#         " - Nota1: " +str(self.nota1)+ \
#         " -Nota2:"+str(self.nota2)

#     def promedio(self):
#         promedio = (self.nota1 + self.nota2) / 2
#         return promedio

class Producto:

    def __init__ (self, codigo, desc, precio, stock):
        self._codigo = codigo
        self.desc = desc
        self.precio = precio
        self.stock = stock

    def __str__ (self):
        return f"Codigo: {self.codigo} - Descripción: {self.desc} - Precio: ${self.precio} - Stock: {self.stock}"

    def hayStock (self):
        return True if self.stock > 0 else False

    def valorStock (self):
        return self.stock

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self,  nuevo_codigo):
        self._codigo = nuevo_codigo



producto1 = Producto(1, "Café", 2000, 0)
producto2 = Producto(2, "Te", 800, 30)

print(f"Producto 1: {producto1} \nProducto 2: {producto2}")
print(f"¿Stock Producto 1? : {producto1.hayStock()} \n¿Stock Producto 2? : {producto2.hayStock()}")


producto1._codigo = 4
print(producto1)