def main():
    pass



if __name__== "__main__":
    
    lista_paises= ["arabia", "peru", "colombia", "argentina", "peru", "ecuador", "mexico", "venezuela", "panama",  "peru", "colombia", "argentina"]
    lista_final  = set(lista_paises)
    ordenada = sorted(lista_final) 

    for pais in ordenada:
       
        texto = f'{pais}, '
        print(texto, end="")
      
   

    main()