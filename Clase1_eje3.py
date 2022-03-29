x= int (input("Ingrese el numero de dias que lleva vivo :D"))
a= x//365
m= (x%365)//30
s= (x-(a*365+m*30))//7
x=x-(a*365+m*30+s*7)
print("Usted lleva vivo",a,"años",m,"meses",s,"semanas",x,"días")