# there are 4 types of Functions Arguments in Python
'''
1. Default Arguments
2. variable length Arguments
3. Keyword Arguments
4. Required Arguments
'''


#1. Required Arguments ---- In this arguments we need to give all the values of arguments before calling the function

def average(a,b):
    avg = (a+b)/2
    print("this value is calling from Required arguments " , avg)

average(5,4)    


#2. Default Arguments ---- In this arguments we need to set the default value of arguments while creating the funtion

def average1(a = 5,b= 4):
    avg1 = (a+b)/2
    print("this value is calling from Default arguments " ,avg1)

average1()

        # We can change the value of arguments while calling the function
average1(3,5)

        # We can change the value of a single arguments while calling the function and the other one will remain same as default
average1(3)
average1(b=6)


#3. variable length Arguments ---- We can pass the attributes as a n times of number by using *

def AvgOfNumber (*number):
    print(type(number))
    sum = 0
    for i in number:
        sum= sum +i
        print("the avg of given number from Veriable length argumets is ", sum/len(number))

AvgOfNumber(5,9)



#3. Keyword Arguments ---- We can pass the attributes as a dictionary by using **

def name(**name):
    print("Hello,", name["Fname"], name["Mname"], name["Lname"])

name(Fname="himanshu", Mname= "-", Lname= "Aggarwal")

