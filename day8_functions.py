#Welcome Day 8
#day8_functions.py
#Day 8: Functions, Problems
a = 2
b = 7
sum = a+b
print(sum)
#More lines of code
a = 5
b = 10
sum = a+b
print(sum)
#More lines of code
a = 99
b = 1
sum = a + b
print(sum)

#Function -few lines of code, single print statement, decereased redundancy --> Better Code
print('def, return, sum(x), calc_sum(x)')
def calc_sum(a, b): #a,b parameters
    sum = a + b
    print(sum)
    return sum
calc_sum(7, 7) #function call; arguments
calc_sum(5, 10)
calc_sum(2, 7)

def calc_sum(a, b):
    return a + b
sum = calc_sum(3, 4), calc_sum (2, 7), calc_sum(0, 2)
print(sum)

def total (a, b):
    return a + b
add = total(24502, -79342), total (-2034, 111), total(-3, 3), total(-89, -10)
print(add)

def calc_mul(a, b):
    return a * b* b* a
mul = calc_mul(4,2), calc_mul(2, 3)
print(mul)

def print_hello():
    print("hello")
output = print_hello()
print(output) #None (if no return)

#avergae of 3 numbers
def sum(a, b, c):
    return a + b + c /3
add = sum(1, 3, 2)
print(add)

def avg_calc(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
avg_calc(1, 2, 3)
avg_calc(99,98,96)

#Types of Functions (print(), len(), type(), range().)
print()
print("Quantum", "Computing") #sep = " " (space)

print("Quantum") #end = "\n"
print("Computing")

print("Quantum", end = ' ') # end = " " {To print multiple values on the same line"
print("Computing")

print("Quantum", end= '$')
print("Computing")

#Default Parameters
def cal_product(a = 7, b= 7):
    print(a * b)
    return a * b

cal_product()

def calc_product(a, b= 7): # Default Args, then Non-default Args
    print(a * b)
    return a * b

calc_product(2) # Passes 2 in a on default parameter of (a, b = var)

#Practice Questions
"""WAF to print the length of a list. (list the parameters)"""
cities = ["Hyderabad", "Gurgaon", "Delhi", "Mumbai", "Goa", "Noida", "Bengaluru"]
heroes = ["Batman", "Superman", "Captain America", "Black Widow"]  
print(len(cities)) #or

def print_len(list):
    print(len(list))
print(len(heroes))
    
"""WAF to print the elements of a list in a single line. (list is the parameters)"""
       
books = ["Atomic Habits", "Millionaire Mindset", "48 Rules of Power", "Think Rich, Grow Rich", "Essentialism", "Deep Work", "Get Things Done"]
print(books ,end = "\n")
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item , end= " ")

print_list(books)