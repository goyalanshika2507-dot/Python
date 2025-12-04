i=int(input("enter the number of which you want the sum"))
sum=0
while i>0:
   sum=sum+i%10
   i=i//10
print("sum of digits",sum)

#sum of square
i=int(input("enter number whose sum you want"))
sum=0
while i>0:
   sum=sum+(i%10)*(i%10)
   i=i//10
   print("sum=",sum)
