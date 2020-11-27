import random
n=(random.randint(0,11))
m=(random.randint(0,11))
while True:
    a=int(input(str(m) +'+'+ str( n)+'='))
    if a==m+n:
        print("Good job♥")
        break
    else:
        print ("please try again")
