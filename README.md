# java-python-data-structurres
#bubble_sorting 
l=[2,1,3,5,4]
for m in range(len(l)-1):
    for k in range(1,len(l)-m):
        if l[k-1]>l[k]:l[k],l[k-1]=l[k-1],l[k]
print(l)
