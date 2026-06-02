#Welcome Day 5
#Day:5 Sets, Problems

collection = {1, 2, 3, 4, 5} #Set
print(collection)
print(type(collection))

collection = {1, 2, 2, 2, 3, "hello", "world", "world", 4}
print(collection)
print(len(collection))

collection = {}
print(collection)
print(type(collection)) #Type Dict not set

collection = set()
print(type(collection)) #Empty Set; Syntax

values = {9, 9.27, 2.0, 2, 0} # Python prints float value 2 instead of 2.0 in set
print(values)

value = {9.0, "9"}
print(value)

#Set Methods
set = set()
set.add(1)
set.add(2)
set.add(2)
set.remove(2)
set.add(("code"))
print(set)

collection = {"hello", "user", "processing", "python", "logic"}

print(collection.pop())
print(collection.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1)
print(set2)

set3 = {7, 9, 2, 0}
set4 = {2, 7, 5, 4}

print(set3.intersection(set4))
print(set3)
print(set4)

#Practice Questions
"""Store following word meanings in a python dictionary
 table : "a piece of furniture", "list of facts & figures
 cat: "a small animal" """

dictionary = { 
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]

}
print(dictionary) #1st key,value & 2nd key,value pair

""" You are given a list of subjects for students
 Assume one classroom is required for 1 subject.
 How many classrooms are needed by all students.
  "python", "java", "C++" "python" "javascript" 
 "java" "python", "java", "C++", "C" """

subjects = { 
    "python", "java", "c++", "python", "javascript", "java",
    "python", "java", "java", "c++", "c"
}

print(len(subjects))

"""WAP to enter marks of 3 subjects from a user & store them in the dictionary.
 Start with an empty dictionary & add one by one.
 Use subject name as key & marks as value """

marks = {}

x = int(input("enter phy marks: "))
marks.update({"phy" : x})

y = int(input("enter chem marks: "))
marks.update({"chem" : y}) 

z = int(input("enter math marks: "))
marks.update({"math" : z})

print(marks)

"""Figure out a way to store 9 & 9.0 as separate values in the set"""
values = {
    ("float", 9.0),
    ("int", 9),
}
print(values)


