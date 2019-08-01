#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:27:16 2019

@author: luisalbertocastroquevedo
"""
import unittest
class NumeroUlam:
    contador=1
    contador2=0
    def Algoritmo(numero):
        valor=numero%2
        if valor==0:
            numero=numero/2
            return int(numero)
        else:
            numero=numero*3
            numero=numero+1
            return int(numero)
    
    def Siguiente():
        algoritmo=NumeroUlam.Algoritmo(NumeroUlam.contador2)
        NumeroUlam.contador2=NumeroUlam.contador2+1
        return algoritmo
    def retroceder(): 
     try:
      auxiliar=NumeroUlam.Algoritmo(NumeroUlam.contador2-1)
      if auxiliar>=1:
       NumeroUlam.contador2=NumeroUlam.contador2-1
       return auxiliar
      else:
       auxiliar=-1
      return auxiliar
     except NameError:
       print("error")

class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado=5
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        valorObtenido= NumeroUlam.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 def test_dos(self):
        valoresperado=2
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.retroceder()
        valorObtenido= NumeroUlam.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 def test_tres(self):
        valoresperado=64
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.Siguiente()
        NumeroUlam.retroceder()
        valorObtenido= NumeroUlam.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 if __name__ == "__main__":
  unittest.main()   
         