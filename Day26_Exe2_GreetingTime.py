import time

t = time.strftime('%H:%M:%S')
# name = input("Enter your good name : ")

hour = int(time.strftime('%H'))
hour = int(input("Enter the hour as per your time : "))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning ")
elif(hour>=12 and hour<17):
    print("Good Afternoon ")
elif(hour>=17 and hour<20):
    print("Good Evening ")
elif(hour>=20 and hour<0):
    print("Good Night ")