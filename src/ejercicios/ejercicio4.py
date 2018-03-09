#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 9, 2018

@author: Jesús Molina
'''

class Ejercicio4(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def formDistance(self, distance):
        
        km = distance / 100000
        m = (float(distance) / 100000 - km)*1000
        cm = (((float(distance) / 100000 - km)*1000)-int(m))*100
        
        print ('%d km %d m %d cm') % (km, m, cm)
        
        