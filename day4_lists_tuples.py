#Welcome Day 4
# Day 4: Lists and Tuples Foundational Logic

#Lists []
list = [2,1,3,1]
print(type(list))

marks = [94.4 , 76.2 , 82.7 , 96.2, 66.3, 48.1] #-->lists
print(marks)
print(type(marks))
print(len(marks))
print(marks[2])
print(marks[5])
print(marks[3])

student = ["Optimus", 84, "Delhi"]   

#strings --> immutable & lists --> mutable (unchange/change)
str = "hello"
print(str[0])   #    str [0] = y [invalid Item Asignment] in str

str = ["hello", 77.7, 22.1, "world"]
print(str[0])
str [0] = "Great"
print(str)     #     str[0] = y [Valid] in lists

#String Slicings
marks = [87, 44, 93, 67, 72, 90]
print(marks [1:4])  #same as [0:4]
marks = [87, 44, 93, 67, 72, 90]
print(marks [:4]) 
marks = [87, 44, 93, 67, 72, 90]
print(marks [1:]) 
marks = [87, 44, 93, 67, 72, 90]
print(marks [-3:-1]) 
marks = [87, 44, 93, 67, 72, 90]
print(marks [-3:]) 

#List Methods
list = [2, 1 , 3]
list.append(4)  # mutation of list
print(list)  
print(list.sort())
print (list)
print(list.sort(reverse= True) )
print(list)

list = ["banana", "mango", "apple"]
print(list.sort(reverse=True)) #Descending Order; Character z -> a
print(list)

list = ["banana", "mango", "apple"]
print(list.sort()) #Ascending Order; Character a -> z
print(list)

list = ['a','c','h','f','b','g','e','i','j','d','k']
print(list.sort())
print(list)
list = ['a','c','h','f','b','g','e','i','j','d','k']
print(list.sort(reverse=True))
print(list)

list = ['a','c','h','f','b','g','e','i','j','d','k']
list.reverse()
print(list)

list = [2, 1, 3]
list.insert(1,0)
print(list)

list = [2,1,3,1]
list.pop(2)
print(list)

#Tuples ()
tup = (2,1,3,1)
print(type(tup))
print(tup[1])
print(tup[2])

#tup [0] = 5 9Tuple doesnt supprt value assignment)
tup = (1)
print(tup)
print(type(tup))

tup = ("hello")
print(tup)
print(type(tup))

tup = ("hello",)
print(tup)
print(type(tup))

tup = (1, 2, 3, 4,)
print(tup[1:3])
print(type(tup))

tup = (0, 1, 2, 3 )
print(tup.index(0))

tup = (1, 2, 3, 2, 2)
print(tup.count(2))

#Practice Problems
"""WAP to ask the user to enter names of their 3 favorite movies
    & store them in a list."""
movies = []
movies.append(input("Enter your 1st favorite movie: "))
movies.append(input("Enter your 2nd favorite movie: "))
movies.append(input("Enyer your 3rd facorite movie: "))
print(movies)

"""WAP to check if a list contains 
    palindrome of elements"""
list1 = [1, 2, 1]  
list2 = [1, 2, 3]
list3 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse() 
         
if(copy_list1) == (list1):
    print("palindrome")
else:
    print("NOT palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2) == (list2):
    print("palindrome")
else:
    print("NOT palindrome")

copy_list3 = list3.copy()
copy_list3.reverse()
if(copy_list3) == (list3):
        print("palindrome")
else:
    print("NoT palindrome")

list = ["m", "a", "a", "m"]
list = list.copy()
list.reverse()
print(list)

"""WAP to count the number of students with the "A" grade in the following tuple"""
grade = ("A", "D", "A", "B", "C", "A", "B", "D", "A")
print(grade.count ("A"))

""" ["C","D","A","A","B","B","A"]
    Store the above values in a list & sort them from "A" to "D" """
grade = ["C","D","A","A","B","B","A"]
print(grade.sort())
print(grade)


