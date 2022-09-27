def es_impar(lista):
   resultado = filter(lambda x: x % 2, lista)
   return list(resultado)