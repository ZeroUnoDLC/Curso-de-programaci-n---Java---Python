año1=2001
año2=2022
r= "El rango de años requeridos entre "+str(año1)+" y "+str(año2)+" es: "
for i in range(año1,año2+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        r+=str(i)+", "
print(r)