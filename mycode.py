"""x = int(input('Enter 1st value'))

y = int(input('Enter 2nd value'))
z = (x+y)
print(z)"""

"""ch = input('Enter the char')[]
print(ch)"""

"""from array import *

arr = array('i',[])
n = int (input("Enter the lenth of array"))
for i in range(n):
    x = int(input("Next value"))
    arr.append(x)

print(arr)"""


"""def sum():

    a = int(input("Enter 1st number"))
    b = int(input("Enter 2nd number"))

    c = a+b
    print("Sum is:",c)

sum()"""

"""def add_sum(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c,d,e,f


x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))

R1,R2,R3,R4 =  add_sum(x,y)
print(R1,R2,R3,R4)"""

"""Factorial Code"""

"""def fact(n):

    if n == 0:
        return 1

    return n * fact(n - 1)

a = int(input("Enter number:"))

result = fact(a)
print(result)"""

"""sum = lambda a, b: a+b;
print ("Value of total : ", sum(10, 20))
print ("Value of total : ", sum(20,20))"""

"""input = int(input("Enter Number"))
if input%2 == 0:
    print("Input is Even Number: ")
else:
    print("Input is odd Number:")"""


"""class SimpleInterest:

    def SimpleInterest(self):
        Principle = int(input("Enter The Principle Amount: "))
        Rate = int(input("Enter The Rate: "))
        Time = int(input("Enter The Time: "))

        SI = (Principle * Rate * Time) / 100
        print("Simple Intrest is:",SI)

class CompoundInterest:

    def CompoundInterest(self):
        Principle = int(input("Enter The Principle Amount: "))
        Rate = int(input("Enter The Rate: "))
        Time = int(input("Enter The Time: "))

        CI = Principle * (pow((1 + Rate / 100), Time))
        print("Compound Interest is:",CI)

S = SimpleInterest()
C = CompoundInterest()

print("1 For SimpleInterest")
print("2 For CompoundInterest")

A = int(input("Enter Your Selection: "))
if A == 1:
    S.SimpleInterest()
elif A == 2:
    C.CompoundInterest()"""

"""A = [10,20,30]
B = [40,50,60]
sum = sum(A)+sum(B)
print("Total is:",sum)"""

a = open("AAA",'r')
print(type(a))
print(content)




