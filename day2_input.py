#Welcome Day 2
#Input in Python

#string input
name = input("enter your name: ")
print("Welcome ", name)
#int input
name = int(input("enter your age: "))
print("You entered", name)
#float input
money = float(input("money: "))
print("You entered", money)

val = input("enter some value: ")
print(type(val), val)

#Conditional Statememts if-elif-else (SYNTAX)
age = int(input("Your age: "))
if (age >= 18):
    print("You are eligible to vote")
elif(age < 18):
    print("You are Underage")
#Traffic Light

light = input("light color: ")

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Ready to stop")
elif(light == "green"):
    print("Go!")
else:
    print("light is Broken")

 #Grades of Students

marks = int(input("Enter your marks: "))
if("mark = 100"):
    print("A+")
elif(marks >= 90 and marks < 100):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
elif(marks >= 60 and marks < 70):
    print("D")
elif (marks >= 50 and marks < 60):
    print("E")
else:
    print("F")


#Single / Ternary operator

food = input("food: ")
eat = "Yes" if food =="cake" else "no"
print(eat)

food = input("food: ")
print ("sweet")if food == "cake" or food == "jalebi" else print("not sweet")

#Clever if/ Ternary operator
age = int(input("age : "))
vote = ("yes", "no") [age < 18]

sal = float(input("salary: "))
tax = sal*(0.1, 0.2) [sal<=50000]
print(tax)

#Arithmatic Operators
a = 2
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#Relational/Comparision Operators
a = 50
b = 20

print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#Assignement Operators
num = 10
num = num + 10
print("num: ", num) #20

num = 10
num += 10 
print("num: ", num) #20

num = 10
num *= 5
print("num: ", num) #50

num = 10
num /= 5
print("num: ", num) #2

num = 10
num %= 5
print("num: ", num) #0

num = 10
num **= 5
print("num: ", num) #1,00,000

#Logical Operators

val1 = False
val2 = False
print("AND operator:", val1 and val2)

print("OR operator:", (a==b) or (a > b))

#Type Coversion
a = 2
b = 4.25

sum = a + b
print(sum)

#Type Cast
a = int("2")
b = 4.25

print(type(a))
print(a + b)

