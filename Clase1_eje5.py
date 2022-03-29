from tarfile import PAX_FIELDS


x=int(input("Ingrese el numero de aciertos"))
y=int(input("Ingrese el numero de errores"))
total=x+y
px=(100/total)*x
py=(100/total)*y
print("Su puntaje final fue: "+str(x)+"/"+str(total))
print("Su porcentaje de aciertos es de: %.2f"%px,"%")
print("Su porcentaje de errores es de: %.2f"%py,"%")
