#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:12:38 2019

@author: luisalbertocastroquevedo
"""
import unittest
class NumeroSuerte:
    def Algoritmo(dia,mes,anio):
        total=dia+mes+anio
        primerDigito=total /1000
        segundoDigito = (total /100)%10
        tercerDigito = (total /10)%10
        cuartoDigito = total % 10
        suerte = primerDigito+segundoDigito+tercerDigito+cuartoDigito
        return suerte
    contador=0
    def Siguiente():
        algoritmo=NumeroSuerte.Algoritmo(NumeroSuerte.contador,NumeroSuerte.contador,NumeroSuerte.contador)
        NumeroSuerte.contador=NumeroSuerte.contador+1
        return int(algoritmo)
    
    def retroceder(): 
     try:
      algoritmo=NumeroSuerte.Algoritmo(NumeroSuerte.contador-1,NumeroSuerte.contador-1,NumeroSuerte.contador-1)
      if algoritmo>=0:
         NumeroSuerte.contador=NumeroSuerte.contador-1
         return int(algoritmo)
      else:
         algoritmo=None
         return algoritmo
     except NameError:
        print("no puede haber números negativos...")
        
        #aquí empiesa la prueba unitaria...
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado= 9
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        valorObtenido=NumeroSuerte.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)
 def test_dos(self):
        valoresperado= 13
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        valorObtenido=NumeroSuerte.Siguiente()
        valorObtenido=NumeroSuerte.Siguiente()
        self.assertEqual(valorObtenido,valoresperado) 
 def test_tres(self):
        valoresperado= 13
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.retroceder()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.retroceder()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.Siguiente()
        NumeroSuerte.retroceder()
        valorObtenido=NumeroSuerte.Siguiente()
        valorObtenido=NumeroSuerte.Siguiente()
        self.assertEqual(valorObtenido,valoresperado)        
if __name__ == "__main__":
     unittest.main()         