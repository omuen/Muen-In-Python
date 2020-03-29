apples = [100,300,50,500,200,800,700]
f=apples[0]
g=apples[0]+apples[1]+apples[2]+apples[3]+apples[4]+apples[5]+apples[6]
y=0
i=0
total=0
h=apples[0]
for apple in apples:
  if f<apple:
    f=apple
  if h>apple:
    h=apple
  total=apple+total
  if apple>100:
    i=i+1
    y=y+apple
print('Total of >100g=',y)
print('>100g:'+str(i))
print('Max='+str(f))
print('all=',total)
print('Total=',g)
print('Min=',h)  