#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:34:53 2019

@author: luisalbertocastroquevedo
"""
import unittest
class Capicua:
     def NumeroCapicua(numero):
         #Intervalo inferior
         a=int(numero)
         #Intervalo superior 
         b=454657
         #Contador para la cantidad de capicuas
         c=0
         for i in range(a,b+1):
           num_s=str(i)
           num_list=list(num_s)
           if num_list==num_list[::-1]:
            cap=''.join(num_list)
            c+=1
            cadena="el número "+str(numero)+" es capicúa"
            return cadena
           else:
              cadena="el número "+str(numero)+" no es capicúa"
              return cadena
             
c=0
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado='el número 600 no es capicúa'
        valorObtenido=Capicua.NumeroCapicua(600)
        self.assertEqual(valorObtenido,valoresperado)
 def test_dos(self):
        valoresperado='el número 606 es capicúa'
        valorObtenido=Capicua.NumeroCapicua(606)
        self.assertEqual(valorObtenido,valoresperado)
 def test_tres(self):
        valoresperado='el número 636 es capicúa'
        valorObtenido=Capicua.NumeroCapicua(636)
        self.assertEqual(valorObtenido,valoresperado)
 def test_cuatro(self):
        valoresperado='el número 66 es capicúa'
        valorObtenido=Capicua.NumeroCapicua(66)
        self.assertEqual(valorObtenido,valoresperado)
 def test_cinco(self):
        valoresperado='el número 600 no es capicúa'
        valorObtenido=Capicua.NumeroCapicua(606)
        self.assertEqual(valorObtenido,valoresperado)        
if __name__ == "__main__":
    unittest.main() 