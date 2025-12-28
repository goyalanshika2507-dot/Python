import numpy as np
x=[1,2,3,4]
print(x)
ar=np.array(x)
print(ar)
print(type(ar))
print(ar.ndim) #tells the dimension of array
#ar was 1-d array
#2-d array
ar1=np.array([[1,2,3,4],[1,2,3,4]])
print(ar1)
print(ar1.ndim)
#3-d array
ar2=np.array([[[2,5,5],[1,5,6],[4,7,6]]])
print(ar2)
print(ar2.ndim)
arn=np.array([1,2,3,4],ndmin=10) #to create multidimensional array
print(arn)
print(arn.ndim)
print(ar2.dtype) #give data type
print(ar2.shape)#tells shape of array 
print(ar2.size)#tells size of array

rng=np.arange(1,6) #creates array with values from 1 to 5
print(rng)
lspace=np.linspace(1,50,10)#creates array with 10 values from 1 to 50 with equal interval
print(lspace)
emp=np.empty((4,6))#creates empty array of shape 4x6
print(emp)
ide=np.identity(45)#create empty matrix 
print(ide)
arr=np.arange(99)#creates array with values from 0 to 98
print(arr.reshape(3,33))
print(ar2.sum(axis=0))#sum of coloumn
print(ar2.sum(axis=1))#sum of rows
print(ar2.T)#transpose the array
for i in ar2.flat:
    print(i)
print(ar2.size)#returns the size of the array
print(ar2.nbytes)#returns the total bytes pf data present in the array
arr2=np.array([1,26,387,71])
print(arr2.argmax())#returns the index where the maximum value is present
print(ar2.argmin())#returns the index where the minimum value is present
print(ar2.argsort())#returns the index for the increasing order of value where they are present