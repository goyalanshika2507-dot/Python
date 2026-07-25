try:
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    print("division=",x/y)
except ValueError:
    print("enter numbers only")
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("program executed successfully")
