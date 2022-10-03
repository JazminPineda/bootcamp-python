import re
import sqlite3
import getpass


#abro base de datos

# def main2():
    # crear_usuario(9, 'lUCAS', 'ROJAS')
    # crear_usuario(10, 'MARIO', 'lOPEZ')
    # crear_usuario(11, 'MARIA', 'CARDENAS')

def main2():
    nombre = input("Nombre del alumno que desea buscar: ")
    busqueda_alumno(nombre)
       

     

def busqueda_alumno(nombre):
    conn = sqlite3.connect("./miaplicacion.db")
    cursor = conn.cursor()# se llama cursor
    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"

    rows = cursor.execute(query)
    for row in rows:
        if row == None:
            return print("Alumno no encontrado")
        return  print(f"Alumno encontrado sus datos son  {row}")


    cursor.execute
    cursor.close()
    conn.close()
  
 

def crear_usuario(identificador, nombre, apellido):
    conn = sqlite3.connect("./miaplicacion.db", isolation_level=None)
    cursor = conn.cursor()# se llama cursor
   
    query = f"INSERT INTO alumnos (id, nombre, apellido) VALUES(?,?,?) "
    #print("query a ejecutar: ", query)
    rows = cursor.execute(query, (identificador, nombre, apellido)) #en cada execute se ejecuta

    conn.commit() # para actualizar y enviar cambios a la base de datos, si no no se envia 

    cursor.close()
    conn.close()



if __name__ == "__main__":
    main2()

