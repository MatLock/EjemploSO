'''
Created on 26/08/2013

@author: MatLock
'''
import unittest
from Class import *


class Test(unittest.TestCase):

    def setUp(self):
        lista = ['hola']
        self.x = Class(lista)
        self.x.addElement('jeje')

    def testfirstElement(self):
        hola = self.x.firstElement()
        self.assertEqual(hola, 'hola')
        self.assertEqual(2, len(self.x.list))

    def testPrintT(self):
        i = self.x.prinT()
        self.assertEqual(2, i)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()