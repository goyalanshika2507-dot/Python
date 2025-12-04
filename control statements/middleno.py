a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if (a>b and a<c)or(a<b and a>c):
    print("middle number=",a)
elif(b>a and b<c) or (b<a and b>c):
    print("middle number=",b)
else:
    print("middle number=",c)