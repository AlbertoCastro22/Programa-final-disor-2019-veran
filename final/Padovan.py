#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:55:48 2019

@author: luisalbertocastroquevedo
"""
import unittest
class Padovan:
    def Algoritmo(numero):
        if numero==0 or numero==1 or numero==2:
            variableAuxiliar=1
            return variableAuxiliar
        else:
            variableAuxiliar=Padovan.Algoritmo(numero-2)+Padovan.Algoritmo(numero-3)
            return variableAuxiliar
    contador=0
    def Siguiente():
        algoritmo=Padovan.Algoritmo(Padovan.contador)
        Padovan.contador=Padovan.contador+1
        return algoritmo
    
    def retroceder(): 
     try:
      algoritmo=Padovan.Algoritmo(Padovan.contador-1)
      if algoritmo>=0:
         Padovan.contador=Padovan.contador-1
         return algoritmo
      else:
         algoritmo=None
         return algoritmo
     except NameError:
        print("no puede haber números negativos...")
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado=816
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        valorObtenido=Padovan.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 def test_dos(self):
        valoresperado=114
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        valorObtenido=Padovan.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 def test_tres(self):
        valoresperado=55405
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.retroceder()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.retroceder()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.retroceder()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.Siguiente()
        Padovan.retroceder()
        valorObtenido=Padovan.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)         
 if __name__ == "__main__":
  unittest.main()         
        