#! /usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
import math


class Ejercicio1(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def calIMC(self, peso, altura):
        '''
        Desc: Calcula el indice de masa corporal.
        
        Pre: Toma peso como un entero, y altura como un flotante.
        
        Post: Devuelve el indice de masa corporal como flotante con dos decimales.
        '''
        # imc = peso / altura², peso en Kg, altura en m.
        
        imc = peso / math.pow(altura, 2) 
        return round(imc,2)
        