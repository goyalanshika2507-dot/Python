a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
e=int(input("enter fifth number"))
total=a+b+c+d+e
percentage= (total/500)*100
print("total marks=",total,"percentage",percentage)
if percentage>=80:
    print("grade A")
elif percentage>=60:
    print("grade B")
elif percentage>=40:
    print("grade C")
else:
    print("grade D")