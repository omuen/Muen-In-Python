import random
colors=["red","green","orange","blue","yellow","pink","purple"]
answer = input("Do you want to see a spiral? y/n:")
if answer=="y":
    print("Working...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    for x in range(1000):
        print(x);
        t.pencolor(colors[x % 7])
        t.forward(random.randint(3, 50))
        t.left(89)
print("Okay, we're done!")
