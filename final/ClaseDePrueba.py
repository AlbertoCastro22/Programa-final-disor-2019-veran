#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 12:26:35 2019

@author: luisalbertocastroquevedo
"""
import fib3
import Padovan
import NumeroSuerte
import Mensajes
import Ulam

class Prueba:
    def atrasTodos():
        mensajeFibonacci="\nNumero Fibonacci\n"+Mensajes.Mensajes.textoAtras(fib3.SerieFibonacci.retroceder())
        mensajePadovan="\nNumero Padovan\n"+Mensajes.Mensajes.textoAtras(Padovan.Padovan.retroceder())
        mensajedeLaSuerte="\nNumero de la Suerte\n"+Mensajes.Mensajes.textoAtras(NumeroSuerte.NumeroSuerte.retroceder())
        mensajeUlam="\nNumero Ulam\n"+Mensajes.Mensajes.textoAtras(Ulam.NumeroUlam.retroceder())
        uniontodos=mensajeFibonacci+mensajePadovan+mensajedeLaSuerte+mensajeUlam
        return uniontodos
    def SiguienteFiboNacci():
        cadenaSiguiente="\nNumero Fibonacci\n"+Mensajes.Mensajes.textoSiguiente(fib3.SerieFibonacci.siguiente())
        return cadenaSiguiente
    def SiguientePadovan():
        cadenaSiguiente="\nNumero Padovan\n"+Mensajes.Mensajes.textoSiguiente(Padovan.Padovan.Siguiente())
        return cadenaSiguiente
    def SiguienteSuerte():
        cadenaSiguiente="\nNumero de la Suerte\n"+Mensajes.Mensajes.textoSiguiente(Padovan.Padovan.Siguiente())
        return cadenaSiguiente
    def SiguienteUlam():
        cadenaSiguiente="\nNumero Ulam\n"+Mensajes.Mensajes.textoSiguiente(Ulam.NumeroUlam.Siguiente())
        return cadenaSiguiente
    
        
        
if __name__ == "__main__":
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())  
 print(Prueba.SiguienteFiboNacci())  
 print(Prueba.SiguienteFiboNacci())  
 print(Prueba.SiguienteFiboNacci())  
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci())
 print(Prueba.SiguienteFiboNacci()) 
 print("---------------------------------------------------------------------")
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())
 print(Prueba.SiguientePadovan())  
 print("---------------------------------------------------------------------")
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print(Prueba.SiguienteUlam())
 print("---------------------------------------------------------------------")
 print(Prueba.SiguienteSuerte())
 print(Prueba.SiguienteSuerte())
 print(Prueba.SiguienteSuerte())
 print(Prueba.SiguienteSuerte())
 print(Prueba.SiguienteSuerte())
 print(Prueba.SiguienteSuerte())
 print("---------------------------------------------------------------------")
 print("\nAtras todos")
 print(Prueba.atrasTodos())
 print(Prueba.atrasTodos())
 print(Prueba.atrasTodos())
 print(Prueba.atrasTodos())

         
#    
        
        
        