# There are two kinds of variable like instance and static variables.
# Instance variables can be changed with obj.
# But the class variables i.e. static variables does not change with the obj.
# If we define a variable inside __init__ it becomes a instance varible but at the same time 
# if we define a variable outside __init__ and inside the class it vbecomes class variable.
# Class variables are shared by all the obj.

class car:

    wheel=4

    def __init__(self,name,milage):
        self.name=name
        self.milage=milage

c1=car('BMW',20)
c2=car('Audi',30)
print(c1.name," ",c1.milage," ",c1.wheel)
print(c2.name," ",c2.milage," ",c2.wheel)
    