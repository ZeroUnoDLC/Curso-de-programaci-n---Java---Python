saldo=500
eleccion=0
while (eleccion!=3):
    eleccion= int(input("""BIENVENIDO, POR FAVOR ESCOJA UNA OPCION
    1- Retiro
    2- Deposito
    3- Salir
    : """))
    print("----------------------------------------------------")
    if(eleccion>3 or eleccion<1):
        print("Opcion no valida")
        continue
    elif(eleccion==1):
        retiro=float(input("Ingrese la cantidad a retirar: "))
        if saldo-retiro<0:
            print("No tiene fondos suficientes")
        else:
            saldo=saldo-retiro
        print("------------------------------------")
    elif(eleccion==2):
        deposito=float(input("Ingrese la cantidad a depositar: "))
        saldo=saldo+deposito
        print("------------------------------------")
    print("Su saldo actual es de $"+str(saldo))