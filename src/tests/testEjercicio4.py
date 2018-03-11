#!  /usr/bin/python
# -*-  coding: latin-1 -*-
'''
Created on Mar 9, 2018

@author: Jesús Molina
'''
import unittest
from ejercicios.ejercicio4 import Ejercicio4

class Test(unittest.TestCase):


    def setUp(self):
        self.instEjercicio4 = Ejercicio4()


    def tearDown(self):
        pass

    def testName(self):
        pass


    def testFormDistance(self):
        self.instEjercicio4.formDistance(204255)

if __name__ == "__main__":
    unittest.main()