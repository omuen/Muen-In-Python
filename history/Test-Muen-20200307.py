import random
s=0
while s<100:
    x=random.randint(1,20)
    y=random.randint(1,20)
    try:
        u=int(input(str(x)+'+'+str(y)+'='))
        if x+y==u:
            s=s+10
            print('Good')
        else:
            print('Try again')
    except:
        print("Bad answer.")
print('finished')
