# name = "himanshu"
# print(name)
# name2 = 'himanshu2'
# print(name2)
# # name3 = "himanshu is learning a coding language i.e. "python" 
# # print(name3)



# # The above string throws an error. to overcome of this we have two options

#     #-- either we use \before using the double inverted comma ("")
# name4 = "himanshu is learning a coding language i.e. \"python" 
# print(name4)
#     #-- or we can use the string that enclosed in single inverted comma ('')
# name5 = 'himanshu is learning a coding language i.e. "python'
# print(name5)


# # if we want to write three lines of string: (We need to enlclosed in triple inverted comma (''' ''')
# name6 = '''nsfdsfsd
# sdfkhds'f
# dsjfdjsf
# dsjkfdskf
# '''
# print(name6)

# # if we want to print the character of the string:
#     #-- we can use the index numbers.
# name7 = "himanshu"
# print(name[0])

#     #-- we can use the loop if we have such a bigger string
# for x in name6:
#     print(x)


#---------------  String Slicing-------------


fruit = "mango"  
print(len(fruit))
print(fruit[0:5]) # including 0 but not 5
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5]) # it will take automatic 0 as starting index
print(fruit[0:-3]) # it will take (0: len(fruit)-3) i.e. (0:2) .. which including 0 but not 2.
print(fruit[-3:-1]) # it will take (len(fruit)-3): len(fruit)-1) i.e. (2:4) .. which including 2 but not 4.
print(fruit[-4:-2])
