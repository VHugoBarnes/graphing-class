# encoding: utf-8

"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""

print 'Dame un numero'
numero = input()

if numero > 0:
    print 'El número ', numero, ' es positivo.'
elif numero < 0:
    print 'El número ', numero, ' es negativo.'
elif numero == 0:
    print 'El número es cero' 