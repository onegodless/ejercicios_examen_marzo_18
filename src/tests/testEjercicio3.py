#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 8, 2018

@author: Jesús Molina
'''
import unittest
from ejercicios.ejercicio3 import Ejercicio3

class Test(unittest.TestCase):


    def setUp(self):
        
        self.instEjercicio3 = Ejercicio3()


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    
    def testUsrMenu(self):
        
        choice = self.instEjercicio3.usrMenu()
        
    
    
    def testCalcTriangleArea(self):
        
        self.assertEqual(self.instEjercicio3.calcTriangleArea(2.45, 3.65), 4.47)
        
    
    def testCalcArea(self):
        
        self.assertEqual(self.instEjercicio3.calcCircleArea(5.87), 108.25)    

if __name__ == "__main__":
    unittest.main()