from numpy import *;

arr=array([1,2,3,4])

# 1.Adding 5 to the array
arr+=5
print(arr)

# 2.Adding 2 arrays
arr2=array([2,3,4,5])
print(arr2+arr)

# 3.sum of arry
print(sum(arr))

# 4.min and max of array
print(min(arr),end=" ")
print(max(arr))

# 5. sort the array
print(arr.sort)

# 6. sin, cos, log of array
print(sin(arr))
print(cos(arr))
print(log(arr))

# 7. Concatenate 2 arrays
print(concatenate([arr,arr2]))
