
import BinarioToDecimal
import unittest
import DecimalToHexadecimal
import Capicua
class SerieFibonacci:
 def fib(variablePedida):
  if variablePedida < 2:
   return variablePedida
  else:    
   return SerieFibonacci.fib(variablePedida-1) + SerieFibonacci.fib(variablePedida-2)
 contador=0  
 def siguiente(): 
  auxiliar=SerieFibonacci.fib(SerieFibonacci.contador)
  SerieFibonacci.contador=SerieFibonacci.contador+1
  return auxiliar
 
 def retroceder(): 
  try:
   auxiliar=SerieFibonacci.fib(SerieFibonacci.contador-1)
   if auxiliar>=0:
      SerieFibonacci.contador=SerieFibonacci.contador-1
      return auxiliar
   else:
      auxiliar=None
      return auxiliar
  except NameError:
      print()
  
class Test(unittest.TestCase):
 def test_sum(self):
        valoresperado=21
        SerieFibonacci.siguiente()
        SerieFibonacci.siguiente()
        SerieFibonacci.retroceder()
        SerieFibonacci.retroceder()
        SerieFibonacci.retroceder()
        SerieFibonacci.retroceder()
        valorObtenido=SerieFibonacci.retroceder()
        self.assertEqual(valorObtenido,valoresperado)
 def test_sumd(self):
        binario=BinarioToDecimal.BinarioDecimal
        valoresperado=89 
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        valorobtenido=SerieFibonacci.siguiente()
        self.assertEqual(valorobtenido,valoresperado)
 def test_tres(self):
        binario=BinarioToDecimal.BinarioDecimal
        valoresperado=17711
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        valorobtenido=SerieFibonacci.siguiente()
        self.assertEqual(valorobtenido,valoresperado)
 def test_cuatro(self):
        binario=BinarioToDecimal.BinarioDecimal
        valoresperado=89 
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())       
        valorobtenido=SerieFibonacci.retroceder()
        self.assertEqual(valorobtenido,valoresperado)
 def test_cinco(self):
        binario=BinarioToDecimal.BinarioDecimal
        valoresperado=144
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        valorobtenido=SerieFibonacci.retroceder()
        self.assertEqual(valorobtenido,valoresperado)
 def test_seis(self):
        binario=BinarioToDecimal.BinarioDecimal
        valoresperado=110111
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.siguiente())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())
        binario.binarioDos( SerieFibonacci.retroceder())       
        valorobtenido=binario.binarioDos( SerieFibonacci.retroceder())
        self.assertEqual(valorobtenido,valoresperado)
 def test_siete(self):
        valoresperado='59'
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.siguiente())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        valorobtenido=DecimalToHexadecimal.DecimalHexadecimal.hexa( SerieFibonacci.retroceder())
        self.assertEqual(valorobtenido,valoresperado)        
 if __name__ == "__main__":
  unittest.main()       
     
     
    
    

