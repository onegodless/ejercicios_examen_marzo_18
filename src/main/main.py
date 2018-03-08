#! /usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
from ejercicios.ejercicio1 import Ejercicio1
from ejercicios.ejercicio2 import Ejercicio2


if __name__ == '__main__':
    
    instEjercicio1 = Ejercicio1()
    print 'EL indice de masa corporal es: %f.' %  (instEjercicio1.calIMC(110, 1.72))
    
    instEjercicio2 = Ejercicio2()
    secs = instEjercicio2.usrInputSecs()
    print instEjercicio2.calcFormTime(secs)
    