from functools import reduce


def sumar_lambda(impares):

    sumatoria = reduce(lambda x, y: x + y, impares)
    return sumatoria