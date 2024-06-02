marks= [3, 4, 5, 6, "9"]
# index = [0], [1], [2], [3], [4]


print(type(marks))
print(marks)
print(marks[:])
print(marks[0])
print(marks[1])
print(marks[2])

# Negative indexing
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])


#more methods to print the negarive indexing

print(marks[-3]) #-- suppose we want to print the value of this
print(marks[len(marks)-3])  #-- first need to make it in positive index by using (len) funtion
print(marks[5-3])   #-- len = 5 -3 
print(marks[2])   #-- now we can easily tell the value of index.



if 5 in marks:
    print("is present")
if "9" in marks:
    print("9 is present")
else:
    print("not present")



marks2 = [3, 4, 5, "himanshu"]
if "ansh" in marks2:
    print("Yes present in this list")
if "ans" in "himanshu":
    print("yes present in the argument of list")
else:
    print("no")


#jumpindex --> jump the indexes as given value
marks3 = [3, 4, 5, "himanshu", 6]
print(marks3[:])
print(marks[0:4:2])


#ListComprehension --> On the Way generating the list
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4)]
print(lst)

lst2 = [i for i  in range(20) if i%2==0]
print(lst2)