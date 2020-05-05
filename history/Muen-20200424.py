def pen(principal,years):
  for k in range(years):
    principal = principal + principal * 0.011
  return principal

uuuu = pen(1000,2)
print(uuuu)