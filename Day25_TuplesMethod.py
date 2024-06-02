countries = ("India", "Russia", "Japan", "France", "America")
print(type(countries))

#suppose we want to change the value in tuple----

        # 1. then we need to change that tuple in list first and then use the list operations.
cntry = list(countries)
print(type(cntry))
cntry.append("China")
cntry.pop(3)  # this will remove the value of index
cntry[3] = "London"
print(cntry)

        # 2. Now change the list into tuple to print the tuple
countries = tuple(cntry)
print(countries)
print(type(countries))



# if we can to concatinate two different tuples------

name1 = ("himanshu", "Ravi", "Aryan")
name2 = ("rohit", "Dilip", "patel")
print(type(name1), name1)
print(type(name2), name2)

name = name1 + name2
print(type(name), name)


name = name2 + name1
print(type(name), name)


tup1 = (1,2,3,3,4,5,6,7,7,3,3,3,4)
tup = len(tup1)
print(tup)

newTup = tup1.count(3)
print(newTup)

newTup2 = tup1.index(3)
print(newTup2)