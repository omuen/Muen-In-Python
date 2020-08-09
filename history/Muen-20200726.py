def miles(a,b,x):
  if x=='Meow':
    return a+b
  elif x=='woof':
    return a-b
  elif x=='N O T H I N G':
    return a*b
  elif x=='NOTHING':
    return a*a+b*b
  else:
    return('MMMMMEEEEEOOOOOWWWWW')


print('~~Made~By~Muen~~')
c=miles(3,6,'Meow')
print(c)

c=miles(6,3,'woof')
print(c)

c=miles(6,3,'N O T H I N G')
print(c)

c=miles(3,6,'N O T H I N G')
print(c)

c=miles(3,6,'NOTHING')
print(c)

c=miles(3,6,'WWW')
print(c)