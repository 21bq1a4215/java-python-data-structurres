# java-python-data-structurres
#bubble_sorting 
l=[2,1,3,5,4]
for m in range(len(l)-1):
    for k in range(1,len(l)-m):
        if l[k-1]>l[k]:l[k],l[k-1]=l[k-1],l[k]
print(l)



#selection sorting 
l=[455,565,54,54,95,95,654,53,54,654,64,5,55,4665,564,6,65]
for i in range(1,len(l)):
    if l[i-1]>l[i]:
        l[i-1],l[i]=l[i],l[i-1]
        print(l)
        for j in range(i-1,-1,-1):
            if  l[j] < l[j-1]: l[j],l[j-1] =l[j-1],l[j]
            print(l)
#l[-1],l[0]=l[0],l[-1]
print(l)
