
def stu():
    print('Hey there!')
# calling function
stu()


# with argument
def stu(name, id):
    print('Name is:', name)
    print('Your id is: ', id)


stu('Jagruti', 101)


# Using return
def stu():
    name = 'Jagruti'
    id = 101
    return name, id


name, id = stu()
print('Name is:', name)
print('Your id is:', id)



#Types of Function Argument
#Default Argument
def sub(name='python',sub_code=101):
    print('Subject is: ', name)
    print('Subject code is:', sub_code)

sub(name='Ajp', sub_code=102 )
sub()


#Keyword Argument
def sum(*kw):
    sum = 0

    for i in kw:
        sum+=i
    print(sum)

sum(10, 20, 30)

#Keyword Argument

def emp(**info):
    for i , j in info.items():
        print(i, 'is:' , j)

emp(name='Jagu', id = 101, department = 'CS')
emp(name='Ronak', id = 102, department = 'IT')


#Scope of a Variable

def scope():
    name='Jagruti'
    print('Locala variable name:', name)

scope()
name='Shweta'
print('Global variable name:', name)