a = input("enter a interger value to find the table: ")
print("table of {a} is mentioned below")

for i in range(1, 11):
    print(f"{int(a)} * {i} = {int(a)*i}")



''' Suppose if user entered the value in string than this program shows error
  to avoind the error we use try and except method
  please run the below program  '''



b = input("enter a interger value to find the table: ")
print("table of {b} is mentioned below")

#try and except will pass the error and print the value of error and print except value
try:
    for i in range(1, 11):
        print(f"{int(b)} * {i} = {int(b)*i}")
except Exception as e:  # we can use except: only also, if we dont want to the error name.
    print(e)

print("End of program, Thankyou!!")        

# we can also use except Exception as e, and then print (e)  to print that error too.



''' We can define our errors if we want too just by giving the name of that error
Please run below program'''

try:
    num = int(input("enter a number : "))
    d = [0,5]
    print(d[num])

except ValueError:
    print(" Number entered is not an integer number")   # enter the num as "him" to print this error

except IndexError:
    print(" Range is out of index")  # enter the num more than 1 to print this error
