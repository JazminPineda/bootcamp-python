import sqlite3

#abro base de datos

conn = sqlite3.connect("./miaplicacion.db")

#cursor es una variable que va contener una serie de datos en un momento determinado
cursor = conn.cursor()#inicio 

# se filtra con where
rows = cursor.execute('SELECT * FROM users WHERE username= "SANDRA"') #ejecuto consulta la query 
for row in rows:
    print(row)


cursor.close() #tambien se cierra
#despues de abrir un fichero se tiene que cerrar el fichero
conn.close()