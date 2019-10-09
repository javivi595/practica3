#P4E2 JAVIER DURAN Imprime la velocidad media dada la distancia y el tiempo recorrido

km, horas= map(float,input("Introduce los kilometros recorridos y las horas que has necesitado: ").strip().split())
print("La velocidad media es {}km/h".format(km/horas))