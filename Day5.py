
class student:
    def info(self):
        print('OOPs Concept')

    #DefaultConstructor
    def __init__(self):
        print('Default Constructer')


s=student()
s.info()


class student:
    def info(self):
        print('OOPs Concept')

    # ParameterizedConstructor
    def __init__(self,n):
        print('Name is: ', n)


s = student('Jagruti')
s.info()


#Polymorphism
#Method Overloading

class student:
    def info(self,name):
        self.name=name
        print('Method 1')

    def info(self,age):
        self.age=age
        print('Method 2')



s = student()
s.info('Jagruti')
s.info(20)

#Method Overriding
class A:

    def fun1(self):
        print('class A method-1')

    def fun2(self):
        print('class A method-2')


class B(A):

    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Method overriding ')

    def fun3(self):
        print('class B')


obj = B()
obj.fun1()
obj.fun2()
obj.fun3()

