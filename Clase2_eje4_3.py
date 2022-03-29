hora= 23
minutos=58
segundo=59
segundo+=1
if segundo>=60:
    segundo=0
    minutos+=1
    if minutos>=60:
        minutos=0
        hora+=1
        if hora>=24:
            hora=0
print("La hora un segundo despues es",hora,"horas",minutos,"minutos",segundo,"segundos")