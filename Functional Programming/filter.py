# Filter takes two args one is afunction and another is iterable i.e list, array

def fun(n):
    return n%2==0

num=[2,3,5,6,7,8]
even=list(filter(fun,num))
print(even)

# with lambda

l1=[2,3,4,5,6,6,9,6,4]
even=list(filter(lambda a:a%2==0,l1))
print(even)

# Here lambda a: This is the args
# a%2 ==0 :This is the return val

l1=[2,3,4,5,6,6,9,6,4]
even=list(filter(lambda a:a+2,l1))
print(even)

# Filter works for only true false
# You can't do any operation on it