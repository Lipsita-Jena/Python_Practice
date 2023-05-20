from array import *;
vals= array('i',[1,2,3])
print(vals)
print(vals.buffer_info)  #prints the address and size
print(vals.typecode) #prints the type like integer or long

#printing the array
for i in range(len(vals)):
    print(vals[i])

for val in vals:
    print(val)

#using while loop
i=0
while i<len(vals):
    print(vals[i])
    i+=1
    