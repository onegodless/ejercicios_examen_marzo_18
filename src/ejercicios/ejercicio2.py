#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jesús Molina
'''

class Ejercicio2(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def usrInputSecs(self):
        
        intUsrSecs = int(raw_input('Introduce una cantidad de segundos: '))
        return intUsrSecs
    
    
    def calcFormTime(self, intUsrSecs):
        
        if intUsrSecs >= 60:
            intCalcSecs = int(intUsrSecs % 60)

        if intUsrSecs >= 60:
            intCalcMin = int(intUsrSecs / 60) - 60
            
        if intCalcMin >= 60:
            intCalcHours = int((intUsrSecs / 60) / 60)
        
        formatTime = '%d Hora/s:%d Minuto/s:%d Segundo/s' % (intCalcHours, intCalcMin, intCalcSecs)
        return formatTime