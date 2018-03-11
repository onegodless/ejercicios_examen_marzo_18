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
        '''
        Desc: Asks the user to input the amount of seconds to format in hours, minutes and seconds.
        
        Pre:
        
        Post: Returns the integer that the user introduced.
        '''
        intUsrSecs = int(raw_input('Introduce una cantidad de segundos: '))
        return intUsrSecs
    
    
    def calcFormTime(self, intUsrSecs):
        '''
        Desc: Formats the time with the given seconds into Hours: Minutes : Seconds.
        
        Pre: Takes an integer as a paremeter.
        
        Post: Returns the time formatted as a string.
        '''
        if intUsrSecs >= 60:
            intCalcSecs = int(intUsrSecs % 60)
        else:
            intCalcSecs = intUsrSecs

        if intUsrSecs >= 60:
            intCalcMin = int(intUsrSecs % 60)
        else:
            intCalcMin = 0
            
        if intCalcMin >= 1:
            intCalcHours = int((intUsrSecs / 60) / 60)
        else: 
            intCalcHours = 0
        
        formatTime = '%d Hora/s:%d Minuto/s:%d Segundo/s' % (intCalcHours, intCalcMin, intCalcSecs)
        return formatTime