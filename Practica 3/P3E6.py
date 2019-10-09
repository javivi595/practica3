#P4E6 JAVIER DURAN Pide el precio y nombre de un producto 
#     y muestra lo que vale con el 21% de IVA

var=input("Introduce catalogo y precio: ").strip().split()
print("El precio con IVA de {} es de {:.2f} euros".format(var[0],(float(var[1])*1.21)))