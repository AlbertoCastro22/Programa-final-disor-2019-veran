#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:43:13 2019

@author: luisalbertocastroquevedo
"""
import DecimalToHexadecimal
import BinarioToDecimal
import Capicua
import unittest
class Mensajes:
    def textoAtras(texto):
        textoDecimal=str(texto)
        textoBinario=str(BinarioToDecimal.BinarioDecimal.binarioDos(int(texto)))
        textoHexadecimal=str(DecimalToHexadecimal.DecimalHexadecimal.hexa(int(texto)))
        Capicuas=Capicua.Capicua.NumeroCapicua(texto)
        textoCompleto='atrás: ' +textoDecimal+'\nBinario: '+textoBinario+'\nHexadecimal: '+textoHexadecimal+'\nCapicua: '+Capicuas
        return textoCompleto
    def textoSiguiente(texto):
        textoDecimal=str(texto)
        textoBinario=str(BinarioToDecimal.BinarioDecimal.binarioDos(int(texto)))
        textoHexadecimal=str(DecimalToHexadecimal.DecimalHexadecimal.hexa(int(texto)))
        Capicuas=Capicua.Capicua.NumeroCapicua(texto)
        textoCompleto='Siquiente: ' +textoDecimal+'\nBinario: '+textoBinario+'\nHexadecimal: '+textoHexadecimal+'\nCapicua: '+Capicuas
        return textoCompleto
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado='atrás: 22\nBinario: 10110\nHexadecimal: 16\nCapicua: el número 22 es capicúa'
        valorObtenido=Mensajes.textoAtras(22)
        self.assertEqual(valorObtenido,valoresperado)
 def test_dos(self):
        valoresperado= 'atrá[15 chars] 1011010\nHexadecimal: 5a\nCapicua: el número 90 no es capicúa'
        valorObtenido=Mensajes.textoAtras(90)
        self.assertEqual(valorObtenido,valoresperado) 
 def test_tres(self):
        valoresperado= 'atrás: 80\nBinario: 10110\nHexadecimal: 16\nCapicua: el número 80 no es capicúa'
        valorObtenido=Mensajes.textoSiguiente(80)
        self.assertEqual(valorObtenido,valoresperado)       
 if __name__ == "__main__":
  unittest.main()       
     
             