"""String codes"""


"""String = "Hello Welcome in automation"
print(len(String))"""

"""String = "Hello Welcome in automation"
appearance = {}

for i in String:
    if i in appearance:
        appearance[i] += 1
    else:
        appearance[i] = 1
print("Appearance of Each is: "+str(appearance))"""

"""import re
String = "Hello Welcome in automation"
print(String)
res = re.findall("Welcome",String)
print(res)"""

"""String = "Batty brought butter but the butter was bitter so batty brought better butter"
#print(String.find("butter"))
#res = String[14:20]
res = String.replace("butter","BUTTERS",1)
print(res)"""

"""def reverce(String):
    str = ""
    for i in String:
        str = i + str
    return str

String = input("Enter plz:")

print("Original String is:"+String)
print("Reverce String is:",reverce(String))"""


"""String = "Pune is a city"
index = String.find("city")
print(String[:index] + "beautiful " + String[index:])"""


"""String = "BHASHKAR"
if String == String.upper():
    print(String.lower())
else:
    print(String.upper())"""

"""String = "A quick brown cat jumps over the lazy dog"
print(String.replace("cat","fox"))"""



"""List codes"""

"""List = [11,17,31,3,11,17]
print(len(List))
print(List.count(11))
print(List.__sizeof__())
List.append(22)
print(List)"""

"""from collections import OrderedDict
List = [11,17,31,3,11,17]
List.sort()
print(List)
List.remove(3)
print(List)
print(list(OrderedDict.fromkeys(List))"""


"""def largest(List):
    lenght = len(List)
    List.sort()
    print("Largest Element in the List : ",List[lenght-1])

def smallest(List):
    lenght = len(List)
    List.sort()
    print("Smallest Element in the List :",List[0])

List = [11,12,13,14,15,16,17]
Largest = largest(List)
Smallest = smallest(List)"""

"""List1 = [11,12]
List2 = [13,14]

List = List1 + List2
print(List)"""


"""List = [11,12,13,14,15,16]
lenght = len(List)
middle = lenght/2

print("1st list is : ",List(range(0,middle)))
print("2nd list is : ",List(range(middle+1,lenght)))"""

"""Methods Codes"""


"""class Addition:
    def Addition(self ,a,b):
        self.a = a
        self.b = b
        return a + b

class Subtraction:
    def Subtraction(self ,a , b):
        self.a = a
        self.b = b
        return a - b

class Multiplication:
    def Multiplication(self, a , b):
        self.a = a
        self.b = b
        return a * b

class Divition:
    def Divition(self, a , b):
        self.a = a
        self.b = b
        return a / b

add = Addition()
print(add.Addition(3,2))

sub = Subtraction()
print(sub.Subtraction(3,2))

mul = Multiplication()
print(mul.Multiplication(3,2))

div = Divition()
print(div.Divition(3,2))"""


"""class reverse:
    def reverce(self,String):
        str = ""
        for i in String:
            str = i + str
        return str


rev = reverse()
String = input("Enter plz:")
print("Original String is:"+String)
print("Reverce String is:",rev.reverce(String))"""


""""Loops Codes"""

"""def Fibonacci(n):
    if n <= 1:
       return n
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))

Result = int(input("Enter plz How Many item : "))

if Result <= 0:
  print("Invalied Entry")

else:
    print("Fibonacci Sequence:")
    for i in range(Result):
        print(Fibonacci(i))"""


"""for i in range(3):
    for j in range(j>=i and j<=6-i):
        print("#",end="")
print()"""


"""String = input("Enter string : ")
count1 = 0
count2 = 0
for i in String:
    if(i.isdigit()):
         count1 = count1 + 1
    count2 = count2 + 1

print("Number of Digit is :")
print(count1)
print("Number of character is : ")
print(count2)"""

"""String = input("Enter string : ")
if(String =='A' or String =='a' or String =='E' or String =='e' or String=='I'
 or String =='i' or String =='O' or String =='o' or String =='U' or String =='u'):
    print(String, "is a Vowel")
else:
    print(String, "is a Consonant")"""

"""import datetime

Number = int(input("Enter Number"))
month = datetime.date(1900, Number, 1).strftime('%B')
print(month)"""


"""Students = {'01':'Ankita','02':'Ashil','03':'Bhashkar','04':'Gaurav','05':'Rohit','06':'Shubham'}
Data = input("Enter Strudent Info : ")
print(Students.pop(Data))"""


"""def Merge(StrudentName , StrudentNumber):
    return (StrudentNumber.update(StrudentName))
StrudentName = {'01':'Ankita','02':'Ashil','03':'Bhashkar','04':'Gaurav','05':'Rohit','06':'Shubham'}
StrudentNumber = {'07':'2222','08':'3333','09':'4444'}
print(Merge(StrudentName,StrudentNumber))
print(StrudentNumber)"""


"""one = {'1':'krishna'}
two = {'1':'Bhashkar'}
three = {'1':'Jha'}

Resault = dict((k, [one[k], two.get(k), three.get(k)]) for k in one)
print(Resault)"""

