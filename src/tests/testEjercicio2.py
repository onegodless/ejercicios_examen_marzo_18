#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
import unittest
from ejercicios.ejercicio2 import Ejercicio2

class Test(unittest.TestCase):


    def setUp(self):
        
        self.instEjercicio2 = Ejercicio2()


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    
    def testCalcFormTime(self):
        
        self.assertEqual(self.instEjercicio2.calcFormTime(12345), '3 Hora/s:45 Minuto/s:45 Segundo/s')
        
        
    def testCalcFormTime_Case2(self):
        
        self.assertEqual(self.instEjercicio2.calcFormTime(5), '0 Hora/s:0 Minuto/s:5 Segundo/s')


if __name__ == "__main__":
    unittest.main()