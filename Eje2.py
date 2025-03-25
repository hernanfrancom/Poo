class Estudiante:
    def __init__(self,nombre,edad,calificacion):

        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def aprovado (self):
        if self.calificacion >= 3 :
            return f"{self.nombre} ha aprobado con una calificación de {self.calificacion}."
          
        else:
            return f"{self.nombre} ha reprobado con una calificación de {self.calificacion}."
        

Estudiante1 = Estudiante ("juan perez", 20,2)
print (Estudiante1.aprovado( )) 

Estudiante2 = Estudiante ("carlos muñoz", 20,6)
print (Estudiante2.aprovado( )) 

