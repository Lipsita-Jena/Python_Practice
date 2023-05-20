''' We can create n object of inner class inside the outer class or 
    outside outer class but wit the help of name of outer class'''

class Student:
    def __init__(self,name,roll) :
        self.name=name
        self.roll=roll
        self.lap=self.Laptop()
    
    def show(self):
        print(self.name," ",self.roll," ",self.lap.brand)

    # inner class
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.price=50000
        def show(self):
            print(self.brand," ",self.price)

s1=Student('Lipsita',20)
lap1=Student.Laptop()
lap1.show()
s1.show()