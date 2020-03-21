apples=[
    "red","green","red","green","bad","big","red","red","big","green","red","red","big",
    "green","red","bad","green","bad","big","red","green","big","red","green","red","bad","bad",
    "green","red","bad","green","red","big","bad","green","big","red","bad","green","red",'green',
    "green"
];
red=0
green=0
dott=0
baseus=0
for apple in apples:
    if(apple=="green"):
        green = green +1
    if(apple=="red"):
        red=red+1
    if(apple=="bad"):
        dott=dott+1
    if(apple=="big"):
        baseus=baseus+1
        
x = red - green

print("red=" + str(red))
print("green=" + str(green))
print("total = " + str(green+red))
print("x=" + str(x));
print("bad="+str(dott))
print("big=" + str(baseus))
print("pig+pig=?")
