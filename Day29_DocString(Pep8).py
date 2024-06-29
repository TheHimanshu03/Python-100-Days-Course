# DocStrings are the strings that written after the defination of function name, class, methods etc
# It will return the value of string if we want to print
# __doc__  >> using this we can print the DocString


def square(n):
    '''
    Hi I am a doc string
    '''
    print(n**2)

number = int(input("enter a number : "))
print(square(number))    

print(square.__doc__)




# ----------- PEP-8 --------------
# Python Enhancement Programme.

# try >> import this
