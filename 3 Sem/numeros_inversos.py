lista_nueva = []

"""Imprimer numeros impartes de forma ordenada alreves"""
def imprime_numImpar():
    for numero in range (1, 101):
        lista_nueva.append(numero)
    return print(sorted(lista_nueva, reverse = True))

imprime_numImpar()