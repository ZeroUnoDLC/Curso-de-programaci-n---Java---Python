def imp (n):
    if(n==1):
        print("La maquina saco piedra")
    elif(n==2):
        print("La maquina saco papel")
    elif(n==3):
        print("La maquina saco tijera")
def imp2(n):
    if(n==1):
        print("Sacaste piedra")
    elif(n==2):
        print("Sacaste papel")
    elif(n==3):
        print("Sacaste tijera")
from random import randint
win=0
winpc=0
while (winpc!=3 and win!=3):
    opUsuario=int(input("""Ingrese una opcion:
    1-piedra
    2-papel
    3-tijera
    :"""))
    opMaquina=randint(1,3)
    if (opUsuario<1 or opUsuario>3):
        print("Opcion no valida")
        continue
    imp2(opUsuario)
    imp(opMaquina)
    if((opUsuario==1 and opMaquina==3)or(opUsuario==2 and opMaquina==1)or(opUsuario==3 and opMaquina==1)):
        win+=1
        print("Ganador")
    elif(opUsuario==opMaquina):
        print("Empate")
    else:
        winpc+=1
        print("Que mal, perdiste")
    print("Veces que ganaste "+str(win))
    print("Veces que perdiste "+str(winpc))
if(opUsuario==3):
    print("Felicidades, ganador!")
else:
    print("Game over")
