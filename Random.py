from pip._vendor.distlib.compat import raw_input
from random import randint

acabar = True
random = randint(1, 100)
while acabar:
    x = raw_input ("Introduzca un numero: ")

    xint = int(x)
    if random == xint:
        print("Enhorabuena era ",random)
        acabar = False

    elif random > xint:
      print("El numero es mayor, prueba de nuevo.")
    elif random < xint:
      print("El numero es menor, prueba de nuevo.")


