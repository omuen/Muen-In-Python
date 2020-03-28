apples = [100,300,50,500,200,800,700]
f=apples[0]
for apple in apples:
  if f<apple:
    f=apple
print('Max='+str(f))
h=apples[0]
for apple in apples:
  if h>apple:
    h=apple
print('Min=',h)
g=apples[0]+apples[1]+apples[2]+apples[3]+apples[4]+apples[5]+apples[6]
print('Total=',g)
total=0
for apple in apples:
  total=apple+total
print('all=',total)
i=0
for apple in apples:
  if apple>100:
    i=i+1
print('>100g:'+str(i))
y=0
for apple in apples:
  if apple>100:
    y=y+apple
print('Total of >100g=',y)  