import pickle
from shutil import register_unpack_format


class Archivo():

    
    def escribe(self, entrada):
        self.entrada = entrada

        archivo = open('creacion_lectura','wb' )
        #se tiene que llamar dump 
        pickle.dump(entrada, archivo)
        archivo.close()
        print('termino modo escritura')


    def lectura(self):
        lectura = open('creacion_lectura', 'rb')
        objeto = pickle.load(lectura)
        lectura.close()
        return objeto 
    
