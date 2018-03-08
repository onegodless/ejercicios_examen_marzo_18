#! /usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
from ejercicios.ejercicio1 import Ejercicio1


if __name__ == '__main__':
    
    instEjercicio1 = Ejercicio1()
    print 'EL indice de masa corporal es: %f.' %  (instEjercicio1.calIMC(110, 1.72))
    