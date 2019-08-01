#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 01:24:06 2019

@author: luisalbertocastroquevedo
"""
import unittest
class DecimalHexadecimal:
    def hexa(numero):
     auxiliar= hex(numero)[2:]
     return auxiliar
     
if __name__ == '__main__':    
     print(DecimalHexadecimal.hexa(1000))

class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado='1f4'
        valorObtenido=DecimalHexadecimal.hexa(500)
        self.assertEqual(valorObtenido,valoresperado)
 def test(self):
        valoresperado='3e8'
        valorObtenido=DecimalHexadecimal.hexa(1000)
        self.assertEqual(valorObtenido,valoresperado)        
       
 if __name__ == "__main__":
  unittest.main()          