a=[]
b=int(input("enter how many numbers:"))
for i in range(b): #if we enter number 5 it will give program to 0-4 as indexing start from 0
   val=int(input("enter the values"))
   a.append(val)
   sum=0
   for i in a:
      sum+=i 
print("sum of list elements",sum)



