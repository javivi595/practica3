#P4E4 JAVIER DURAN Introduce 3 notas y imprime la media

a, b, c=map(float,input("Introduce 3 notas separadas por espacio: ").strip().split())
print("La media es {:.2f}.".format((a+b+c)/3))