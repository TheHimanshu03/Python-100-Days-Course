for i in range(5):
    print(i)

else:
    print("sorry there is no i left")


j = 0
while j<7:
    print(j)
    j = j + 1
    if (j == 5):
        break

else:
    print("Printing Else Statement")


for x in range(5):
    print("iteration of {} in for loop". format(x+1))
else:
    print("block in loop ")  

print("out from loop")      