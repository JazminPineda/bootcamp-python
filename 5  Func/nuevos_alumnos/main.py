from  persona import Persona
from alumno import Alumno

lucas = Persona("Lucas", "Bonanni", "35456412", '15/02/2012')
# Alumno(lucas).legajo = 45185
# lucasAlumno = Alumno("Lucas", "Bonanni", "35456412", '15/02/2012', 123456)

lucasAlumno = Alumno(lucas, 123456)

lucasAlumno.establecer_carrera('Analisis')

print(lucasAlumno)