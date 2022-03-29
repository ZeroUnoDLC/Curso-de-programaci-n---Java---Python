dic= {}
indice = "nombre"
valor = "kevin"
dic[indice]=valor
#dic.setdefault(indice,valor)
print(dic)

menu= True
while menu:
    op = int(input("""Elija una opcion
    1.- Agregar
    2.- Salir
    : """))
    if op==1:
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor: ")
        dic[indice]=valor
        print(dic)
    elif op==2:
        menu=False
    else:
        print("Escoja una opcion valida")