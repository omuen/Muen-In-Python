answer = input('Do you want to see a spiral,Yes or no?')
if answer =='Yes':
    print('Working...')
    import turtle
    t=turtle.Pen()
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(89)
    print('Well done')
else:
    print('???')

print('By Muen')
               #Meaw
