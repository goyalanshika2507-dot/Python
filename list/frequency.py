a=[]
b=int(input("enter size of list:"))
for  i in range(b):
    val=int(input("enter number:"))
    a.append(val)
key=int(input("enter number to find frequency:"))
count=0
for i in range(b) :
    if (a[i]==key):
        count+=1
print("frequency=",count)