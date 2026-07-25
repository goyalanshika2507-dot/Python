try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    result=a/b
    print("result=",result)
except ZeroDivisionError:
    print("error!division by zero is not allowed")