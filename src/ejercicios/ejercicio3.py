#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jes�s Molina
'''

import math

class Ejercicio3(object):
    '''
    classdocs
    '''
    
    
    menu = ('1.Calcular el �rea de un triangulo.',
             '2.Calcular el �rea de un c�rcuo.')

    def __init__(self):
        '''
        Constructor
        '''
    
    
    def usrMenu(self):
        
        print self.menu
        choice = raw_input('Elige una de las opciones.')
        
    
    def calcTriangleArea(self, base, height):
        
        #area  = base * height / 2.
        areaTriangle = (base * height) / 2
        return round(areaTriangle, 2)
    
    
    def calcCircleArea(self, radius):
        
        #area = pi * radius�
        areaCircle = math.pi * math.pow(radius, 2)
        return round(areaCircle, 2)