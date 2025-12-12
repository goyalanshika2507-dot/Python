def factorial(n):
    if(n==0 or n==1):
        return   #as factorial of 0 and 1 is 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(5))