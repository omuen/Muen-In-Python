import random
m=(random.randint(0,10000))
while True:
    a=int(input("Please type a number betwwin 1 and 10000:"))
    if m>a:
        print("it is too small, please try again")
    if m<a:
        print("it is too big, please try again")
    if a == m:
        int(input("Good Job"))
        break 
