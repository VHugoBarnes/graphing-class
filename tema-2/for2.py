# encoding: utf8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""

def _aumenta4(inicio, fin):
    while inicio <= fin:
        print inicio
        inicio += 4

inicio = input('Ingresa el número de inicio: ')
final = input('Ingresa el número final: ')

_aumenta4(inicio,fin)
