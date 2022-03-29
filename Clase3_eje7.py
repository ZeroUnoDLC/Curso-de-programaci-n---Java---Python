a=[1,3,5,7,1,8,5]
print(a)
for i in range((len(a)-1),-1,-1):
    if a[i]in a[:i]:
        del (a[i])
print(a)