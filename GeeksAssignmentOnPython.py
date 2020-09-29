# Arrays

# To Find Largest Element In The Arrays

"""def largest(Array,L):
    max = Array[0]
    for i in range(1,L):
        if Array[i] > max:
            max = Array[i]
    return max

print("Enter the Number : ")
Array = [int(i) for i in input().split()]
L = len(Array)
Ans = largest(Array,L)
print("Largest Element is : ",Ans)"""

# Find remainder of arr[0] * arr[1]

"""def FindRemainder(Array,L,Divisor):
    mul = 1
    for i in range(L):
        mul = (mul * (Array[i] % Divisor)) % Divisor
    return mul % Divisor

print("Enter The Array Plz : ")
Array = [int(i) for i in input().split()]
L = len(Array)
Divisor = int(input("Enter Divisor Plz : "))
Ans = FindRemainder(Array,L,Divisor)
print("Number is:",Ans)"""

# check if a string is palindrome or not

"""def reverse(s):
    return s[::-2]

def isPalindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    else:
        return False

s = input("Enter the string : ")
ans = isPalindrome(s)
if ans == True:
    print("YES")
else:
    print("NO")"""

# remove i’th character from string in Python

"""String = input("Enter The String :")
S = len(String)
print("Original String is : ",String)

NewString = ""
k = int(input("Enter Index Plz:"))
for i in range(0,S):
    if i != k:
        NewString +=  String[i]
print("The New string is : "+NewString)"""

# Check if a Substring is Present in a Given String

"""def Check(String,Sub_string):
    if (String.find(Sub_string) == -1):
        return print("NO")
    else:
        return print("YES")

String = input("Enter String plz :")
Sub_string = input("Enter Sub String plz :")
Check(String,Sub_string)"""

"""String = input("Enter String is :")
ans = len(String)
ans1 = String.split()
print("Length of String is:",ans,ans1)"""

# Program to accept the strings which contains all vowels

"""def check(String):
    vowels = set('aeiouAEIOU')
    s = set({})
    for char in String:
        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("NOT Accepted")

if __name__ == "__main__":
    String = input("Enter the String :")
    #String = String.lower()
    check(String)"""


# Count the Number of matching characters in a pair of string

"""def check(string1, string2):
    a, b = 0, 0

    for i in string1:
        if string2.find(i) >= 0 and b == string1.find(i):
            a += 1
        b += 1
    print(" Total Matching Characters are :", a)
    print(" Total Characters are : ",b)


def main():
    string1 = input(" Enter 1st String : ")
    string2 = input(" Enter 2nd String : ")
    check(string1, string2)


if __name__ == "__main__":
    main()"""

#Remove all duplicates from a given string in Python

"""from collections import OrderedDict

def RemoveDuplicatesWithoutOrder(str):
    return "".join(set(str))

def RemoveDuplicatesWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))

if __name__ == "__main__":
    str = input(" Enter String : ")
    print(" Without Order : ",RemoveDuplicatesWithoutOrder(str))
    print(" With Order : ",RemoveDuplicatesWithOrder(str))"""

#Program to check if a string contains any special character

"""import re
def run(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(string) == None):
        print("String Accepted")
    else:
        print("String is not accepted.")


if __name__ == '__main__':
    string = input(" Enter the string : ")
    run(string)"""

