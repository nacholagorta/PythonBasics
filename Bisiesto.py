
year =int(input("ingresa año\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año " , str(year), " es bisiesto")

else:
    print("El año " , str(year), " no es bisiesto")