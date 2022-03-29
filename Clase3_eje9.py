from random import randint
def llenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista
def llenarAle(n):
    lista=[]
    for i in range(1,n+1):
        num=randint(1,n)
        while num in lista:
            num=randint(1,n)
        lista+=[num]
    return lista

listaB=llenarAle(10)
print(listaB)
listaA=llenarSec(10)
print(listaA)
for i in range (1,(len(listaB)//2)+1):
    print("A la persona",(listaB[i-1]),"le toca con",(listaB[(len(listaB))-i]))

