import time

name = "osiel"

name= str(input("What is your name?:"))

Wakeup = "wake"

Wakeup = str(input("What time do you want to wake up?:"))


# initializing string
strn = "GeeksforGeeks"

# printing geeksforgeeks after delay
# of each character
for i in range(0, len(strn)):
    print(strn[i], end="")
    time.sleep(2)