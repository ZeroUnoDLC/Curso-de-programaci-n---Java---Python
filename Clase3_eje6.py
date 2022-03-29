lista1=[1,2,3,4,"a","b","c","d"]
while len(lista1)>0:
    print(lista1)
    elem= int(input("Ingrese la posicion del elemento a eliminar: "))
    if elem>len(lista1)-1:
        print("El elemento esta fuera del rango")
        continue
    del (lista1[elem])
