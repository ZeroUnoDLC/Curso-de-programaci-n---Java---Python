jornada=48
hTrabajadas= int(input("Ingrese las horas trabajadas: "))
pagoHora=2
pagoExtra=3.5
if hTrabajadas<=jornada:
    salario = hTrabajadas*pagoHora
else:
    salario = (hTrabajadas*pagoHora)+((hTrabajadas-jornada)*pagoExtra) 
print ("Su pago total es de: ",salario)   