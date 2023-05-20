#Copying one array to another

from array import *;
arr=array('i',[1,2,3])
newarr=array(arr.typecode, (a for a in arr))
for i in newarr:
    print(i,end=" ")