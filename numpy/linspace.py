#2. arrsy using linspace
# Here the range is included and it divides the array into different parts that is specified by the third value.
#the difference between the number are same

from numpy import *;
arr=linspace(0,15,20) #this will divide the array into 20 parts but within the range that is 15
print(arr)

arr1=linspace(0,15) #the default part is 50
print(arr1)