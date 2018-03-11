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
    
    __menu = ('1.Calcular el �rea de un triangulo.',
             '2.Calcular el �rea de un c�rcuo.')

    def __init__(self):
        '''
        Constructor
        '''
    
    def printMenu(self):
        '''
        Desc: Prints the menu so the user can select an operation and ask the user for the 
            parameters to complete the operation.
        
        Pre: 
        
        Post: Calls one the other methods of the class with the parameters they need.
        '''
        
        print self.__menu
        usrChoice = raw_input('�Qu� quieres calcular?: ')
        
        if usrChoice == '1':
            base = float(raw_input('Qu� longitud de base quieres darle al tr�ngulo: '))
            height = float(raw_input('Qu� altura quieres darle al tri�ngulo: '))
            areaTriangle = self.calcTriangleArea(base, height)
            return areaTriangle
        
        elif usrChoice == '2':
            radius = float(raw_input('Qu� radio quieres darle al c�rculo: '))
            areaCircle = self.calcCircleArea(radius)
            return areaCircle
    
    def calcTriangleArea(self, base, height):
        '''
        Desc: Finds the area of a triangle.
        
        Pre: Takes the base and height as real numbers.
        
        Post: Returns the area of the triangle.
        '''
        #area  = base * height / 2.
        areaTriangle = (base * height) / 2
        return round(areaTriangle, 2)
    
    
    def calcCircleArea(self, radius):
        '''
        Desc: Finds the area of a circle.
        
        Pre: Takes the radius as a real number.
        
        Post: Returns the area of the circle.
        '''
        #area = pi * radius�
        areaCircle = math.pi * math.pow(radius, 2)
        return round(areaCircle, 2)