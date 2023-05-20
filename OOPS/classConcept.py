class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def display(self):
        print(self.cpu," ",self.ram)

Comp1=Computer('i5','8GB')
Comp1.display()

# __init__ is a special method that is called automaticaly.
# It is just like the constructor of java
# self is the reference of the object that is passed automaticaky and is like 'this' in Java