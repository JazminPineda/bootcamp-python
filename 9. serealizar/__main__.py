#from crear_archivo import Archivo
import os 
from pathlib import Path

def main():
    #f = Archivo()
      
    def creando():
        # ruta = 'C:\Users\jazmin\Documents\Proyectos\bootcamp-python'
        # carpeta  = Path('docrest.txt')
        # carpeta.touch(exist_ok = True)
        carpeta = open('docrest.txt','a+' )
        carpeta.close()
        print("archivo creado")
    
    def escribe():
        carpeta = open('docrest.txt','w+' )
        carpeta.write("Escribo mi primera linea")
        carpeta.close()
        print('termino modo escritura')
        


    creando()
    escribe()

if __name__ == "__main__":
    main()