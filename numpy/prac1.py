'''in numpy we acn work with single dimensional array as well as multidimensional
array. Here we don't need to mention the type of the array'''

'''There are 6 ways of creating the array in numpy'''

#1.array()

from numpy import *;
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)

#we can also specify the type of the arrays
arr1=array([1,2,3],float)
print(arr1) #[1. 2. 3.]