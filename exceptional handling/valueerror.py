try:
    a=int(input("enter a number"))
    print("num you entered",a)
except ValueError:
    print("invalid input!please enter valid integer")