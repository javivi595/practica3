#P4E5 JAVIER DURAN Pide un numero de 3 cifras y que devuelva error si es mayor

num=int(input("Introduce un numero de tres crifras: "))
if num>=1000:
    print("ERROR: El numero {} tiene más de tres cifras".format(num))
else:
    print("Tu numero es {}".format(num))