''' There are 3 kinds of methods :- Instance , static and class
.Instance method use self within it and change with every object.
.Instance methods are also of two types:- 1) Getter also called as Accessor
                                          2) Setter also called as Mutators

Class Method:-
- This can be used only with @classMethod Decorator.
- Here te value does not get changed with the obj and remin the same for all the obj.
- It can be called with the name of the class.     
- Here we use cls as the keyword.                             
                                         
Static Method:-
- The method work with @staticmethod Decorator
- Here neither we specify self nor cls.
- This is the method that has to be called any how nothing to do with class and obj.
- They are just like normal method.

                                            
                                              '''

class Student:

    school='SOA Univercity' # class variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_m1(self):
        return self.m1
    
    def set_m1(self,val):
        self.m1=val

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school # Like we use self for instance variable, we use cls for class variables
    
    @staticmethod
    def staticinfo():
        print("Hey I am static method")

S1=Student(22,34,56)
print(S1.avg())
print(S1.info())

print("class method ",Student.info()) #This will throw you an error if you will not use @classMethod decorator
print(Student.staticinfo())

