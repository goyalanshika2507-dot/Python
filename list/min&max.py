#USING PRE-DEFINED FUNCTION:-
a=[]
b=int(input("enter size of list:")) 
for i in range(b):
     val=int(input("enter number:"))
     a.append(val)
#     _min=min(a)
#     _max=max(a)
# print("min number:",_min)
# print("max number:",_max) 

#USING USE-DEFINED FUCNTION:-
max=a[0]
for i in a:
     if i>max:
          max=i
print("max number:",max)

#to find second max and mix use remove function and remove min and max number