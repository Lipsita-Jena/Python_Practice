class A:
    def feature1(self):
        print("Feature1 is working!")
    def feature2(self):
        print("Feature2 is working!")

class B(A):
    def feature3(self):
        print("Feature3 is working!")
    def feature4(self):
        print("Feature4 is working!")

obj=A()
#obj.feature1()
#obj.feature2()


obj1=B()
obj1.feature1()
obj1.feature2()
obj1.feature3()
obj1.feature4()

