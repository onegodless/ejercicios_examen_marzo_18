#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
import unittest
from ejercicios.ejercicio1 import Ejercicio1

class Test(unittest.TestCase):


    def setUp(self):
        self.instEjercicio1 = Ejercicio1()


    def tearDown(self):
        pass


    def testName(self):
        pass

    
    def testcalIMC(self):
        self.assertEqual(self.instEjercicio1.calIMC(110, 1.72), 37.18) #Parametros peso en kg, altura en m.
    
if __name__ == "__main__":
    unittest.main()