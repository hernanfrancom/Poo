class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.numero_paginas}")

    def actualizar_numero_paginas(self, nuevo_numero_paginas):
        self.numero_paginas = nuevo_numero_paginas
        print(f"El número de páginas ha sido actualizado a {self.numero_paginas}")


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 432)
libro1.mostrar_informacion()


libro1.actualizar_numero_paginas(450)
libro1.mostrar_informacion()