lista= [80,34,80,23,70]
comparador=0
for i in range((len(lista)-1)):
    for j in range(len(lista)):
        if((lista[i]+lista[j])<=150)and(lista[i]!=lista[j])and(j!=(i-1)):
            print("Peso de "+str(lista[i])+" + "+str(lista[j])+" = "+str(lista[i]+lista[j]))
            if (comparador<(lista[i]+lista[j])):
                comparador=(lista[i]+lista[j])
print("El peso maximo posible es de ",comparador)