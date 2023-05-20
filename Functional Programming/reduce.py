# reduce the value to only a single value no list is displayed in the output
# It is present in functools module

from functools import reduce
num=[1,2,3]
sum=reduce(lambda a,b: a+b,num)
print(sum)