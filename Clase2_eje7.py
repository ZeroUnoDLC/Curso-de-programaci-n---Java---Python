niveles=5
for i in range (niveles):
    for j in range (1,niveles-i):
        print ("  ",end="")
    for k in range (i*2+1):
        print("* ",end="")
    print()