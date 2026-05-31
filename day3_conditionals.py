#Welcome Day 3
# Day 3: Problems, Strings and Conditional Statements
#Practice Question
first = int(input("enter first number: "))
second = int(input("enter second number: "))

print("sum = ", first + second)

side = float(input("enter a square side: "))

print("area = ", side * side)

a = float(input("enter first number: "))
b = float(input("enter second number: "))

print("avg =", a+b/2)

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print(a >= b)

#Strings
str1 = "This is a string."
str2 = 'This is a string.'
str3 = "'This is a sring.'"

str = "This is a string operation.\n escape sequence characters."
print(str)

str = "This is a string operation.\t tab sequence characters."
print(str)

#Concatenation of Strings

str1 = "Escape"
str2 = "theMatrix"

print(str1 + str2)

str1 = "Mohammed"
str2 = "Faizaan"
final_str = str1 + str2
print(final_str)

str1 = "lengths"
len1 = len(str1)
print(len1)

str2 = "string"
len2 = len(str2)
print(len2)

final_str = str1 + "  " + str2
print(final_str)
print(len(final_str))

#Indexing
str = "Index"
ch = str [4]
print(ch)

str = "Python Code"
print(str[6])

#Slicing
str = "Score_Board"
print(str[1:6])

str = "Foundation"
print(str[4:len(str)])

str = "Technique"
print(str[:7])  #[0:4]

str = "Negative"
print(str[-4:-1])

#String Functions
str = "I am studying Python"
print(str.endswith("on"))

str = "i am studying Python"
print(str.capitalize())
print(str)

str = "I am studying Python"
print(str.replace("Python" , "Artificial Intelligence"))

str = "I am studying Python"
print(str.find("y"))

str = "I am studying Python"
print(str.find("q"))

str = "I am good studying Python good"
print(str.count("good"))

str = "I am studying Python, I want to be a Programmer"
print(str.count("a"))
#str. (more lists of functions in strings)

#Practice Problem
"""WAP to input user's first name &  print its length"""
name = input("enter your name : ")
print("length of your name is: ", len(name))

#Conditional Statement
age = int(input("enter age: "))

if (age >= 18):
    print("can vote & for license")
    print("can drive")
elif (age < 18):
    print("under the age of 18")

marks = int(input("enter your marks: "))

if (marks >= 90):
    grade ="A+"
elif (marks >= 80):
    grade = "A"
elif (marks >= 70):
    grade = "B"
elif (marks >= 60):
    grade = "C"
elif (marks >= 50):
    grade = "D"
else:
    grade = "E"

print("grade of student -> ", grade)

#Nesting

age = int(input("Your Age: "))

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:       
    print("cannot drive")    
