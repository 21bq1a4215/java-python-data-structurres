l=[]
x=int(input("Enter the size of the array:"))
print("Enter the elements:")
for k in range(x):l.append(int(input()))
key=int(input("Enter the element that u found:"))
for k in l:
    if key==k:
        print("Your  element found at position",l.index(k))
        break
else: print("The element not found anywhere !!")
         
