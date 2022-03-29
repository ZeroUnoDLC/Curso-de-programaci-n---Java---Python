from random import randint
def pesos(n):
    lista=[]
    for i in range(n):
        lista+=[randint(1,80)]
    return lista
def humanos(n):
    lista=[]
    for i in range(n):
        lista+=[i+1]
    return lista
#NUMERO DE HUMANOS
num=20
#INICIO CODIGO
Nave= pesos(num)
Humanos= humanos(num)
print(Nave)
print(Humanos)
