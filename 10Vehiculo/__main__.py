
from auto import Auto, AudiA5Full, AudiStock

def main():
   # Miauto = Auto() cuando no se definen parametros 
    MiAudiFull = AudiA5Full('Rojo perlado', 5632120)
    print(MiAudiFull)
    print(MiAudiFull.sonido())
    MiStock = AudiStock('v5', 4, 3, 'negro', 'audi', 'unica', '1000cc', 500000)
    
    print(MiStock)


if __name__== "__main__":
    main()