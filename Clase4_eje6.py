def imprimir (dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])
dic= {}
dic["pan"]=.12
dic["queso"]=.80
menu= True
while menu:
    op = int(input("""Elija una opcion
    1.- Agregar producto
    2.- Facturar
    3.- Salir
    : """))
    if op==1:
        indice = input("Ingrese el indice: ")
        valor = float(input("Ingrese el valor: "))
        dic[indice]=valor
        print(dic)
    elif op==2:
        total=0
        factura= True
        while factura:
            imprimir(dic)
            op2 = int(input("""Elija una opcion
            1.- Agregar a Factura
            2.- Finalizar
            : """))
            if op2==1:
                indice = input("Ingrese el indice: ")
                cantidad = int(input("Ingrese el valor: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado")
                else:
                    total += (dic.get(indice)*cantidad)
                    print("El total es:",total)
            else:
                factura=False
                total=0
    elif op==3:
        menu=False
    else:
        print("Escoja una opcion valida")