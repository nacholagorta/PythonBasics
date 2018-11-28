# Cálculo del sumatorio de la raíz de i desde un número a hasta un número b
# proporcionado por el usuario. Comprobar antes de calcular que 0<=a<=b
# i=b
# ∑√i
# i=a para a y b introducidos desde teclado., siendo 0<= a<=b
import math

a = int(input("ingresa primer número:\n"))
while a < 0:
    a = int(input("El número no puede ser negativo, prueba de nuevo: "))
b = int(input("ingresa segundo número:\n"))
while b < 0:
    b = int(input("El número no puede ser negativo, prueba de nuevo: "))

raizA = math.sqrt(a)
raizB = math.sqrt(b)
sumatorio = raizA + raizB

print (sumatorio)