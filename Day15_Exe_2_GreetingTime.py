import time

name = input("Enter your good name ")
print("\n")


timestamp = time.strftime('%H: %M: %S')
print(timestamp)
times = int(time.strftime('%H'))
if (1 <= times <12):
    print("Good Morning", name, "its.", timestamp )
elif (12 <= times <=17):
    print("Good Evening", name, "its.", timestamp )
else:
    print("Good Night", name, "its.", timestamp )
