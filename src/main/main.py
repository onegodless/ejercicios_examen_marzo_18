#! /usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
from ejercicios.ejercicio1 import Ejercicio1
from ejercicios.ejercicio2 import Ejercicio2
from ejercicios.ejercicio3 import Ejercicio3
from ejercicios.ejercicio4 import Ejercicio4
from ejercicios.ejercicio5 import Ejercicio5


if __name__ == '__main__':
    
    #Ejercicio 1.
    print 'Ejercicio 1: '
    instEjercicio1 = Ejercicio1()
    print 'EL indice de masa corporal es: %f.' %  (instEjercicio1.calIMC(110, 1.72))
    print '\n'
    
    
    #Ejercicio 2.
    print 'Ejercicio 2: '
    instEjercicio2 = Ejercicio2()
    secs = instEjercicio2.usrInputSecs()
    print instEjercicio2.calcFormTime(secs)
    print '\n'
    
    #Ejercicio 3.
    print 'Ejercicio 3: '
    instEjercicio3 = Ejercicio3()
    print instEjercicio3.printMenu()
    print '\n'
    
    #Ejercicio 4.
    print 'Ejercicio 4: '
    instEjercicio4 = Ejercicio4()
    instEjercicio4.formDistance(204521)
    print '\n'
    
    #Ejercicio5
    instEjercicio5 = Ejercicio5()
    instEjercicio5.gameLoop()