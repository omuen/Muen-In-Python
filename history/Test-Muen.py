for i in range(1,10):
  for j in range(1,10):
    if(j<i):
        continue
    print(str(i) + '*' + str(j) + '=' + str(i*j))
