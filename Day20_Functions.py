def CalculateGmean(a,b):
    mean =(a*b)/(a+b)
    print("the calculated mean of the given number is " , mean)


def GreaterNumber(a,b):
    if (a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")

a = 5
b = 6
Gmean = (a*b)/(a+b)
print(Gmean)
print("through Function")
CalculateGmean(a,b)
print(GreaterNumber(a,b))



c = 5
d = 3
Gmean2 = (c*d)/(c+d)
print(Gmean2)
print("through Function")
CalculateGmean(c,d)
print(GreaterNumber(c,d))