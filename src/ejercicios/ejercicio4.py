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
        '''
        Desc: Converts the given distance in cm into Km, m, cm.
        
        Pre: Takes a real number representing the distance in cm.
        
        Post: Prints the conversion as a string.
        '''
        km = int(distance / 100000)
        m = int(((float(distance) / 100000) - km) * 1000)
        cm = int((((float(distance) / 100000 - km) * 1000) - int(m)) * 100)
        
        print ('%d km %d m %d cm') % (km, m, cm)
        
            