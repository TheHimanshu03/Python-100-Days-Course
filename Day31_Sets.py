# Set is a collection of well defined values.
# set dont contain duplicate items while print.
# cannot mantain the order. ie. we cannot print the values of indexes.

s = {2,4,2,6}
print(type(s), s)

for values in s:
    print(values)
    
for values in s:
    print(s)


s2 = set()  # to print the empty set with set datatype
print(type(s2))


