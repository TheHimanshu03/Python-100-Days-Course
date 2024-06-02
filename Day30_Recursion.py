'''
factorial(7) = 7*6*5*4*3*2*1
factorial(6) = 6*5*4*3*2*1
factorial(5) = 5*4*3*2*1
factorial(4) = 4*3*2*1
factorial(3) = 3*2*1
factorial(2) = 2*1
factorial(1) = 1
factorial(0) = 1


factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
print(factorial(4))
print(factorial(3))


'''
Fibonacci Series:
0,1,1,2,3,5,8
F(0) = 0
F(1) = 1
F(2) = F(1) + F(0)
F(3) = F(2) + F(1)
F(4) = F(3) + F(2)

F(n) = F(n-1) + F(n-2)

'''


def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
a = int(input("Enter a number : ")) 
for i in range(a):
    print(fibonacci(i))    
