lista= ["a","b","c","d","e"]
print(lista)
lista2=["e","f","c","d"]
print(lista2)
listatodo=lista+lista2
print(listatodo)
lambas=[]
lsolo1=[]
lsolo2=[]
for palabra in lista:
    if palabra in lista2:
        lambas=lambas+[palabra]
    else:
        lsolo1=lsolo1+[palabra]
for palabra in lista2:
    if palabra not in lista:
        lsolo2= lsolo2+[palabra]
print(lambas)
print(lsolo1)
print(lsolo2)