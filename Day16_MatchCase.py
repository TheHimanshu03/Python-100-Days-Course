x = int(input("enter a value of x"))
match x:
    case 0:
        print("x is 0")
    case 5:
        print("x is 5")
    case 10:
        print("x is 10")
    


# Match Case is use to match the values with output and input.
# if any case is got true the program will automatic stop itself.
# - is use to default value (also called as else statement)  
    case _ if (x>100):
        print("x is greater than 100")
    case _ if (x<50):
        print("x is smaller than 50")

# We can use the default case as many time as we want using the condition.
        

    case _:    
         print("the given value by the user is: ", x)

# the above statement is basically use to terminate the program.
        