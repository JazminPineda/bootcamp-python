
from auto import Auto, AudiA5Full, AudiStock
from crear_archivo import Archivo

def main():
   # Miauto = Auto() cuando no se definen parametros 
    archivo = Archivo()

    escritura = []
    MiAudiFull = AudiA5Full('Rojo perlado', 5632120)
    print(MiAudiFull)
    print(MiAudiFull.sonido())
    MiStock = AudiStock('v5', 4, 3, 'negro', 'audi', 'unica', '1000cc', 500000)
    escritura.append(MiAudiFull)
    archivo.escribe(MiAudiFull)
    print(archivo.lectura())


if __name__== "__main__":
    main()