import numpy as np
x=[1,2,3,4]
print(x)
ar=np.array(x)
print(ar)
ar1=np.array([1,2,3,4,5])
print(ar1)
ar1
print(type(ar1))#tells the type of ar1
print(ar1.ndim)#tells the dimension of array
# ar1 was 1-d array
ar2=np.array([[1,2,3,4],[1,2,3,4]])#2-d array
print(ar2)
print(ar2.ndim)
#ar2 is 2-D array
ar3=np.array([[[1,2,3,4], [1,2,3,4], [1,2,3,4]]])#3-d array
print(ar3)
print(ar3.ndim)
#ar3 is 3-D array
arn=np.array([1,2,3,4], ndmin=10)# to create multidimensional array
print(arn)
print(arn.ndim)
print(ar3.dtype)
print(ar3.shape)#tells the shape of array
print(ar3.size)#tells the size of array
rng=np.arange(1,6)#creates array with values from 1 to 5
print(rng)
lspace=np.linspace(1,50,10)#creates array with 10 values from 1 to 50 with equal interval
print(lspace)
emp=np.empty((4,6))#creates empty array of shape 4x6
print(emp)
ide=np.identity(45)#creates identity matrix of order 45
print(ide)
arr=np.arange(99)#creates array with values from 0 to 98
print(arr.reshape(3,33))
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.sum(axis=0))#sums the columns
print(arr1.sum(axis=1))#sums the rows
print(arr1.T)#transpose the array
for i in arr1.flat:
    print(i)
print(arr1.size)#returns the size of the array
print(arr1.nbytes)#returns the total bytes pf data present in the array
arr2=np.array([1,26,387,71])
print(arr2.argmax())#returns the index where the maximum value is present
print(arr2.argmin())#returns the index where the minimum value is present
print(arr2.argsort())#returns the index for the increasing order of value where they are present