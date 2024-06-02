name = "Himaanshu"
print(name)
print(len(name)) #tells the string lenght.
print(name.upper()) #make the string in upper case.
print(name.lower()) #make the string in lower case.

name2 = "!!!!Himanshuu!!!!"
print(name2.rstrip("!")) # Only rmoves the trailling symbols. Not for the starting symbols.
print(name.replace("Himanshu", "Coder")) # will replace the all the values of name(himanshu) with Coder.

name3 = "hi himanshu this side"
#right now the name3 is having a string > means a single value is present in a string. We can split the string into Lists
print(name3.split()) #split the strings in the lists.
print(name3.capitalize()) # this will capitalize the first word of string and rest character is in lower case.
print(len(name3))
print(len(name3.center(50))) #string.center(x) > will add the spaces before the string and make the string length as x.
print(name.count("a")) # tells the no of occurance is coming in string.
print(name.endswith("u")) # tells the string ends with the given attribute.
print(name3.endswith("is",7 ,16)) #tells the string ends with given attribute from index 4 to 15.
print(name3.title()) # make the string every word first letter captial
print(name3.find("is")) #give the first occurance in the string, where the attribute is present. If present gives true and not then gives -1.
# print(name3.index("ish")) #throws error and exit from the program (if the value is not found).
print(name.isalnum()) # give the output as TRUE if the string contains only (a-z, A-Z, 0-9). Alphanumeric
print(name.isalpha()) # give the output as TRUE if the string contains only (a-z, A-Z). Alphabatics

name4 = "Hi Coder This Side"
print(name4.istitle()) # gives true/false if the first letter of each word in string is capital.
print(name4.islower()) # gives true/false if the first letter of each word in string is small.
