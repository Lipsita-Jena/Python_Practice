a=10 # global variable
print("outside a= ",a)

def myfun():
    a=20 #local variable
    a=21 # Here I am changing the global varibale
    print("Inside a= ",a)

    global b
    b=30
    print("Inside b= ",b)

    #Acessing the global variable a and changing the variable to 11
    globals()['a']=11
    print("Gloabl a = ",globals()['a'])

myfun()

print("Outside fun b= ",b) # Here we can access the variable b as it is globally declared
print("outside a= ",a)
