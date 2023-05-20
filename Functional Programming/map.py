# Adding +5 to the odd values

l1=[2,3,4,5,6,7]
odd=list(filter(lambda a: a%2!=0,l1))
print(odd)
res=list(map(lambda a:a+5,odd))
print(res)