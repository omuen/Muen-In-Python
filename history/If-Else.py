import random
scores=0
while scores<100:
  x=random.randint(0, 100)
  y=random.randint(0, 100)
  r = int(input(str(x) + "+" + str(y) + "="))
  if(x+y==r):
      scores=scores+10
      print("You are right.")
  else:
      scores=scores-5
      print("Your are wrong.")
  print("Your Scores: " + str(scores))
