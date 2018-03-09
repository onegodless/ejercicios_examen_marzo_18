#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jesús Molina
'''

import math

class Ejercicio3(object):
    '''
    classdocs
    '''
    
    __menu = ('1.Calcular el área de un triangulo.',
             '2.Calcular el área de un círcuo.')

    def __init__(self):
        '''
        Constructor
        '''
    
    def validateUsrInput(self, input):
        for x in input:
            try:
                float(x)
                return 'Valid'
            except ValueError:
                return 'notValid'
    
    
    def menuPrint(self):
        
        print self.menu
        while True:
            choice = raw_input('Elige una de las opciones o escribe "q" para salir: ')
            if choice == 1:
                self.usrInputTriagle()
                break
                
            elif choice == 2:
                self.usrInputCircle()
                break
                
            elif choice == 'q':
                break

    
    
    def usrInputTriangle(self):
        
        status = 'notValid'
        
        while self.__status == 'notValid':
            baseTriangle = raw_input('Elige una base para el triángulo o escribe "q" para salir: ')
            status = self.validateUsrInput(baseTriangle)
            
        status = 'notValid'
        
        while status == 'notValid':
            heightTriangle = raw_input('Elige una altura para el triángulo: ')
            status = self.validateUsrInput(heightTriangle)
            
        self.calcTriangleArea(int(baseTriangle), int(heightTriangle))
        
        
    def usrInputCircle(self):
        
        radiusCircle = raw_input('Elige un radio para el círculo.')
        self.calcCircleArea(int(radiusCircle))
        
    
    def calcTriangleArea(self, base, height):
        
        #area  = base * height / 2.
        areaTriangle = (base * height) / 2
        return round(areaTriangle, 2)
    
    
    def calcCircleArea(self, radius):
        
        #area = pi * radius²
        areaCircle = math.pi * math.pow(radius, 2)
        return round(areaCircle, 2)