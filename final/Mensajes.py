#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:43:13 2019

@author: luisalbertocastroquevedo
"""
import DecimalToHexadecimal
import BinarioToDecimal
import Capicua
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