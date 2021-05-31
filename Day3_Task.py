
#1.Calculate avg of 5 Numbers
num = int(input('Numbers you want to enter:'))
sum = 0

for n in range(num):
    number = float(input('Enter number : '))
    sum += number

avg = sum / num
print('Average of ', num, ' numbers is :', avg)



#2.Check whether number is even or odd.
n = int(input('Enter number:'))

if n % 2 == 0:
    print(n, 'Number is even')
else:
    print(n, 'Number is odd')



#3.Take a year and check whether it is leap year or not

year = int(input('Enter year: '))

if year % 4 ==0:
    print(year, 'is Leap year')
else:
    print(year, 'is not leap year ')


#4.	Take a number and check whether it is zero, positive or negative.
n = int(input('Enter number:'))

if n==0:
    print('Entered number is zero')
elif n>=0:
    print('Entered number is positive')
else:
    print('Entered number is negative')


#5.	Take 2 numbers and display greatest number. (Also check equal number condition)

n1 = int(input('Enter 1st number'))
n2 = int(input('Enter 2nd number'))

if n1 > n2:
    print(n1, 'is greater than', n2)
elif n1 == n2:
    print('both are equal')
else:
    print(n2 ,'is greater than', n1)


#6.	Take a number and find factorial of that number.
num = int(input('Enter number:'))
fact=1

for n in range(1,num+1):
    fact *= n
print('Factorial of ', num, 'is', fact)


#7.	Write a program to swap 2 numbers using third variable.

n1 = int(input('Enter 1st number'))
n2 = int(input('Enter 2nd number'))

print('Before swapping: n1 is ', n1 ,' and n2 is ', n2)

temp = n2
n2 = n1
n1 = temp

print('After swapping')
print('Now n1 is ', n1)
print('Now n2 is ', n2)


#8.	Take 2 numbers and find smallest number.
n1 = int(input('Enter 1st number'))
n2 = int(input('Enter 2nd number'))

if n1 < n2:
    print(n1, 'is smallest')
else:
    print(n2, 'is smallest')


#9.	Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

n = int(input('Enter number:'))

if n < 100:
    print('number is less than 100')
    if n % 2 == 0:
        print(n, 'Number is even')
    else:
        print(n, 'Number is odd')

else:
    print('Number is not less than 100')


#10.	Take a number to print the square of a number if it is less than 10.

n = int(input('Enter number:'))

if n < 10:
    print('Number is less than 10')
    print('Square of ', n, 'is ', n ** 2)
else:
    print('Entered number is greater')



#11.	Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .
n = int(input('Enter number'))
if n < 1 :
    if n == 0:
        print('Entered number is zero')
    else:
        print('Entered number is negative')
else:
    print('Entered number is positive')


#12.	Take 3 numbers and find greatest number using nested IF….ELSE statement.

a = int(input('Enter 1st number'))
b = int(input('Enter 2nd number'))
c = int(input('Enter 3rd number'))

if a > b:
    if a > c:
        g = a
    else:
        g = c
else:
   if b > c:
       g = b
   else:
       g = c
print('Greatest is', g)

#13.	Take 3 numbers and find smallest number using logical operator.
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

smallest = 0

if a < b and a < c :
    smallest = a
elif b < c and b < c:
    smallest = b
else :
    smallest = c

print(smallest, "is the smallest of three numbers.")


#14.	Write a program to swap 2 numbers without taking third variable.

n1 = int(input('num 1'))
n2 = int(input('num 2'))

print('Before Number 1 is ', n1, 'Number 2 is', n2)
n1 , n2 = n2, n1
print('After:')
print(n1)
print(n2)



#15.	Take starting number and ending number from the user and print following series.

start = int(input('Enter start index'))
end = int(input('Enter ending index'))
counter = end

while start <= counter:
    print(counter)
    counter -=1

