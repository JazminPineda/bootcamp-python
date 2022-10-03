import re
import sqlite3
import getpass


#abro base de datos

def main():
    crear_usuario(34, 'MARIO', '4567')


def main2() :
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect("./miaplicacion.db")
    cursor = conn.cursor()# se llama cursor
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    #print("query a ejecutar: ", query)
    rows = cursor.execute(query)
    data = rows.fetchone()# solo devuelve un elemento
    cursor.execute
    print("data es ", type(data))

    cursor.close()
    conn.close()


    if data == None:
        return False
    return True


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect("./miaplicacion.db", isolation_level=None)
    cursor = conn.cursor()# se llama cursor
    identificador += 1
    query = f"INSERT INTO users (id, username, password) VALUES(?,?,?) "
    #print("query a ejecutar: ", query)
    rows = cursor.execute(query, (identificador, usuario,clave)) #en cada execute se ejecuta
    print("data es ", type(rows), rows)
    conn.commit() # para actualizar y enviar cambios a la base de datos, si no no se envia 

    cursor.close()
    conn.close()




if __name__ == "__main__":
    main()


# conn = sqlite3.connect("./miaplicacion.db")

# cursor es una variable que va contener una serie de datos en un momento determinado
# cursor = conn.cursor()#inicio 

# se filtra con where se envia la consulta 
# rows = cursor.execute('SELECT * FROM users WHERE username= "SANDRA"') #ejecuto consulta la query 
# for row in rows:
#     print(row)


# cursor.close() #tambien se cierra el cursor
# despues de abrir un fichero se tiene que cerrar el fichero
# conn.close()