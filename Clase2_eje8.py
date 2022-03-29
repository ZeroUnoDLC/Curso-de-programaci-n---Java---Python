frase= "Hola mi vida, hola mi cielo, hola mi gran amor"
letra= "o"
contador=0
for i in frase:
    if letra== i:
        contador+=1
if contador==0:
    print ("No se encontró la letra ´"+letra+"´")
else:
    print("La letra ´"+letra+"´ se encontró "+str(contador)+" veces")
