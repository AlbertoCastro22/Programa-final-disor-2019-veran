#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:05:09 2019

@author: luisalbertocastroquevedo
"""
import math
import unittest
class NumeroFeliz:
    def obtenerDigitos(numero):
       # numeros=numero
        lista=[]
        digito=0
        auxiliar=[]
        while numero>0:
            auxiliar=lista.append(digito)
            auxiliar2=lista.append(numero%10)
            auxiliar=auxiliar2
            numero = numero/10  
            digito=digito+1
        return lista
     
    def esNumeroFeliz(numero):
        listas=NumeroFeliz.obtenerDigitos(numero)
        suma=0
        listados=[]
        Repetido = False
        while suma!=1 and Repetido!=False:
            suma=0
            
            for x in range(len(listas)):
                suma=suma+ math.pow(listas[x],2)
                listas = NumeroFeliz.obtenerDigitos(suma)
                return suma
            if listas[x]==suma:
                Repetido = True
            else:
                listados.appdend(suma)
        if Repetido:
             return "No es un numero Feliz"
        else:
             return " es un numero feliz"
        
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado='es un numero feliz'
        valorObtenido=NumeroFeliz.esNumeroFeliz(623223)
        self.assertEqual(valorObtenido,valoresperado)                
if __name__ == "__main__":
# print(NumeroFeliz.esNumeroFeliz(623223)) 
 unittest.main()          
        