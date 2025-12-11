a=[]
b=int(input("enter size of list:"))
for i in range(b):
    val=int(input("enter number:"))
    a.append(val)
print(a[::-1])