#Welcome Day 6
#Day 6 Loops Part 1
#Function of Loop + Problems on while loop


#while True:
    #print("hello") --> prints hello infinitely

print("hi")
count = 1
while count <=5 :
    print("hello") 
    count += 1 
print(count)

i = 1
while i <= 100:
    print("Error", i)
    i+=1

print("Stop")

i = 1
while i <=5:
    print(i)
    i += 1
print("Loop ended")

i = 5
while i >= 1:
    print(i)
    i -= 1

print("looped")

#Practice Problems
print("Q.1")
"""Print numbers from 1 to 100"""
num = 1
while num <= 100:
    print(num)
    num += 1

print("Q.2")
"""Print numbers from 100 to 1"""
num = 100
while num >= 1:
    print(num)
    num -= 1

print("Q.3")
"""Print the multiplication table of a number of n"""
i = 1
while i <= 10:
    print(27*i)
    i += 1

#Multiplication Table of 'x' number 
n = int(input("enter a number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

print("Q.4")
"""Print the elemrents of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]"""
nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1 

nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["Saitama", "Ayanakoji", "Tanjiro", "Aizen"]

#traverse
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1