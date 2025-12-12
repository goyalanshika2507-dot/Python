# 'f=open("myfile.txt",'r')
# data=f.read  #we can also give number so that it will read till that number only
# print(data')

# f=open('myfile.txt','w')
# f.write("hello  world")
# f.close()

f=open("myfile2.txt","r")
data=f.readline(66) #in output extra line will come so for that use "end"
print(data,end='')
