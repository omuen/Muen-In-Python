def mat(b,y):
  for i in range(y):
    b=b*0.01+b
    print(b)
  return b
x=mat(1000,5)
print("Result=", x)
print("Result=", mat(2000,3))
print("Result=", mat(5000,1))