#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:33:52 2019

@author: luisalbertocastroquevedo
"""

class NumeroSuerte:
    contador=0
    contador2=0
    def Algoritmo(numero):
        siguientePosicion=numero
        if NumeroSuerte.contador > numero :
            return numero
        if numero % NumeroSuerte.contador==0 :
            return 0
        siguientePosicion=siguientePosicion-1
        NumeroSuerte.contador=NumeroSuerte.contador+1
        
    def Siguiente():
        algoritmo=NumeroSuerte.Algoritmo(NumeroSuerte.contador2)
        NumeroSuerte.contador2=NumeroSuerte.contador2+1
        return algoritmo

if __name__ == "__main__":
   numero=NumeroSuerte
   print(numero.Siguiente())
   print(numero.Siguiente())
   print(numero.Siguiente())
   print(numero.Siguiente())
   print(numero.Siguiente())
   print(numero.Siguiente())
   
                      
            
        