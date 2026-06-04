#Welcome Day 7
# day7_for_loops.py
# Day 7: for loops, range(), break, continue, nested loops

#Break for while loop
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

nums = (1,4,9,16,25,36,49,64,81,100,36)

x = 36

i =  0 
while i < len(nums):
    if(nums [i] == x):
        print("FOUND at idx", i)
        break 
    else:
        print("finding..")
    i += 1

print("loop ended")

#Continue for while loop
i = 0
while i <= 5:
    if(i == 3):
     i += 1
     continue
    print(i)
    i += 1

i = 1 
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue #skip
    print(i)
    i += 1

##For Loops
list = [1, 2, 3, 4, 5]
for val in list:
    print(val)

veggies = ["spinach", "cucumber", "potato", "carrot", "tomato", "onion"]
for list in veggies:
    print(list)

tup = (1,2, 7, 4, 6, 9, 2)
for num in tup:
    print(num)

str = "Radiation" #Individual characters print
for cha in str:
    print(cha)

el = "artificial general intelligence AGI"
for ele in el:
    print(ele)
else: 
    print("END") #else optional

#name = input("enter a name: ")
name = "Python"
for char in name:
    if(char == 'n'):
        print("n found")
        break
    print("char")
else:
    print("END")

#Practice using for
print("Q.1")
"""Print the elements of the following list using a loop:
[1, 4, 9, 25, 36, 49, 64, 81, 100]"""
list = [1, 4, 9, 25, 36, 49, 64, 81, 100]
for val in list:
    print(val)

print("Q,2")
"""Scearch for a number x in this tuple using loop
[1, 4, 9, 25, 36, 49, 64, 81, 100]"""
tup = (1, 4, 9, 25, 36, 49, 64, 81, 100, 81) #linear scearch

idx = 0
x = 81
for el in tup:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1

#Range()
print(range(5))

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

#Range function methods:  range(start?,stop,step?)
seq = range(10)
for i in seq:
    print(i)

print("Syntax")
for i in range(10): #range(stop)
    print(i)

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)

#for even numbers
for i in range(2, 101, 2):
    print(i)
#for odd numbers
for i in range(1, 101, 2):
    print(i)

#Practice using for & range()
print("Q.1")
"""Print numbers from 1 to 100."""
for i in range (1, 101):
    print(i)

print("Q.2")
"""Print  numbers from 100 to 1."""
for i in range (100, 0, -1):
    print(i)

print("Q.3")

"""Print the multiplication table of a number n"""
n = int(input("enter a number: "))
for i in range(1, 11):
    print(n * i)

#Pass statement (skip) placeholder for future code.
for i in range(5):
    pass

print("some useful work")

#Practice Problems
print("Q.1")
"""WAP to find the sum of first n natural numbers. (using while)"""
n = 7
sum = 0
i = 1 
while i <= n:
    sum += i
    i += 1

print("total sum =", sum)

print("Q.2")
"""WAP to find the factorial of first n natureal numbers. (using for)"""
#while
n = 4
fac = 1
i = 1
while i <= n:
    fac *= i
    i += 1

print("total factorial =", fac)

#for
n = 5
fac = 1
for i in range(1, n+1):
    fac *= i
print("factorial =", fac)

#Revision + for Loop concept
for i in range(5):
    print(i) #0,1,2,3,4

for i in range(1,11,2):
    print(i)

name = "Faizaan"
for char in name:
    print(char)

movies = ["Inception", "Titanic", "Interstellar"]
for movie in movies:
    print(movie)

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i %2 == 0:
        continue
    print(i)

#Nested Loops - star pattern
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

#nested loops - multiplicatiion table
for i in range(1,6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
print()

