
#1.Create a class cal1 that will calculate sum of three numbers. Create setdata() method which has three parameters that contain numbers.Create display() method that will calculate sum and display sum
class cal1:
    def setData(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def display(self):
        d =  self.a + self.b + self.c
        print('Addition of 3 numbers is :', d)

c1=cal1()
c1.setData(20,40,10)
c1.display()


#2. Create a class cal2 that will calculate area of a circle. Create setdata() method that should take radius from the user. Create area() method that will calculate area . Create display() method that will display area .
class cal2:
    def setData(self,r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14

    def display(self):
        print("Area of circle is:", self.area())

c1=cal2()
c1.setData(int(input('Enter radius value: ')))
c1.area()
c1.display()


#3. Create a class cal3 that will calculate simple interest. Create constructor method which has three parameters .Create calInterest() method that will calculate Interest . Create display() method that will display Interest.
class cal3:
    def __init__(self,p,t,r):
        self.p=p
        self.t=t
        self.r=r
    def calInterest(self):
        return (self.p * self.t * self.r)/100

    def display(self):
        print("Simple Interest is:", self.calInterest())

c3=cal3(10000,5,5)
c3.calInterest()
c3.display()


#4. Create a class cal4 that will calculate square of a number. Create setdata() method which has one parameters that contain number. Create display() method that will calculate sum.(Function should return value)
class cal4:
    def setData(self,a):
        self.a=a


    def display(self):
        return self.a*self.a

c4=cal4()
c4.setData(6)
print(c4.display())



#5. Consider an employee class, which contains fields such as name and designation. And a subclass, which contains a field salary. Write a program for inheriting this relation.
class emp:

    def show(self,name,deg):
        self.name = name
        self.deg = deg
        print(f'Name is {name}')
        print(f'Designation is :{deg}')

class emp1(emp):
    def display(self,salary):
        self.salary=salary
        print(f'Salary is {salary}')

e = emp1()
e.show('Jagruti','Web developer')
e.display(70000)


#6. Create a class cal5 that will calculate area of a rectangle. Create constructor method which has two parameters .Create calArea() method that will calculate area of a rectangle. Create display() method that will display area of a rectangle.
class cal5():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length

    def area(self):
        return self.breadth*self.length

    def display(self):
        print('Area of Rectangle is: ', self.area())

obj=cal5(20,10)
obj.display()



#7. Create a class cal6 that will calculate area of a square. Create setdata() method that should take length from the user. Create area() method that will calculate area . Create display() method that will display area .
class cal6():
    def __init__(self,length):
        self.length=length

    def area(self):
        return self.length*self.length

    def display(self):
        print('Area of Square is: ', self.area())

a=int(input("Enter length of square: "))
obj=cal6(a)
obj.display()


#8. Write a program with use of inheritance: Define a class publisher that stores the name of the title. Derive two classes book and tape, which inherit publisher. Book class contains member data called page no and tape class contain time for playing. Define functions in the appropriate classes to get and print the details.
class Publisher:
    def __init__(self,name):
        self.name=name

class Book(Publisher):
    def __init__(self,name,no):
        Publisher.__init__(self,name)
        self.no = no

    def print(self):
        print("Book Details \n Title : ", self.name, "\n No of pages : ",self.no)

class Tape(Publisher):
    def __init__(self,name,playTime):
        Publisher.__init__(self,name)
        self.playTime=playTime

    def print(self):
        print("Tape Details \n Title : ", self.name, "\n Play Time : ", self.playTime, " hours")

b = Book("Think like a monk",300)
b.print()

t = Tape("Think like a monk",30)
t.print()


#9. Create a class called scheme with scheme_id, scheme_name,outgoing_rate, and message_charge. Derive customer class form scheme and include cust_id, name and mobile_no data.Define necessary functions to read and display data.
class Scheme:
    def __init__(self,id,name,rate,charge):
        self.id = id
        self.name=name
        self.rate=rate
        self.charge=charge

    def show(self):
        print('Scheme Id is:', self.id)
        print('Scheme Name is:', self.name)
        print('Scheme Rate is:', self.rate)
        print('Scheme Charge is:', self.charge)

class Customer(Scheme):
    def __init__(self,scheme_id,scheme_name,scheme_rate,scheme_charge,cust_id,cust_name , cust_no):
        Scheme.__init__(self,scheme_id,scheme_name,scheme_rate,scheme_charge)
        self.cust_id=cust_id
        self.cust_name=cust_name
        self.cust_no=cust_no

    def dis(self):
        Scheme.show(self)
        print('Customer id is: ',self.cust_id)
        print('Customer name is: ',self.cust_name)
        print('Phone number is: ',self.cust_no)

c1 = Customer(1,"WFH Pack","599","12","1001","Jagruti","9974896644")
c1.dis()


#10. Create a arith class. The class should have a parameterized constructor and methods to add, subtract and multiply two numbers and to return the answers.
class airth:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1-self.n2

    def mul(self):
        return self.n1*self.n2

a1=airth(30,10)
print('Addition is : ', a1.add())
print('Subtraction is : ', a1.sub())
print('Multiplication is : ', a1.mul())







