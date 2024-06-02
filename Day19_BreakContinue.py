for i in range(11):
    if (i == 10):
        break
    print("5 X ", i+1, "=" , 5 * (i+1))

print("Loop is over ")


# Break Statement means : Loop se bhar aa jao


for i in range(11):
    if (i == 5):
        continue
    print("5 X ", i+1, "=" , 5 * (i+1))

print("We have skipped the value of 6 ")



for i in range(1, 100, 1):
    print(i, end= " ")
    if (i == 50):
        break
    else:
        print("mission impossible")

print("ThankYou!!")        


while True:
    number = int(input("enter a positive number : "))
    print(number)
    if not number > 0:
        break

print("ThankYou!!")        
