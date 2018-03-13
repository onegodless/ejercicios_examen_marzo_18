#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 13, 2018

@author: Jesús Molina
'''
import unittest
from ejercicios.ejercicio5 import Ejercicio5

class Test(unittest.TestCase):


    def setUp(self):
        self.instanceEjercicio5 = Ejercicio5()


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    
    def testCardGenerator(self):
        
        self.instanceEjercicio5.cardGenerator()

        
    def testPrintCards(self):
        
        self.instanceEjercicio5.printCards()
        
    
    def testPrintRound(self):
        
        self.instanceEjercicio5.printRound()
    
    
    

if __name__ == "__main__":
    unittest.main()