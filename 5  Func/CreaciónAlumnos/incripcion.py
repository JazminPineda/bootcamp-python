from tracemalloc import Statistic
from alumnos import Alumno
import statistics

class Inscripcion():

    def __init__(self, alumno, prog, estadid, bd):
        self.prog = prog
        self.estadis = estadid
        self.bd = bd

    def materias_cursadas(self, alumno, prog, estadid, bd):
    
        self.prog = prog
        self.estadis = estadid
        self.bd = bd
      
        self.materias = {   
         
            'id_alumno' : alumno.id_interno,
            # 'materias' : materias,
            'programacion': prog,
            'estadistica' : estadid,
            'base_de_datos' : bd,
        }
    
    def promedio_cursada(self ):
        #accedo a los atributos
        lista = [self.prog, self.estadis, self.bd] 
        resultado = statistics.mean(lista)
        return resultado

    def aprobado(self, resultado):
        if resultado > 4:
            return "Aprobo"
        else:
            return "Desaprobado"

#muestra resultado
    def __str__(self) :
        return f'{self.prog}, {self.estadis}, {self.bd}'

 

alumno = Alumno("Federico", "Ciencia de Datos")
alumno1 = Alumno("Federico", "Ciencia de Datos")
alumno3 = Alumno("Federico", "Ciencia de Datos")
print(alumno)

materias_cursadas = Inscripcion(alumno, 5, 8, 6)

# cursada  = materias_cursadas.promedio_cursada(materias_cursadas)
nota = materias_cursadas.promedio_cursada()
print(nota)
print(materias_cursadas.aprobado(nota))
# alumno.promedio_cursada(materias_cursada)

# # print(alumno.carrera)