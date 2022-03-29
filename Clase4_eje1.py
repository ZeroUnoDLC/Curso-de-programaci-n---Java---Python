def imprimir(tabla):
    for i in range (len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],",",end="")
        print("]")
def llenarSecuencial(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[(j+1)+i*len(tabla)]
    return tabla
tabla =llenarSecuencial(5)
imprimir(tabla)