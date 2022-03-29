from random import randint
def imprimir(tabla):
    for i in tabla:
        print("[",end="")
        for j in i:
            print("%3s"%j,",",end="")
        print(" ]")
def llenarVacio(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        columnas=randint(1,10)
        for j in range(columnas):
            tabla[i]+=[randint(1,10)]
    return tabla
tabla= llenarVacio(5)
imprimir(tabla)