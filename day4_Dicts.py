#Welcome Day 4 part-2
#Dictionary and Sets
info = {
    
    "key" : "value",
    "name" : "MohammedFaizaan",
    "subjects" : "Math, Physics, Chemistry, English",
   "learning" : "Coding",
   "topic" : "Dicts & Sets",
   "age" : 18,
   "is_adult" : True,
   "marks" : 94.4,
   94.4 : 100.0

}
print(info)
print(type(info))

info2 = {
    
    "name" : "Ayaan",
    "subjects" : "Java, Web development, C++",
    "age" : 24,
    "is_adult": True,
    "marks": 87.5, 
    87.4 : 100.0

}


print(info2["name"])
print(info2["age"])
print(info2["subjects"])

info2["name"] = "Kunal" #Overwrite
info2["surname"] = "Kumar"
print(info2)

null_dict = {}
print(null_dict)
null_dict["name"] = "Virtual Studio Code"
print(null_dict)

#Nested Dictionary
student = {
    "name" : "A",
    "subjects" : {
        "Phy" : 97,
        "Chem" : 90,
        "Math" : 92
    }
}
print(student["subjects"]["Math"])

#Dictionary Methods --> dic.keys, dic.values
student = {
    "name" : "X",
    "subjects" : {
        "Phy" : 98,
        "Chem" : 95,
        "Math" : 97
    }
}
print(student.keys())
print(len(student))
print(list(student.keys()))
print(len(list(student.keys()))) #Use of functions overview
print(student.values())

#Method --> dic.item 
student = {
    "name" : "L",
    "subjects" : {
        "Phy"  : 90,
        "Chem" : 92,
        "Math" : 96
    }
}
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])

#Method --> dic.get
student = {
    "name" : "F",
    "subjects" : {
        "Phy" : 91,
        "Chem" : 93,
        "Math" : 90
    }
}
print(student["name"])
print(student.get("name")) #same

#Method --> dic.update
student = {
    "name" : "S",
    "subjects" : {
        "Phy" : 99,
        "Chem" : 99,
        "Math" : 97
    }
}

student.update({"city" : "Hyderabad"})

print("student")

