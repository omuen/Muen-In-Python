import turtle
t=turtle.Pen()
colors=['red','orange','yellow','green','blue','purple']
for cat in range(1000):
    t.pencolor(colors[cat%6])
    t.forward(cat)
    t.left(61)
