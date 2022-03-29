from random import randint
Zonausuario=4
Zonaportero= randint(1,6)
print("El portero saltó a la zona",Zonaportero)
if Zonausuario==Zonaportero:
    print(" EL JUGADOR NO ANOTÓ")
else:
    print("EL JUGADOR SI ANOTÓ!!!") 
    #randint(x,y)=entero
    #random()=numeros
    #radrange(x,y,z)=enteros
    #uniform(x,y)=flotantes