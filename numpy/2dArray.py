from numpy import *;
arr=array([
    [1,2,3,7,8,9],[4,5,6,9,8,7]
])
print(arr)
print(arr.dtype) # type of attribute int32
print(arr.ndim) # dimension of array =>2 
print(arr.shape) # number of rows and col => (2,3)
print(arr.size) #size of array 3*2
print(arr.flatten()) #flat the array from 2d-1d

arr1=arr.flatten()
print(arr1.reshape(3,4)) # 1d array to 3d array

# Creating a matrix from a 2-d array
a=array([
    [1,2,3],
    [4,5,6]
])
m=matrix(a)
print(m)
# They look similar but the only difference is that we can perform matrix operation here.

mat=matrix('1,2;3,4;5,6')
print(mat)
print(diagonal(mat))
print(mat.min())