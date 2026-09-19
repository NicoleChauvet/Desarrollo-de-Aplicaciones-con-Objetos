
class Libro:
    def __init__(self, titulo, autor, cantPag, estPrest):
        self.titulo = titulo
        self.autor = autor
        self.cantPag = cantPag
        self.estPrest = estPrest

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Cantidad Paginas: {self.cantPag} - Estado Prestamo: {self.estPrest}"

    def prestar(self):
        if self.estPrest == False:
            self.estPrest = True
            return "Prestado"
        return "No se puede prestar"

    def devolver(self):
        self.estPrest = False
        return "Devuelto"


libro1 = Libro("La casa de los espiritus", "Isabel Allende", 480, False)
libro2 = Libro("Una corte de rosas y espinas", "Sarah J. Maas", 496, True)

print(libro1)
print(libro2)

print(f"Puedo pedir prestado el libro1? {libro1.prestar()}")
print(f"Puedo deolver el libro1? {libro1.devolver()}")
print(f"Puedo pedir el libro2 {libro2.prestar()}")
