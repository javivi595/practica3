#P4E7 JAVIER DURAN Pide una fecha, valida si es una fecha correcta y en caso 
#     de serlo le he añadido al ejercicio que cambie el mes alfabeticamente.

dia=int(input("Introduce un día:"))
mes=int(input("Introduce mes:"))
año=int(input("Introduce el año:"))
mesalpha={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
if mes>12 or año>2019 or(mes%2==0 and dia>=31 and mes<7) or (mes%2==1 and dia>=31 and mes>7):
    print("Fecha invalida")

else:
    print("La fecha seleccionada es {} de {} del año {}".format(dia,mesalpha[mes],año))