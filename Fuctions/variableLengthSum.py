def sum(a,*b):
    print(a)
    print(b) # Here b acts as a tuple hence we have ti iterate it
    s=a
    for i in b:
        s+=i
    print("Sum=",s)

sum(2,3)
sum(4,5,6)