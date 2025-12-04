# # a=int(input("enter first 10 natural number"))
# while a<=10:
#     print(a)
#     a=a-1
# a=10
# while True:
#     a=a-1
#     if a==0:
#         break
#     print(a)   
a=10
while a>0:
    print(a)
    a=a-1

#reverse the digit
i=int(input("enter the number:"))
rev=0
while i>0:
    rev=(rev*10)+i%10
    i=i//10
    print("reverse=",rev)
            