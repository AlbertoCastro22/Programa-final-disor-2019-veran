#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:53:37 2019

@author: luisalbertocastroquevedo
"""
import unittest
class BinarioDecimal:    
    def binarioDos(variable):
     try:    
      auxiliar=int(bin(variable)[2:])
      return auxiliar
     except ValueError:
      print()
if __name__ == '__main__': 
    
     print(int(bin(50)[2:]))
     print(BinarioDecimal.binarioDos(500))


class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado=0
        valorObtenido=BinarioDecimal.binarioDos(0)
        self.assertEqual(valorObtenido,valoresperado)
 def test(self):
        valoresperado=110010
        valorObtenido=BinarioDecimal.binarioDos(50)
        self.assertEqual(valorObtenido,valoresperado)  
 def testtres(self):
        valoresperado=1010000
        valorObtenido=BinarioDecimal.binarioDos(80)
        self.assertEqual(valorObtenido,valoresperado)        
       
 if __name__ == "__main__":
  unittest.main()      