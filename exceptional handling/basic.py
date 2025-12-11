# a=input("enter the number:")
# print(f'multiplication table of {a}is')
# try:
#     for i in range(1,11):
#        print(f"{int(a)}X{i}={int(a)*i}")
# except:
#     print("invalid input")

# print("some imp lines of code")
# print("end of program")

#isme try except tb use kiya jaata hai jb hume lage ki program humara glt yaa error aane vala hai toh try except use kiya jaata hai jisse output m likha ajaye ki vo wrong hai without an error hum aage ka agr ku  h print krwana ho tohh print ho jaaye
#syntax:
# try:
#     #statements which could generate exception
# except:
#     #solutions of generated exception

try:
   num=int(input("enter an integer"))
   a=[6,3]
   print(a[num])
except ValueError:
   print("number entered in not an integer")
except IndexError:
   print("Index Error")
   