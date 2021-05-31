'''
#SingleLevel Inheritance
class Admin:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  def show_msg(self):
      print('Parent class')

  def show(self):
    print(f'First name is {self.fname}. Last ame is {self.lname}')

class Student(Admin):
    def show_msg2(self):
        print('Child class')


s1 = Student('Jagruti', 'Rasne')
s1.show_msg()
s1.show()
s1.show_msg2()


#MultiLevel Inheritance
class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Add(cal):
    def add(self,c):
        self.c=c
        return self.a+self.b

class Sub(Add):
    def sub(self,d):
        self.d=d
        return self.c-d

c = Sub(10,20)
print('Addition', c.add(30))
print('Subtraction ', c.sub(10))


#Multiple Inheritance

class a:
    def fun(self):
        print('Parent a')

class b:
    def fun2(self):
        print('Parent b')

class c(a,b):
    def fun3(self):
        print('Child')

c1 = c()
c1.fun()
c1.fun2()
c1.fun3()


#Hierachical Inheritance
class Parent:
    def func1(self):
        print("This is a parent class.")


class Child1(Parent):
    def func2(self):
        print("This is child 1.")


class Child2(Parent):
    def func3(self):
        print("This is child 2.")


c1 = Child1()
c2 = Child2()
c1.func1()
c1.func2()
c2.func1()
c2.func3()
'''


class Parent:
    def func1(self):
        print("This is parent class.")


class Child1(Parent):
    def func2(self):
        print("This is child class-1. ")


class Child2(Parent):
    def func3(self):
        print("This is  student-2.")


class Child3(Child1, Parent):
    def func4(self):
        print("This is student-3.")


# Driver's code
c3 = Child3()
c3.func1()
c3.func2()

