l=[]
n=int(input("enter the elements"))
for i in range(n):
    val=int(input("enter the values"))
    l.append(val)
largest=max(l)
print("largest element is",largest)