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
    
    
    def testUsrInputSecs(self):
        
        self.assertEqual(self.instEjercicio2.usrInputSecs(), 185)
    
    
    def testCalcFormTime(self):
        
        self.assertEqual(self.instEjercicio2.calcFormTime(3665), '1 Hora/s:1 Minuto/s:5 Segundo/s')


if __name__ == "__main__":
    unittest.main()