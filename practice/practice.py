#even and odd
# num=int(input("enter the number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#sum of digits
# i=int(input("enter the number:"))
# sum=0
# while i>0:
#     sum=sum+i%10
#     i=i//10
# print("sum of digits",sum)

#palindrome
# i=int(input("enter the number:"))
# orig=i
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# if orig==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#fibonacci
# n=int(input("enter number:"))
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+

#multiplication
# n=int(input("enter the number"))
# for  i in range(1,11):
#     print(n,"X",i,"=",n*i)


#count the vowels:
# text=input("enter string")
# vowels="AEIOUaeiou"
# count=0
# for ch in text:
#     if ch in vowels:
#         count=count+1
# print("number of vowels",count)

#factorial by recursion
# def factorial(n):
#    if n==0 or n==1:
#       return 1
#    else:
#       return n*factorial(n-1)
# print("factorial",factorial(num))

#prime number
# def is_prime(n):
#     if n<=1:
#         print("not prime")
#     for i in range(2,n):
#         if n%i==0:
#             print("prime number",is_prime)
#     else:
#         print("not prime")
# n=int(input("enter  the number:"))

#palindrome in string
def is_palindrome():
    n=input("enter string")
    rev=n[::-1]
    if n==rev:
        print("palindrome string")
    else:
        print("not palindrome string")
is_palindrome()