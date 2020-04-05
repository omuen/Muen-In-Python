apples = [
  "red","green","bad","red","hole","red",
  "yellow",'bad','green','hole','bad','yellow',
  'hole','yellow','hole','green','green'
]
r=0
y=0
h=0
b=0
g=0
t=0
for apple in apples:
  t=t+1
  if apple=='red':
    r=r+1
  if apple=='bad':
    b=b+1
  if apple=='green':
    g=g+1
  if apple=='yellow':
    y=y+1
  if apple =='hole':
    h=h+1
print('hole=',h)
print('red=',r)
print('yellow=',y)
print('bad=',b)
print('green=',g)
print('Total=',t)
print(apples[4:6])
print(apples[7:10])
print('  Done')
print('~ By Muen ~')
print('------- ------- ------- ------ ------ ------ ------')