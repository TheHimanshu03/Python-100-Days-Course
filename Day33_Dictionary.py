dic = {
    "Himanshu" : "human being",
    "Spoon" : "object"
}

print(dic["Himanshu"])
print(dic["Spoon"])
print(dic.keys())
print(dic.values())
print("\n")

print(dic.items())


dic_EmployeeID = {
    1732 : "Himanshu",
    1480 : "Rohan",
    1949 : "Shivam",
    2002 : "Arun"
}

print(dic_EmployeeID[1732])
print(dic_EmployeeID[1480])
print(dic_EmployeeID[2002])
print(dic_EmployeeID[1949])
print("\n")

print(dic_EmployeeID)
print(dic_EmployeeID.keys())

print("\n")


dic2 = {
    "Himanshu" : "1",
    "Ajay" : "2",
    "Ankur" : "3",
    "Aryan" : "4"
}

for key in dic2.keys():
    print(f"The value of corrosponding key {key} is {dic2[key]}")