i=int(input("enter the number"))
orig=i
rev=0
while i>0:
    rev=(rev*10)+i%10
    i=i//10
if orig==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")