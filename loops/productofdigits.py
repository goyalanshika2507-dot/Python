i=int(input("enter no whose product you want"))
product=1
while i>1:
    product=product*(i%10)
    i=i//10
    print("product=",product)
