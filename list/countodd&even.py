a=[]
b=int(input("enter the elements"))
for i in range(b):
    val=int(input("enter number"))
    a.append(val)
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("total even=",even_count,"total odd=",odd_count)