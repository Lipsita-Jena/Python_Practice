from numpy import *;

arr=array([1,2,3])
print(arr)

# copying the arr -> arr2
arr2=arr
print(arr2)

# printing the address of both the arrys -Here both the address are same
print(id(arr))
print(id(arr2))

# Copying the arr ->arr3 but this time they have differenet address
# But again this is an example of shallow copy that means if we change the value of arr it will also be reflected in arr3
arr3=arr.view()
print(arr3)
print(id(arr))
print(id(arr3))
arr[1]=7
print(arr3)
print(arr)

# But in case of deep copy we want the two array should not be linked in any way
arr4=arr.copy()
print(arr)
arr[1]=9
print(arr)
print(arr4)