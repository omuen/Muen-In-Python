apples = [100,300,50,500,200,800,700]
u=apples[0]
a=apples[0]
for n in apples:
  print(n)
  if u<n:
    u=n
  if a>n:
    a=n
print("Max="+str(u)+'g')
print('Min='+str(a)+'g')