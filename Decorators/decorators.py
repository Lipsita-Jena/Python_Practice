def div(a,b):
    print(a/b)
    return a/b

res=div(4,2)


# Let say you donoot have access to the div function and you want to apply an if condition in it.
# You can do this with the help of decorators.

def smart_div(fun): # This will take a function as argument.
    def inner(a,b): # We can write a func inside another func and this is the copy of the div 
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner

div=smart_div(div)
div(2,4)