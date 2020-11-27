for m in range (1,101):
    if m%3==0:
        if m%5==0:
            print("FizzBuzz")
        else:
            print ("Fizz")
    elif m%5==0:
        print("Buzz")
    else:
        print(m)
