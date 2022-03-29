def imprimir(dic):
    for índice in dic:
        print("Key:",índice,"Value:",dic[índice])
def agregarEstudiante(dic, código, nombre):
    dic[código]=[]
    dic[código].append(nombre)
    dic[código].append([])
def agregarNota(dic,código,nota):
    dic[código][1] += [nota]
def prom(lista):
    suma=0
    for item in lista:
        suma+=item
    return suma/len(lista)
dic={}
imprimir(dic)
agregarEstudiante(dic,"001","Kevin")
agregarNota(dic,"001",10)
agregarNota(dic,"001",8)
imprimir(dic)
print(prom(dic["001"][1]))