n=[1,2,3,5,9,6,7,0,40,8,10,87,99,55,67,41,38,11,12,13,14,15,16,17,18,19,20]
b=0
s=100
for cat in n:
  if(cat>b):
    b=cat
  if(cat<s):
    s=cat
print("the biggest number is " + str(b))
print("the smallest number is " + str(s))
