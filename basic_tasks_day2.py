#Print function
print("Hello world")
print('Hello world')
print('''

Hello world
Python Programming

''')

#Variable Declaration and Initialization
a = 10
b = 'Jagruti'
c = 18.9
print(a)
print('Name is : ', b)
print(c)

#Changing the value of a variable
b = 'Python Programming'
print('Name is ',b)


#Multiple Values to Multiple Variables
x , y, z = 1 ,2 ,3
print(x , y, z)

#Same value to multiple variables
j=k=l = 10
print(j)
print(j , k, l)

#Data Type

#Number Data type
n1 = 16
n2 = 19.8
n3 = 1 + 2j

#Type() Function
print(n1 , 'is of type' , type(n1))
print(b, 'is of type' ,type(b))

#isinstance() Fuction
print(n2, 'is float number?' , isinstance(n2, float))
print('is', n3, 'Complex number? ', isinstance(n3,complex))



#String
str1 = 'Python Programming'
print(str1 * 3)
print(str1 + ' Language')  # String to string concat with + operator
print(str1[0])             #return 0th index
print(str1[0:])            #return complete string
print(str1[::-1])          #return reverse string
print(str1[2:8])           #return 2nd to 8th index character
print(len(str1))           #string length



#List Mutable
l1 = [1, 2, 3, 4, 'python']

print(l1)
print(type(l1))
print(l1[1])
print(l1[2:5])
print(l1[::-1])
l1.append('Programming')
print(l1)
print(l1[1:])


#Tuple Immutable
t1 = (2, 3, 4, 2, 5, 1, 'Django')
print(t1)
print(t1[1:])
print(t1[2:6])
print(t1[4])
print(t1.count(2))


#Dictnory
d1 = {'name': 'Jagruti', 'age': 20, 10: 'Id'}
print(d1)
print(d1['name'])
print(d1[1])
print(d1.values())
print(d1.keys())
print(d1.items())
