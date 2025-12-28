# def double(x):
#     return x*2
# print(double(5))
#now by using lambda function
# double=lambda x:x*2
# cube=lambda x: x*x*x
# # avg=lambda x,y: (x+y)/2 #can take more than 2 values also
# # print(double(5)) #function to double the input
# # print(cube(4))
# # print(avg(4,7))

# #we can also give function in function
# def appl(fx,value):
#     print(appl(cube,3))

#map,filter and reduce
#def cube(l):
   l=[1,2,3,4,5]
#    newl=list(map(cube,l)) #give result through list
# print(newl)
#instead of using cube we can use lambda function also as lambda x:x*x*x

# L=[1,2,3,4,5]
# def filter_function(a):
#    return a>4
# new_list=list(filter(filter_function,L))#greater than 4 elements will obtain
# print(new_list)

numbers=[1,2,3,3]
numbers=[1,2,3,5]
def mysum(x,y):
   return x+y
sum=reduce(mysum,numbers)
print(sum)




